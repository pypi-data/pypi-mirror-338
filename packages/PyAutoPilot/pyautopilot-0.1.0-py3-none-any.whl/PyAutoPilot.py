import importlib
import subprocess
import sys
import pkgutil
import ast

def install_package(package):
    """Installs a missing package using pip."""
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {package}: {e}")

def check_and_install():
    """Scans the current script for imports and installs missing packages."""
    try:
        with open(sys.argv[0], "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=sys.argv[0])
        print(ast.dump(tree, indent=4))
        required_modules = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                required_modules.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                required_modules.add(node.module)
        
        installed_modules = {pkg.name for pkg in pkgutil.iter_modules()}
        
        module_package_map = {
            "win32com.client": "pywin32"
        }
        
        for module in required_modules:
            package_name = module_package_map.get(module, module)
            if module and package_name not in installed_modules:
                print(f"Installing missing package: {package_name}")
                install_package(package_name)
    except Exception as e:
        print(f"Error checking/installing packages: {e}")

check_and_install()