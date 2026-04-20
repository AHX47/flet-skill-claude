# flet-skill-claude
flet skill for claude code  design and proramming last version 0.84.0
---
name: flet
description: "any programming flet using claude code "
---

```markdown
# Flet Programming Skills: Extensions & Custom Development

This document provides a comprehensive overview of Flet extensions (official and community) and a guide to building custom Flet extensions using Dart and Python.

## Table of Contents
- [Official Built-in Extensions](#official-built-in-extensions)
- [Community Extensions & Resources](#community-extensions--resources)
- [Important Updates for Flet 0.26.0+](#important-updates-for-flet-0260)
- [Building Custom Flet Extensions](#building-custom-flet-extensions)
  - [Prerequisites](#prerequisites)
  - [Python Side: Creating a Control](#python-side-creating-a-control)
  - [Dart Side: Implementing the Widget](#dart-side-implementing-the-widget)
  - [Registration & Integration](#registration--integration)
  - [Packaging as a `.whl`](#packaging-as-a-whl)
  - [Complete Example: Custom Button](#complete-example-custom-button)
- [Tips & Best Practices](#tips--best-practices)

---

## Official Built-in Extensions

Flet provides several official extensions that integrate powerful Flutter libraries. Install them via `pip install flet-<name>`.

| Extension | Description |
|-----------|-------------|
| `flet-audio` | Play audio files and control streaming. |
| `flet-audio-recorder` | Record audio from microphone, save in various formats. |
| `flet-video` | Advanced video player with playlists, hardware acceleration, and subtitles. |
| `flet-map` | Interactive maps with layers and markers. |
| `flet-geolocator` | Access GPS location services and get coordinates. |
| `flet-camera` | Live camera preview, capture images, and record video. |
| `flet-webview` | Embed web content (supports macOS/web in addition to mobile). |
| `flet-charts` | Create advanced interactive charts and plots. |
| `flet-ads` | Display Google Ads (Banner & Interstitial) in mobile apps. |
| `flet-permission-handler` | Easily manage device permissions (location, camera, microphone). |
| `flet-lottie` | Play high‑quality Lottie animations. |
| `flet-rive` | Play interactive Rive animations. |
| `flet-flashlight` | Control device flashlight (torch). |
| `flet-secure-storage` | Securely store encrypted sensitive data on device. |
| `flet-datatable2` | Enhanced data table with sticky headers and columns. |

> **Note**: Always check the official [Flet docs](https://flet.dev/docs/extensions) for the latest extensions and version compatibility.

---

## Community Extensions & Resources

The Flet community actively develops additional components and libraries.

### `flet-contrib`
A community repository of pure‑Python controls. Install with:
```bash
pip install flet-contrib
```
Includes:
- `ColorPicker` – multiple picker styles (Material, Block, Hue Ring)
- Custom widgets built from core Flet controls.

### Third‑Party Libraries
| Library | Purpose |
|---------|---------|
| `flet-alchemy` | Seamless SQLAlchemy integration with Flet apps. |
| `flet-route` | Advanced routing / navigation (more structured than built‑in). |
| `flet-fastapi` | Run Flet apps inside FastAPI for robust web deployment. |

### Awesome Flet
The [Awesome Flet](https://github.com/flet-dev/awesome-flet) repository is a curated list of:
- Templates & starter kits
- Utility libraries
- Open‑source Flet projects (great for code reuse)

### Finding More Extensions
Search GitHub for topics `flet-extension` or `flet-control`. Many community extensions provide:
- System notifications
- Bluetooth (`flutter_blue` wrappers)
- QR / barcode scanners

> **Caution**: Community extensions may not always be up‑to‑date. Verify compatibility with your Flet version (especially after the extensions system change in v0.26.0).

---

## Important Updates for Flet 0.26.0+

Recent Flet versions introduced changes to how constants and classes are accessed. Use the following mappings to update your code:

```python
import flet as ft

# Icons
ft.icons = ft.Icons

# Colors
ft.colors = ft.Colors

# Alignment – use ft.alignment.Alignment
ft.alignment.center = ft.alignment.Alignment.CENTER
ft.alignment.top_left = ft.alignment.Alignment.TOP_LEFT
ft.alignment.top_center = ft.alignment.Alignment.TOP_CENTER
ft.alignment.top_right = ft.alignment.Alignment.TOP_RIGHT
ft.alignment.center_left = ft.alignment.Alignment.CENTER_LEFT
ft.alignment.center_right = ft.alignment.Alignment.CENTER_RIGHT
ft.alignment.bottom_left = ft.alignment.Alignment.BOTTOM_LEFT
ft.alignment.bottom_center = ft.alignment.Alignment.BOTTOM_CENTER
ft.alignment.bottom_right = ft.alignment.Alignment.BOTTOM_RIGHT

# Animation
ft.animation.Animation = ft.Animation

