# scripts/extension_scaffold.py
#!/usr/bin/env python3
"""Generate a new Flet extension (Python + Dart stubs)."""
import argparse
from pathlib import Path
from .utils import create_file

PYTHON_TEMPLATE = '''# {ext_name}.py
import flet as ft
from flet.core.control import Control

class {class_name}(Control):
    """A custom Flet control."""
    def __init__(
        self,
        label: str = "Default",
        on_click=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.label = label
        self.on_click = on_click

    def _get_control_name(self):
        return "{control_id}"

    @property
    def label(self):
        return self._get_attr("label")

    @label.setter
    def label(self, value):
        self._set_attr("label", value)

    def _add_event_handler(self, event_name, handler):
        if event_name == "click":
            self.on_click = handler
        super()._add_event_handler(event_name, handler)
'''

DART_TEMPLATE = '''// {control_id}_control.dart
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class {class_name}Control extends StatelessWidget {{
  final Control? parent;
  final Control control;

  const {class_name}Control({{
    super.key,
    this.parent,
    required this.control,
  }});

  @override
  Widget build(BuildContext context) {{
    String label = control.attrString("label", "Default")!;
    return ElevatedButton(
      onPressed: () {{
        control.addEvent("click", {{}});
      }},
      child: Text(label),
    );
  }}
}}

// Register this control in your main.dart:
//
// void registerCustomControls() {{
//   FletControlBackend.registerControl(
//     "{control_id}",
//     (parent, control) => {class_name}Control(parent: parent, control: control),
//   );
// }}
'''

def scaffold_extension(ext_name: str, output_dir: str = "."):
    """Create Python and Dart files for a new extension."""
    class_name = ''.join(word.capitalize() for word in ext_name.split('_'))
    control_id = ext_name.lower()
    out = Path(output_dir)

    python_file = out / f"{ext_name}.py"
    create_file(python_file, PYTHON_TEMPLATE.format(
        ext_name=ext_name, class_name=class_name, control_id=control_id
    ))

    dart_dir = out / "src"
    dart_file = dart_dir / f"{control_id}_control.dart"
    create_file(dart_file, DART_TEMPLATE.format(
        class_name=class_name, control_id=control_id
    ))

    print("\n📦 Next steps:")
    print(f"1. Edit {python_file} to add more properties/events.")
    print(f"2. Implement your Flutter widget in {dart_file}.")
    print("3. For testing, place Dart files in ./src/ and run `flet run --path .`")
    print("4. To distribute, follow the packaging guide in your skill.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new Flet extension")
    parser.add_argument("name", help="Extension name (snake_case, e.g. my_button)")
    parser.add_argument("--output", "-o", default=".", help="Output directory")
    args = parser.parse_args()
    scaffold_extension(args.name, args.output)
