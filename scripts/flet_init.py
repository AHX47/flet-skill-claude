# scripts/flet_init.py
#!/usr/bin/env python3
"""Initialize a new Flet 0.84.0 project with best practices."""
import argparse
from pathlib import Path
from .utils import run_command, create_file

TEMPLATE_MAIN = '''import flet as ft

def main(page: ft.Page):
    page.title = "My Flet App"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # Use new 0.84 API (colors, icons via ft.Colors / ft.Icons)
    page.add(
        ft.Text("Hello from Flet 0.84!", size=30, weight=ft.FontWeight.BOLD),
        ft.ElevatedButton(
            "Click me",
            icon=ft.Icons.THUMB_UP,
            on_click=lambda e: page.add(ft.Text("Button clicked!", color=ft.Colors.GREEN))
        )
    )

ft.app(target=main)
'''

TEMPLATE_REQUIREMENTS = "flet>=0.84.0\n"

def init_project(project_name: str, path: str = "."):
    target = Path(path) / project_name
    if target.exists():
        print(f"Error: {target} already exists.")
        return False

    print(f"Creating Flet project: {project_name}")
    target.mkdir(parents=True)

    # Create virtual environment
    run_command(f"python -m venv {target / 'venv'}")
    print("Virtual environment created.")

    # Write files
    create_file(target / "main.py", TEMPLATE_MAIN)
    create_file(target / "requirements.txt", TEMPLATE_REQUIREMENTS)

    # Install flet inside venv
    pip = target / "venv" / "bin" / "pip"
    run_command(f"{pip} install -r {target / 'requirements.txt'}")
    print("Flet installed.")

    print(f"\n✅ Project ready! cd {target} and run:")
    print(f"   source venv/bin/activate  (or venv\\Scripts\\activate on Windows)")
    print("   flet run main.py")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new Flet project")
    parser.add_argument("name", help="Project name")
    parser.add_argument("--path", default=".", help="Parent directory (default: current)")
    args = parser.parse_args()
    init_project(args.name, args.path)
