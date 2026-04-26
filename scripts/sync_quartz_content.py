#!/usr/bin/env python3
"""Copy the Obsidian vault content into Quartz's content directory."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

PUBLISH_DIRS = [
    "00 MOCs",
    "01 Literature Review",
    "02 Concepts",
    "03 Papers",
    "04 Experiments",
    "05 Methods",
    "06 Data",
]

PUBLISH_ROOT_FILES = [
    "START HERE.md",
    "Containerless Processing.md",
    "Rayleigh and Grashof Numbers in Solidification.md",
]

IGNORE_NAMES = {
    ".DS_Store",
}

IGNORE_SUFFIXES = {
    ".docx",
    ".xlsx",
}


def should_copy(path: Path) -> bool:
    if path.name in IGNORE_NAMES:
        return False
    if path.suffix.lower() in IGNORE_SUFFIXES:
        return False
    return True


def copy_tree(src: Path, dest: Path) -> None:
    if not src.exists():
        return
    for path in src.rglob("*"):
        if path.is_dir() or not should_copy(path):
            continue
        rel = path.relative_to(src)
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def write_index() -> None:
    index = CONTENT / "index.md"
    index.write_text(
        """---
title: Metal Alloy Processing for In-Space Manufacturing
tags:
  - phd
  - microgravity
  - in-space-manufacturing
---

# Metal Alloy Processing for In-Space Manufacturing

This Quartz site publishes the PhD wiki for **Metal Alloy Processing for In-Space Manufacturing: Investigating Solidification Behaviour Under Microgravity**.

## Start Here

- [[00 MOCs/Metal Alloy Processing for In-Space Manufacturing MOC|Main MOC]]
- [[00 MOCs/Interactive PhD Dashboard|Interactive dashboard note]]
- [Interactive visual dashboard](00-MOCs/Interactive-PhD-Dashboard.html)
- [[01 Literature Review/Earth 1g vs Microgravity Solidification Processing|1g vs Microgravity Review]]
- [[05 Methods/Literature Review Workflow|Literature Review Workflow]]

## Core Themes

- [[02 Concepts/Why Gravity Matters in Alloy Solidification]]
- [[02 Concepts/Microgravity as a Diffusion-Controlled Benchmark]]
- [[02 Concepts/Containerless Electromagnetic Levitation]]
- [[02 Concepts/Columnar-to-Equiaxed Transition]]
- [[02 Concepts/Implications for In-Space Additive Manufacturing]]
""",
        encoding="utf-8",
    )


def main() -> int:
    if CONTENT.exists():
        shutil.rmtree(CONTENT)
    CONTENT.mkdir(parents=True)

    for dirname in PUBLISH_DIRS:
        copy_tree(ROOT / dirname, CONTENT / dirname)

    for filename in PUBLISH_ROOT_FILES:
        src = ROOT / filename
        if src.exists() and should_copy(src):
            shutil.copy2(src, CONTENT / filename)

    write_index()
    print(f"Synced Quartz content into {CONTENT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
