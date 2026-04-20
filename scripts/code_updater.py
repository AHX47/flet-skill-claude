# scripts/code_updater.py
#!/usr/bin/env python3
"""Convert old Flet code (<0.26) to 0.84+ syntax."""
import re
import argparse
from pathlib import Path

# Mapping rules: (old_pattern, new_pattern, flags)
RULES = [
    # Icons
    (r'ft\.icons\.([A-Z_]+)', r'ft.Icons.\1', 0),
    # Colors
    (r'ft\.colors\.([A-Z_]+)', r'ft.Colors.\1', 0),
    # Alignment
    (r'ft\.alignment\.center\b', r'ft.alignment.Alignment.CENTER', 0),
    (r'ft\.alignment\.top_left\b', r'ft.alignment.Alignment.TOP_LEFT', 0),
    (r'ft\.alignment\.top_center\b', r'ft.alignment.Alignment.TOP_CENTER', 0),
    (r'ft\.alignment\.top_right\b', r'ft.alignment.Alignment.TOP_RIGHT', 0),
    (r'ft\.alignment\.center_left\b', r'ft.alignment.Alignment.CENTER_LEFT', 0),
    (r'ft\.alignment\.center_right\b', r'ft.alignment.Alignment.CENTER_RIGHT', 0),
    (r'ft\.alignment\.bottom_left\b', r'ft.alignment.Alignment.BOTTOM_LEFT', 0),
    (r'ft\.alignment\.bottom_center\b', r'ft.alignment.Alignment.BOTTOM_CENTER', 0),
    (r'ft\.alignment\.bottom_right\b', r'ft.alignment.Alignment.BOTTOM_RIGHT', 0),
    # Animation
    (r'ft\.animation\.Animation', r'ft.Animation', 0),
    # ImageFit -> BoxFit
    (r'ft\.ImageFit\.([A-Z_]+)', r'ft.BoxFit.\1', 0),
]

def update_file(file_path, dry_run=False):
    path = Path(file_path)
    original = path.read_text(encoding="utf-8")
    new_content = original
    for pattern, repl, flags in RULES:
        new_content = re.sub(pattern, repl, new_content, flags=flags)

    if new_content == original:
        print(f"✓ No changes needed: {file_path}")
        return False

    if dry_run:
        print(f"🔍 Would update: {file_path}")
        return True

    path.write_text(new_content, encoding="utf-8")
    print(f"✅ Updated: {file_path}")
    return True

def update_directory(dir_path, dry_run=False):
    dir_path = Path(dir_path)
    count = 0
    for py_file in dir_path.rglob("*.py"):
        if update_file(py_file, dry_run):
            count += 1
    print(f"\n{'Would update' if dry_run else 'Updated'} {count} files.")
    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate old Flet code to 0.84 API")
    parser.add_argument("target", help="File or directory to convert")
    parser.add_argument("--dry-run", action="store_true", help="Only show what would change")
    args = parser.parse_args()

    target = Path(args.target)
    if target.is_file():
        update_file(target, args.dry_run)
    elif target.is_dir():
        update_directory(target, args.dry_run)
    else:
        print(f"Error: {target} not found.")
