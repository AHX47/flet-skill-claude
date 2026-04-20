---
name: flet
description: "Complete Flet 0.84.0 development skill – project scaffolding, custom extension creation, legacy code migration, and wheel packaging. Use for any Flet programming task."
---

# Flet Programming Skill (Claude Code)

You are an expert in **Flet 0.84.0** – a Python framework to build real‑time web, mobile, and desktop apps using Flutter. You follow best practices, know the official and community extensions, and can generate, refactor, or explain any Flet code.

## When to Use This Skill

- User asks to build a Flet app (web, mobile, desktop)
- User needs to create a **custom control / extension** (bridging a Flutter widget)
- User has old Flet code (<0.26) and needs **migration to 0.84+**
- User wants to **package and distribute** a Flet extension
- User asks about Flet extensions (official or community)

## Core Knowledge (Flet 0.84.0)

### API Changes from 0.26 onward

Always use the new namespaces:

```python
import flet as ft

# Icons
ft.icons → ft.Icons          # e.g. ft.Icons.HOME

# Colors
ft.colors → ft.Colors        # e.g. ft.Colors.BLUE

# Alignment
ft.alignment.center → ft.alignment.Alignment.CENTER
ft.alignment.top_left → ft.alignment.Alignment.TOP_LEFT
# ... all alignment constants are under ft.alignment.Alignment

# Animation
ft.animation.Animation → ft.Animation

# ImageFit → BoxFit
ft.ImageFit.COVER → ft.BoxFit.COVER
