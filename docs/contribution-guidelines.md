# Contribution Guidelines

Thank you for your interest in contributing to **ai-academic-skills**!
This document explains how to add a new skill, follow naming conventions, and keep the repository consistent.

---

## Prerequisites

- Familiarity with the [project architecture](architecture.md).
- A GitHub account and basic knowledge of Git.
- Understanding of the academic domain your skill addresses.

---

## How to Add a New Skill

### 1. Choose the right category

Place your skill under the most appropriate category inside `skills/`:

| Category | When to use |
|---|---|
| `citations/` | Reference formatting, normalization, style conversion |
| `writing/` | Abstract generation, paraphrase checking, style editing |
| `literature-review/` | Paper relevance scoring, synthesis, gap analysis |
| `experiments/` | Dataset cards, metrics reports, reproducibility checklists |

If no existing category fits, propose a new one in an issue before proceeding.

### 2. Create the skill directory

```
skills/<category>/<skill-name>/
├── ua/
└── en/
```

**Both `ua/` and `en/` subfolders are mandatory.**
A skill is not considered complete until both language variants exist.

### 3. Populate the language folders

Add the skill content inside the `ua/` and `en/` subfolders according to the skill format defined in `shared/schemas/`.
Refer to `shared/examples/` for reference implementations.

### 4. Open a Pull Request

- Branch from `main` using the naming convention: `skill/<skill-name>`.
- Describe what the skill does, which category it belongs to, and what academic task it addresses.
- Ensure both `ua/` and `en/` folders are populated before requesting review.

---

## Naming Conventions

| Item | Convention | Example |
|---|---|---|
| Skill folder | `kebab-case` | `citation-to-dstu` |
| Category folder | `kebab-case` | `literature-review` |
| Language folders | lowercase ISO 639-1 code | `ua`, `en` |
| Template files | `kebab-case` with extension | `abstract-template.md` |
| Schema files | `kebab-case` with `.schema.json` | `skill-input.schema.json` |

---

## General Rules

- **Do not** modify other skills unless fixing a clear bug.
- **Do not** add runtime dependencies (this is a documentation-first repository).
- **Do not** leave `ua/` or `en/` folders empty in a merged PR (use a `.gitkeep` only during scaffolding phases).
- Keep all documentation in professional academic English and, where applicable, in grammatically correct Ukrainian.
- Update `docs/roadmap.md` if your contribution corresponds to a planned milestone.

---

## Questions

Open an issue with the label `question` if anything is unclear.
