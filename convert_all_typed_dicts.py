import subprocess
import sys
import os
import argparse

TYPEDDICT_LIST = "TypedDict_classes.txt"
CONVERTER = "typed_dict_to_pydantic_regex.py"

SUCCESS_LOG = []
FAIL_LOG = []


def main(dryrun: bool = False):
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
        if dryrun:
            print(f"[DRYRUN] Would backup {abs_path} to {abs_path + '.bak'} and overwrite with converted code.")
        else:
            # Backup original
            backup_path = abs_path + ".bak"
            os.rename(abs_path, backup_path)
            with open(abs_path, 'w') as f:
                f.write(pydantic_code)
        # Check for valid Python syntax using py_compile
        import py_compile
        try:
            if dryrun:
                import tempfile
                with tempfile.NamedTemporaryFile('w', suffix='.py', delete=False) as tmpf:
                    tmpf.write(pydantic_code)
                    tmp_path = tmpf.name
                py_compile.compile(tmp_path, doraise=True)
                os.remove(tmp_path)
                SUCCESS_LOG.append(path)
                print(f"[OK] {path} (dryrun)")
            else:
                py_compile.compile(abs_path, doraise=True)
                SUCCESS_LOG.append(path)
                print(f"[OK] {path}")
        except py_compile.PyCompileError as e:
            print(f"[ERROR] Syntax check failed for {path}: {e}")
            FAIL_LOG.append((path, 'syntax_error', str(e)))
            if not dryrun:
                # Revert file
                os.remove(abs_path)
                os.rename(backup_path, abs_path)
            sys.exit(1)  # Halt on error
        # Clean up backup if successful
        if not dryrun and os.path.exists(abs_path + '.bak') and path in SUCCESS_LOG:
            os.remove(abs_path + '.bak')
    # Summary
    print("\n--- Conversion Summary ---")
    print(f"Success: {len(SUCCESS_LOG)} files")
    print(f"Failed: {len(FAIL_LOG)} files")
    for fail in FAIL_LOG:
        print(f"  {fail[0]}: {fail[1]} - {fail[2]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert TypedDicts to Pydantic models.")
    parser.add_argument('--dryrun', action='store_true', help='Do everything except overwrite the original file')
    args = parser.parse_args()
    main(dryrun=args.dryrun)
