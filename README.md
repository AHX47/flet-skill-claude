This skill is maintained for Flet 0.84.0. Always refer to the official migration guide for breaking changes.
text


---

## `README.md`

```markdown
# flet-skill-claude

**Claude Code skill for Flet 0.84.0** – build web, mobile, and desktop apps with Python + Flutter.

This skill provides:
- Expert knowledge of Flet 0.84.0 (API, extensions, custom controls)
- Ready‑to‑use automation scripts for project scaffolding, extension creation, legacy code migration, and packaging

## 🚀 Quick Start

### 1. Install the skill for Claude Code

Clone this repository and place it in your Claude Code skills directory:

```bash
git clone https://github.com/AHX47/flet-skill-claude.git
# Then move/copy to ~/.claude/skills/ (or your Claude Code skills folder)

2. Use the skill

Ask Claude Code anything about Flet, for example:

    “Create a new Flet project called chat_app”

    “Build a custom video player extension for Flet”

    “Migrate my old Flet 0.22 app to 0.84”

    “How do I use the flet-map extension?”

Claude will automatically use the scripts and best practices defined in skill.md.
3. Manual script usage (optional)

The automation scripts are located in scripts/. You can run them directly:
Script	Command
New project	python scripts/flet_init.py my_project
Extension scaffold	python scripts/extension_scaffold.py fancy_button
Legacy code upgrade	python scripts/code_updater.py old_app/ --dry-run
Build extension wheel	python scripts/extension_builder.py my_extension/
📦 Included Scripts
flet_init.py

Creates a modern Flet 0.84.0 project:

    Virtual environment

    requirements.txt with flet>=0.84.0

    Sample main.py using new API (ft.Colors, ft.Icons, etc.)

extension_scaffold.py

Generates Python and Dart stubs for a custom Flet control. Use this to wrap any Flutter widget from pub.dev.
code_updater.py

Automatically rewrites old Flet code (<0.26) to the 0.84+ API:

    ft.icons → ft.Icons

    ft.colors → ft.Colors

    ft.alignment.* → ft.alignment.Alignment.*

    ft.ImageFit → ft.BoxFit

    etc.

extension_builder.py

Builds a distributable Python wheel (.whl) from your extension directory. Requires build (pip install build).
🧠 Skill Content

The skill.md file contains:

    Complete Flet 0.84.0 API reference

    Official and community extensions

    Step‑by‑step guide to building custom extensions (Python + Dart)

    Integration instructions for the scripts

    Best practices and troubleshooting

📄 License

MIT – feel free to use and adapt.
🤝 Contributing

Issues and pull requests welcome. Please keep compatibility with Flet 0.84.0.
🌟 Acknowledgements

Built for the Flet community. Thanks to the Flet team and contributors.

Maintainer: abdo_hak47
text


