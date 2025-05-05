import re
import sys
from typing import List

def convert_typed_dict_to_pydantic_regex(source_lines: List[str]) -> List[str]:

    out = []
    for line in source_lines:

        # base classes
        if m := re.match(r'(\s*)class (\w+)\(([^)]*TypedDict[^)]*)\):', line):
            new_line = re.sub(r'TypedDict, total=False', 'BaseModel', line)
            out.append(new_line)

        elif re.match(r'^from typing_extensions.*(Required|TypedDict)', line):
            new_line = re.sub(r',?\s*Required,?', '', line)
            new_line = re.sub(r',?\s*TypedDict,?', '', new_line)
            out.append(new_line)
            # add the pydantic import right after
            out.append('from pydantic import BaseModel')

        # there are some typing_extensions.TypeAlias definitions we need to remove
        elif re.match(r'^[a-zA-Z_]\w+:\s*TypeAlias', line):
            new_line = re.sub(r':\s*TypeAlias', '', line)
            out.append(new_line.strip()+ f' # old {line}')

        # search for fields in the format (\w*)<valid python identifier>:(\w*)<valid python type hint>
        elif m := re.match(r'(\s*)([a-zA-Z_]\w*):\s*(.*)(\s*=\s*\w+)?$', line):
            indent = m.group(1)
            var_name = m.group(2)
            var_type = m.group(3)
            var_default = m.group(4)
            if 'Required' in var_type:
                # Required[<nested type>]
                var_type = re.sub(r'Required\[(.*?)\]', r'\1', var_type)
            elif not var_type.startswith('Optional['):
                var_type = f'Optional[{var_type}]'
            
            var_type = re.sub(r'Iterable', r'List', var_type)

            if not var_default or not var_default.strip():
                var_default = "= None"
            out.append(f'{indent}{var_name}: {var_type} {var_default} # old {line}')
        
        else:
            out.append(line)
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
