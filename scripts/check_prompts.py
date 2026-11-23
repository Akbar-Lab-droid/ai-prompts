#!/usr/bin/env python3
"""Validate prompts.json.

Checks that the file is valid JSON, that every prompt has a non-empty
id/title/category/prompt, that ids are unique, that categories are from
the known set, and prints the prompt count per category.

Usage:
    python3 scripts/check_prompts.py [path/to/prompts.json]
"""

import json
import sys
from collections import Counter
from pathlib import Path

KNOWN_CATEGORIES = {
    "coding",
    "writing",
    "learning",
    "analysis",
    "business",
    "image",
    "data",
    "productivity",
    "career",
    "everyday",
}

REQUIRED_FIELDS = ("id", "title", "category", "purpose", "prompt", "tips", "example")


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "prompts.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"FAIL: file not found: {path}")
        return 1
    except json.JSONDecodeError as exc:
        print(f"FAIL: invalid JSON in {path}: {exc}")
        return 1

    prompts = data.get("prompts")
    if not isinstance(prompts, list) or not prompts:
        print("FAIL: top-level 'prompts' must be a non-empty list")
        return 1

    errors = []
    seen_ids = set()
    for index, entry in enumerate(prompts):
        where = f"prompts[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{where}: not an object")
            continue
        for field in REQUIRED_FIELDS:
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{where}: field '{field}' is missing or empty")
        entry_id = entry.get("id", "")
        if entry_id in seen_ids:
            errors.append(f"{where}: duplicate id '{entry_id}'")
        seen_ids.add(entry_id)
        category = entry.get("category", "")
        if category and category not in KNOWN_CATEGORIES:
            errors.append(f"{where}: unknown category '{category}'")

    counts = Counter(entry.get("category", "?") for entry in prompts if isinstance(entry, dict))

    print(f"Total prompts: {len(prompts)}")
    for category in sorted(KNOWN_CATEGORIES):
        print(f"  {category}: {counts.get(category, 0)}")
    unknown = sorted(set(counts) - KNOWN_CATEGORIES)
    if unknown:
        print(f"  unknown categories: {unknown}")

    if errors:
        print(f"\nFAIL: {len(errors)} problem(s):")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("\nOK: all prompts valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
