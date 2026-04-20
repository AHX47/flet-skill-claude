# scripts/extension_builder.py
#!/usr/bin/env python3
"""Build a Python wheel (.whl) for a Flet extension."""
import argparse
import subprocess
import shutil
from pathlib import Path
from .utils import run_command, create_file

PYPROJECT_TOML_TEMPLATE = '''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{package_name}"
version = "{version}"
dependencies = ["flet>=0.84.0"]
description = "A custom Flet extension"
authors = [{{name = "Your Name", email = "you@example.com"}}]
license = {{text = "MIT"}}
readme = "README.md"
requires-python = ">=3.8"

[tool.setuptools.packages.find]
where = ["."]
include = ["{module_name}*"]
'''

SETUP_PY_TEMPLATE = '''# Setup for {package_name}
from setuptools import setup, find_packages

setup(
    name="{package_name}",
    version="{version}",
    packages=find_packages(include=["{module_name}", "{module_name}.*"]),
    install_requires=["flet>=0.84.0"],
)
'''

def build_extension(extension_dir: str, version: str = "0.1.0"):
    ext_dir = Path(extension_dir).resolve()
    if not ext_dir.exists():
        print(f"Error: {ext_dir} does not exist.")
        return False

    # Assume the Python module has the same name as the directory?
    module_name = ext_dir.name.replace("-", "_")
    package_name = f"flet-{module_name}" if not module_name.startswith("flet-") else module_name

    # Create minimal pyproject.toml if missing
    pyproject = ext_dir / "pyproject.toml"
    if not pyproject.exists():
        create_file(pyproject, PYPROJECT_TOML_TEMPLATE.format(
            package_name=package_name, version=version, module_name=module_name
        ))

    # Also create a dummy __init__.py if needed
    init_file = ext_dir / f"{module_name}.py"
    if not init_file.exists():
        print(f"Warning: No {module_name}.py found. Creating stub.")
        create_file(init_file, f'# {package_name} - custom Flet extension\n')

    # Build the wheel
    print(f"Building wheel for {package_name}...")
    stdout, stderr, rc = run_command(f"python -m build --wheel", cwd=ext_dir)
    if rc != 0:
        print(f"Build failed:\n{stderr}")
        return False

    dist_dir = ext_dir / "dist"
    wheels = list(dist_dir.glob("*.whl"))
    if wheels:
        print(f"✅ Wheel created: {wheels[0]}")
        print(f"Install with: pip install {wheels[0]}")
    else:
        print("No .whl file produced.")
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build a Flet extension wheel")
    parser.add_argument("extension_dir", help="Directory containing the extension Python module")
    parser.add_argument("--version", default="0.1.0", help="Version for the package")
    args = parser.parse_args()
    build_extension(args.extension_dir, args.version)
