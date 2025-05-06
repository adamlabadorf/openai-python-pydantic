import re
import logging
import argparse
from typing import List

def convert_typed_dict_to_pydantic(filename: str) -> List[str]:
    """
    Converts TypedDict definitions to Pydantic BaseModel definitions, supporting multi-line type hints for fields.
    """
    logging.info(f'Reading file: {filename}')
    with open(filename, 'r') as f:
        source_lines = f.readlines()

    out = []
    i = 0
    n = len(source_lines)
    classes = []
    while i < n:
        line = source_lines[i]
        logging.debug(f'Processing line {i}: {line.strip()}')

        # always remove this
        line = re.sub(r',?\s*total=False', '', line)

        # track class names so we can call build_model() on them later
        if m := re.match(r'^class (.*)\(.*$', line):
            class_name = m.group(1)
            classes.append(class_name)
            logging.info(f'Found class definition: {class_name}')

        if re.match(r'^from __future__ import annotations$', line):
            # these might be redundant, but it doesn't hurt to have them
            logging.debug('Adding Pydantic and typing imports after __future__ import')
            out.append('from pydantic import BaseModel, Field\n')
            out.append('from typing import List, Optional\n')
            i += 1
            continue
            
        # base classes
        elif m := re.match(r'^from typing import (.*)$', line):
            imports = set([x.strip() for x in m.group(1).split(',')])
            if 'Iterable' in imports:
                imports.remove('Iterable')
            imports.add('Optional')
            new_line = f'from typing import {",".join(imports)}\n'
            logging.debug(f'Updated typing imports: {new_line.strip()}')
            out.append(new_line)
            i += 1
            continue

        elif re.match(r'^from typing_extensions import', line):
            new_line = re.sub(r',?\s*Required,?', '', line)
            new_line = re.sub(r',?\s*TypedDict,?', '', new_line)
            new_line = re.sub(r',?\s*TypeAlias,?', '', new_line)
            logging.debug(f'Updated typing_extensions import: {new_line.strip()}')
            if not re.match(r'from .* import\s*$', new_line):
                out.append(new_line)
            i += 1
            continue

        elif re.match(r'.*TypedDict', line):
            new_line = re.sub(r'TypedDict', 'BaseModel', line)
            logging.info(f'Converted TypedDict to BaseModel: {new_line.strip()}')
            out.append(new_line)
            i += 1
            continue

        elif re.match(r'^[a-zA-Z_]\w+:\s*TypeAlias', line):
            new_line = re.sub(r':\s*TypeAlias', '', line)
            logging.info(f'Converted TypeAlias to field: {new_line.strip()}')
            out.append(new_line)
            i += 1
            continue

        elif re.match(r'^from pydantic import BaseModel$', line):
            out.append(line)
            i += 1
            continue

        # Multi-line field detection
        field_match = re.match(r'(\s*)([a-zA-Z_]\w*):\s*(.*)', line)
        if field_match:
            indent = field_match.group(1)
            var_name = field_match.group(2)
            var_type_part = field_match.group(3)
            var_default = None
            type_lines = [var_type_part]
            open_brackets = var_type_part.count('[') - var_type_part.count(']')
            logging.debug(f'Parsing field: {var_name} (initial type: {var_type_part})')

            # Continue accumulating lines if brackets are unbalanced or line ends with ',' or is obviously incomplete
            while (open_brackets > 0 or (type_lines[-1].strip().endswith(',') or type_lines[-1].strip() == '')) and i + 1 < n:
                i += 1
                next_line = source_lines[i].rstrip('\n')
                # Remove trailing comments and whitespace
                next_line_clean = next_line.split('#')[0].rstrip()
                type_lines.append(next_line_clean)
                open_brackets += next_line_clean.count('[') - next_line_clean.count(']')
                logging.debug(f'  Continued field line: {next_line_clean}')

            var_type_full = ' '.join(type_lines).strip()

            # Check for default value
            if '=' in var_type_full:
                var_type_split = var_type_full.split('=', 1)
                var_type = var_type_split[0].strip()
                var_default = '= ' + var_type_split[1].strip()
            else:
                var_type = var_type_full
                var_default = None

            if 'Required' in var_type:
                var_type = re.sub(r'Required\[(.*?)\]$', r'\1', var_type.strip())
            elif not var_type.startswith('Optional['):
                var_type = f'Optional[{var_type}]'

            var_type = re.sub(r'Iterable', r'List', var_type)
            if var_name == 'schema':
                var_name = 'schema_'
                var_default = '= Field(default=None, alias="schema")'
            if not var_default or not var_default.strip():
                var_default = "= None"
            # Reconstruct the original field lines for the comment
            original_lines = [line.rstrip('\n')] + [source_lines[j].rstrip('\n') for j in range(i - len(type_lines) + 2, i + 1)]
            original_type = ' '.join(original_lines)
            original_type = re.sub(r'\s+', ' ', original_type)

            var_type = re.sub(r'\s+', ' ', var_type)

            logging.info(f'Converted field: {var_name}: {var_type} {var_default}')
            #out.append(f"{indent}{var_name}: {var_type} {var_default}\n{indent}# old {original_type}\n")

            var_type = var_type.strip().lstrip().replace('"',"'")

            out.append(f"{indent}{var_name}: \"{var_type}\"{var_default}\n{indent}\n")
            i += 1
            continue

        # If not matched, just copy the line
        out.append(line)
        i += 1
    
    for cls in classes:
        logging.info(f'Resolving forward refs for class: {cls}')
        out.append(f'{cls}.model_rebuild()\n')
    logging.info('Conversion complete.')
    return out

def main():
    parser = argparse.ArgumentParser(description='Convert TypedDict definitions to Pydantic BaseModel definitions.')
    parser.add_argument('input_file', help='Input Python file with TypedDicts')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable debug logging')
    args = parser.parse_args()

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=log_level)

    logging.info('Starting conversion process')
    result = convert_typed_dict_to_pydantic(args.input_file)
    print(''.join(result))

if __name__ == "__main__":
    main()
