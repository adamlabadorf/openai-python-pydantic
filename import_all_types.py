import importlib
import pkgutil
import openai_pydantic.types

def import_all_submodules(package):
    """Import all submodules under the given package."""
    for loader, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package.__name__ + "."):
        print(f"Importing {module_name}")
        importlib.import_module(module_name)

if __name__ == "__main__":
    import_all_submodules(openai_pydantic.types)
