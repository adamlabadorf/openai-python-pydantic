import subprocess
import sys
import os

TYPEDDICT_LIST = "TypedDict_classes.txt"
CONVERTER = "typed_dict_to_pydantic_regex.py"

SUCCESS_LOG = []
FAIL_LOG = []

def get_class_names(pyfile):
    # Parse the file to get all class names (for import test)
    import ast
    with open(pyfile, 'r') as f:
        tree = ast.parse(f.read(), filename=pyfile)
    return [node.name for node in tree.body if isinstance(node, ast.ClassDef)]

def main():
    with open(TYPEDDICT_LIST, 'r') as f:
        lines = f.readlines()
    for line in lines:
        if not line.strip():
            continue
        path = line.split(':')[0].strip()
        abs_path = os.path.abspath(path)
        print(f"Converting {abs_path} ...")
        # Generate Pydantic code
        try:
            result = subprocess.run([sys.executable, CONVERTER, abs_path], capture_output=True, text=True, check=True)
            pydantic_code = result.stdout
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Conversion failed for {path}: {e.stderr}")
            FAIL_LOG.append((path, 'conversion_error', e.stderr))
            sys.exit(1)  # Halt on error
        # Backup original
        backup_path = abs_path + ".bak"
        os.rename(abs_path, backup_path)
        with open(abs_path, 'w') as f:
            f.write(pydantic_code)
        # Try importing all classes
        dir_path = os.path.dirname(abs_path)
        module_name = os.path.splitext(os.path.basename(abs_path))[0]
        sys.path.insert(0, dir_path)
        try:
            class_names = get_class_names(abs_path)
            import_line = f"from {module_name} import " + ", ".join(class_names)
            code = compile(import_line, '<string>', 'exec')
            exec(code, {})
            SUCCESS_LOG.append(path)
            print(f"[OK] {path}")
        except Exception as e:
            print(f"[ERROR] Import failed for {path}: {e}")
            FAIL_LOG.append((path, 'import_error', str(e)))
            # Revert file
            os.remove(abs_path)
            os.rename(backup_path, abs_path)
            sys.exit(1)  # Halt on error
        finally:
            sys.path.pop(0)
        # Clean up backup if successful
        if os.path.exists(backup_path) and path in SUCCESS_LOG:
            os.remove(backup_path)
    # Summary
    print("\n--- Conversion Summary ---")
    print(f"Success: {len(SUCCESS_LOG)} files")
    print(f"Failed: {len(FAIL_LOG)} files")
    for fail in FAIL_LOG:
        print(f"  {fail[0]}: {fail[1]} - {fail[2]}")

if __name__ == "__main__":
    main()