# BoxFit (was ImageFit)
ft.ImageFit = ft.BoxFit
### and more add comming soon {Tab , FilePicker , build-in-extention liberaries}
```

Always consult the [official migration guide](https://flet.dev/docs/migration) for breaking changes.

---

## Building Custom Flet Extensions

You can create your own Flet extension that bridges a Flutter library (from [pub.dev](https://pub.dev)) with Python. This involves writing Dart code for rendering and Python code for the control API.

### Prerequisites
- Flutter SDK installed
- Python 3.8+ with Flet (`pip install flet`)
- Basic knowledge of Dart and Flutter widgets

### Python Side: Creating a Control

Create a Python class that inherits from `ft.Control`. Define properties and the control name.

```python
# my_custom_widget.py
import flet as ft
from flet.core.control import Control

class MyCustomWidget(Control):
    def __init__(self, text="Hello", **kwargs):
        super().__init__(**kwargs)
        self.text = text

    def _get_control_name(self):
        return "my_custom_widget"  # Must match Dart registration

    @property
    def text(self):
        return self._get_attr("text")

    @text.setter
    def text(self, value):
        self._set_attr("text", value)
```

### Dart Side: Implementing the Widget

Inside a Flutter project (or inside your extension’s `src` directory), create a Dart file that defines the widget and registers it with Flet’s control backend.

```dart
// my_custom_widget_control.dart
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class MyCustomWidgetControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const MyCustomWidgetControl({
    super.key,
    this.parent,
    required this.control,
  });

  @override
  Widget build(BuildContext context) {
    String text = control.attrString("text", "Default")!;
    return Text(
      text,
      style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
    );
  }
}

// Registration – add this to your main.dart or extension initialization
void registerControls() {
  FletControlBackend.registerControl(
    "my_custom_widget",
    (parent, control) => MyCustomWidgetControl(parent: parent, control: control),
  );
}
```

### Registration & Integration

To make the Dart code available, you have two options:

1. **Custom Flet build** – Place the Dart files in your project’s `src/` directory. Flet will automatically include them when you run `flet build`.
2. **Standalone extension** – Distribute the Python package and instruct users to include the Dart code in their own custom build (advanced).

For development, use:
```bash
flet run --path .   # assuming your Dart code is in ./src/
```

### Packaging as a `.whl`

To distribute your extension via PyPI, create a standard Python package with a `pyproject.toml`:

```toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "flet-my-custom"
version = "0.1.0"
dependencies = ["flet>=0.26.0"]
```

Then build:
```bash
pip install build
python -m build
```

The `.whl` file will be created in `dist/`. Users can install it with `pip install flet-my-custom`.

### Complete Example: Custom Button

Here’s a full example of a custom button that changes color on click.

**Python side (`custom_button.py`):**
```python
import flet as ft
from flet.core.control import Control

class CustomButton(Control):
    def __init__(self, label="Click me", on_click=None, **kwargs):
        super().__init__(**kwargs)
        self.label = label
        self.on_click = on_click

    def _get_control_name(self):
        return "custom_button"

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
```

**Dart side (`custom_button_control.dart`):**
```dart
import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class CustomButtonControl extends StatelessWidget {
  final Control? parent;
  final Control control;

  const CustomButtonControl({super.key, this.parent, required this.control});

  @override
  Widget build(BuildContext context) {
    String label = control.attrString("label", "Click me")!;
    return ElevatedButton(
      onPressed: () {
        control.addEvent("click", {});
      },
      child: Text(label),
    );
  }
}

// Registration
void registerControls() {
  FletControlBackend.registerControl(
    "custom_button",
    (parent, control) => CustomButtonControl(parent: parent, control: control),
  );
}
```

**Usage in Python:**
```python
import flet as ft
from custom_button import CustomButton

def main(page: ft.Page):
    btn = CustomButton(label="Press me", on_click=lambda e: print("Clicked!"))
    page.add(btn)

ft.app(target=main)
```

---

## Tips & Best Practices

1. **Always check compatibility** – Test your extension with the latest Flet version, especially after major releases.
2. **Use `flet build` for testing** – It automatically compiles Dart code placed in `./src/`.
3. **Leverage existing Flutter libraries** – Search [pub.dev](https://pub.dev) for widgets you want to wrap.
4. **Keep the Python API simple** – Mimic the style of built‑in Flet controls.
5. **Document your extension** – Provide clear examples and mention required Flutter setup if any.
6. **For advanced 3D or markdown** – Wrap Flutter packages like `flutter_3d` or `flutter_markdown` following the same pattern.

---

## References

- [Flet Official Documentation](https://docs.flet.dev)
- [Flet GitHub Repository](https://github.com/flet-dev/flet)
- [Awesome Flet List](https://github.com/flet-dev/awesome-flet)
- [Pub.dev – Flutter Packages](https://pub.dev)

Happy extending!
[***]abdo_hak47[***]
```
