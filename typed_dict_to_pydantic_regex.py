import re
import sys
from typing import List

def convert_typed_dict_to_pydantic_regex(source_lines: List[str]) -> List[str]:
    """
    Converts TypedDict definitions to Pydantic BaseModel definitions, supporting multi-line type hints for fields.
    """
    out = []
    i = 0
    n = len(source_lines)
    while i < n:
        line = source_lines[i]

        # base classes
        if re.match(r'(\s*)class (\w+)\(([^)]*TypedDict[^)]*)\):', line):
            new_line = re.sub(r'TypedDict', 'BaseModel', line)
            new_line = re.sub(r',?\s*total=False', '', new_line)
            out.append(new_line)
            i += 1
            continue

        elif re.match(r'^from typing_extensions.*(Required|TypedDict)', line):
            new_line = re.sub(r',?\s*Required,?', '', line)
            new_line = re.sub(r',?\s*TypedDict,?', '', new_line)
            new_line = re.sub(r',?\s*TypeAlias,?', '', new_line)
            if not re.match(r'from .* import\s*$', new_line):
                out.append(new_line)
            out.append('from pydantic import BaseModel')
            i += 1
            continue

        elif re.match(r'^[a-zA-Z_]\w+:\s*TypeAlias', line):
            new_line = re.sub(r':\s*TypeAlias', '', line)
            out.append(new_line.strip() + f' # old {line}')
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
            # Continue accumulating lines if brackets are unbalanced or line ends with ',' or is obviously incomplete
            while (open_brackets > 0 or (type_lines[-1].strip().endswith(',') or type_lines[-1].strip() == '')) and i + 1 < n:
                i += 1
                next_line = source_lines[i].rstrip('\n')
                # Remove trailing comments and whitespace
                next_line_clean = next_line.split('#')[0].rstrip()
                type_lines.append(next_line_clean)
                open_brackets += next_line_clean.count('[') - next_line_clean.count(']')
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
                var_type = re.sub(r'Required\[(.*?)\]', r'\1', var_type)
            elif not var_type.startswith('Optional['):
                var_type = f'Optional[{var_type}]'
            var_type = re.sub(r'Iterable', r'List', var_type)
            if not var_default or not var_default.strip():
                var_default = "= None"
            # Reconstruct the original field lines for the comment
            original_lines = [line.rstrip('\n')] + [source_lines[j].rstrip('\n') for j in range(i - len(type_lines) + 2, i + 1)]
            original_type = ' '.join(original_lines)
            original_type = re.sub(r'\s+', ' ', original_type)

            var_type = re.sub(r'\s+', ' ', var_type)

            out.append(f"{indent}{var_name}: {var_type} {var_default}\n{indent}# old {original_type}\n")
            i += 1
            continue

        # If not matched, just copy the line
        out.append(line)
        i += 1
    return out

def main():
    if len(sys.argv) < 2:
        print("Usage: python typed_dict_to_pydantic_regex.py <input.py>")
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        source_lines = f.readlines()
    result = convert_typed_dict_to_pydantic_regex(source_lines)
    print(''.join(result))

if __name__ == "__main__":
    main()
