#!/usr/bin/env python3
"""Generate the per-category Markdown files from prompts.json.

prompts.json is the single source of truth. This script:
  1. Reads prompts.json from the repo root.
  2. Writes one Markdown file per category into prompts/<category>.md.
  3. Copies prompts.json into docs/prompts.json so the GitHub Pages
     site (which only serves the docs/ folder) can fetch the data.

Usage:
    python3 scripts/build_docs.py
"""

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS_JSON = ROOT / "prompts.json"
PROMPTS_DIR = ROOT / "prompts"
DOCS_DIR = ROOT / "docs"

CATEGORY_TITLES = {
    "coding": "Coding",
    "writing": "Writing",
    "learning": "Learning & Study",
    "analysis": "Analysis & Research",
    "business": "Business & Marketing",
    "image": "Image Generation",
    "data": "Data & Spreadsheets",
    "productivity": "Productivity",
    "career": "Job & Career",
    "everyday": "Everyday Life",
}


def render_category(category: str, entries: list[dict]) -> str:
    title = CATEGORY_TITLES.get(category, category.title())
    lines = [
        f"# {title}",
        "",
        f"{len(entries)} prompts. See [PROMPTING-GUIDE.md](../PROMPTING-GUIDE.md) for how to write your own.",
        "",
    ]
    for entry in entries:
        lines.append(f"## {entry['title']}")
        lines.append("")
        lines.append(f"**Purpose:** {entry['purpose']}")
        lines.append("")
        lines.append("```")
        lines.append(entry["prompt"])
        lines.append("```")
        lines.append("")
        lines.append(f"**Tip:** {entry['tips']}")
        lines.append("")
        lines.append(f"**What to expect:** {entry['example']}")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    data = json.loads(PROMPTS_JSON.read_text(encoding="utf-8"))
    entries = data["prompts"]

    by_category: dict[str, list[dict]] = {}
    for entry in entries:
        by_category.setdefault(entry["category"], []).append(entry)

    PROMPTS_DIR.mkdir(exist_ok=True)
    for old_file in PROMPTS_DIR.glob("*.md"):
        old_file.unlink()

    for category in sorted(by_category):
        output = PROMPTS_DIR / f"{category}.md"
        output.write_text(render_category(category, by_category[category]), encoding="utf-8")
        print(f"Wrote {output.relative_to(ROOT)} ({len(by_category[category])} prompts)")

    # The web app lives in docs/ and GitHub Pages only serves that folder,
    # so the data file has to live there too.
    DOCS_DIR.mkdir(exist_ok=True)
    shutil.copyfile(PROMPTS_JSON, DOCS_DIR / "prompts.json")
    print(f"Copied prompts.json -> {DOCS_DIR.relative_to(ROOT)}/prompts.json")
    print(f"Done: {len(entries)} prompts in {len(by_category)} categories.")


if __name__ == "__main__":
    main()
