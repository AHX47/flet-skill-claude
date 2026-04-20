# scripts/utils.py
import os
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a shell command and return (stdout, stderr, returncode)."""
    proc = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
    return proc.stdout.strip(), proc.stderr.strip(), proc.returncode

def ensure_package(package):
    """Install a pip package if missing."""
    try:
        __import__(package.replace("-", "_"))
    except ImportError:
        print(f"Installing missing package: {package}")
        run_command(f"{sys.executable} -m pip install {package}")

def create_file(path, content):
    """Write content to a file, creating parent directories."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"Created: {path}")
