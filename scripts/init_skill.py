#!/usr/bin/env python3
"""
Skill Initializer for ai-academic-skills

Creates a new bilingual skill with the project's ua/en structure,
YAML frontmatter per Agent Skills spec, and optional references/.

Usage:
    python3 scripts/init_skill.py <skill-name> --category <category>

Examples:
    python3 scripts/init_skill.py abstract-ua-en --category writing
    python3 scripts/init_skill.py paper-triage --category literature-review
"""

import sys
import re
from pathlib import Path

# ── Constants ────────────────────────────────────────────────────────────────

VALID_CATEGORIES = [
    "citations",
    "writing",
    "literature-review",
    "experiments",
]

AUTHOR = "Dmytro Zarezenko"
LICENSE = "MIT"

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"

# ── Templates ────────────────────────────────────────────────────────────────

SKILL_TEMPLATE_UA = """\
---
name: {skill_name}
description: >-
  [TODO: Опишіть що робить цей скіл і коли його використовувати.
  Включіть конкретні сценарії та ключові слова для тригерів.]
license: {license}
metadata:
  author: {author}
  version: "0.1"
  language: uk
---

# {skill_title}

## Призначення

[TODO: 1–2 речення, що пояснюють призначення скіла.]

Детальний довідник див. у [REFERENCE.md](references/REFERENCE.md).

---

## Інструкції

[TODO: Покрокові інструкції для AI-агента.]

---

## Приклади input → output

[TODO: Додайте приклади вхідних даних та очікуваних результатів.]

---

## Edge cases (граничні випадки)

[TODO: Опишіть граничні випадки та як їх обробляти.]
"""

SKILL_TEMPLATE_EN = """\
---
name: {skill_name}
description: >-
  [TODO: Describe what this skill does and when to use it.
  Include specific scenarios and trigger keywords.]
license: {license}
metadata:
  author: {author}
  version: "0.1"
  language: en
---

# {skill_title}

## Purpose

[TODO: 1–2 sentences explaining what this skill does.]

See [REFERENCE.md](references/REFERENCE.md) for the detailed reference guide.

---

## Instructions

[TODO: Step-by-step instructions for the AI agent.]

---

## Examples input → output

[TODO: Add examples of input data and expected results.]

---

## Edge cases

[TODO: Describe edge cases and how to handle them.]
"""

REFERENCE_TEMPLATE_UA = """\
# {skill_title} — Довідник

[TODO: Детальний технічний довідник для цього скіла.]
"""

REFERENCE_TEMPLATE_EN = """\
# {skill_title} — Reference Guide

[TODO: Detailed technical reference for this skill.]
"""

# ── Validation ───────────────────────────────────────────────────────────────


def validate_skill_name(name: str) -> str | None:
    """Validate skill name per Agent Skills spec. Returns error or None."""
    if not name:
        return "Skill name cannot be empty."
    if len(name) > 64:
        return f"Skill name too long ({len(name)} chars, max 64)."
    if not re.match(r"^[a-z0-9]([a-z0-9-]*[a-z0-9])?$", name):
        return "Skill name must be lowercase alphanumeric with hyphens, no leading/trailing hyphens."
    if "--" in name:
        return "Skill name must not contain consecutive hyphens (--)."
    return None


def title_case(name: str) -> str:
    """Convert kebab-case to Title Case."""
    return " ".join(word.capitalize() for word in name.split("-"))


# ── Core ─────────────────────────────────────────────────────────────────────


def init_skill(skill_name: str, category: str) -> bool:
    """Initialize a new bilingual skill. Returns True on success."""

    # Validate category
    if category not in VALID_CATEGORIES:
        print(f"❌ Invalid category: '{category}'")
        print(f"   Valid categories: {', '.join(VALID_CATEGORIES)}")
        return False

    # Validate name
    err = validate_skill_name(skill_name)
    if err:
        print(f"❌ Invalid skill name: {err}")
        return False

    skill_dir = SKILLS_DIR / category / skill_name

    if skill_dir.exists():
        print(f"❌ Skill already exists: {skill_dir.relative_to(SKILLS_DIR.parent)}")
        return False

    skill_title = title_case(skill_name)
    fmt = dict(
        skill_name=skill_name,
        skill_title=skill_title,
        author=AUTHOR,
        license=LICENSE,
    )

    # Create structure
    for lang, skill_tpl, ref_tpl in [
        ("ua", SKILL_TEMPLATE_UA, REFERENCE_TEMPLATE_UA),
        ("en", SKILL_TEMPLATE_EN, REFERENCE_TEMPLATE_EN),
    ]:
        lang_dir = skill_dir / lang
        refs_dir = lang_dir / "references"
        refs_dir.mkdir(parents=True, exist_ok=True)

        # SKILL.md
        (lang_dir / "SKILL.md").write_text(skill_tpl.format(**fmt))

        # references/REFERENCE.md
        (refs_dir / "REFERENCE.md").write_text(ref_tpl.format(**fmt))

    rel = skill_dir.relative_to(SKILLS_DIR.parent)
    print(f"✅ Skill '{skill_name}' created at {rel}/")
    print()
    print("   Structure:")
    print(f"   {rel}/")
    print(f"   ├── ua/")
    print(f"   │   ├── SKILL.md")
    print(f"   │   └── references/REFERENCE.md")
    print(f"   └── en/")
    print(f"       ├── SKILL.md")
    print(f"       └── references/REFERENCE.md")
    print()
    print("   Next steps:")
    print("   1. Fill in the [TODO] sections in ua/SKILL.md")
    print("   2. Fill in the [TODO] sections in en/SKILL.md")
    print("   3. Complete both references/REFERENCE.md files")

    return True


# ── CLI ──────────────────────────────────────────────────────────────────────


def main():
    if len(sys.argv) < 4 or sys.argv[2] != "--category":
        print("Usage: python3 scripts/init_skill.py <skill-name> --category <category>")
        print()
        print("Categories:")
        for cat in VALID_CATEGORIES:
            print(f"  - {cat}")
        print()
        print("Examples:")
        print("  python3 scripts/init_skill.py abstract-ua-en --category writing")
        print("  python3 scripts/init_skill.py paper-triage --category literature-review")
        sys.exit(1)

    skill_name = sys.argv[1]
    category = sys.argv[3]

    success = init_skill(skill_name, category)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
