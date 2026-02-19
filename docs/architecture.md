# Architecture

## Overview

**ai-academic-skills** is designed as a flat, modular collection of discrete AI-assisted skills. Each skill is an independent unit that can be used in isolation or composed into larger research workflows.

---

## Directory Layout

```
ai-academic-skills/
├── skills/          ← Individual AI skills, grouped by category
├── shared/          ← Cross-skill assets (templates, examples, schemas)
└── docs/            ← Project-level documentation
```

### `skills/`

Skills are grouped into thematic categories:

| Category | Description |
|---|---|
| `citations/` | Reference formatting and normalization |
| `writing/` | Academic writing assistance |
| `literature-review/` | Paper evaluation and synthesis |
| `experiments/` | Dataset and experiment documentation |

Each skill lives in its own subfolder under the relevant category:

```
skills/<category>/<skill-name>/
├── ua/   ← Ukrainian language variant
└── en/   ← English language variant
```

This structure makes it trivial to:
- Add a new skill without touching any existing skill.
- Add a new language variant to an existing skill.
- Delete or deprecate a skill without side-effects.

### `shared/`

```
shared/
├── templates/   ← Reusable document templates shared across skills
├── examples/    ← Sample inputs/outputs for testing and demonstration
└── schemas/     ← JSON/YAML schemas defining skill I/O contracts
```

Shared assets reduce duplication and provide a stable contract layer between skills and any external tooling (CLI, API, IDE plugins).

### `docs/`

Project-level documentation only. No skill content lives here.

---

## Language Separation Strategy

Every skill **must** provide both a `ua/` and an `en/` folder. This ensures:

1. **Independence** — each language variant is maintained separately with no coupling.
2. **Completeness** — consumers can require both variants to exist before a skill is considered stable.
3. **Localisation quality** — Ukrainian academic conventions (e.g., DSTU citation standards) can differ significantly from English ones; separate folders allow tailoring.

---

## Future Extensibility

The architecture is intentionally flat and convention-based, which supports the following growth paths:

- **New skill categories** — add a new subfolder under `skills/`.
- **New languages** — add a new language folder (e.g., `de/`, `pl/`) alongside `ua/` and `en/`.
- **CLI integration** — the `shared/schemas/` layer provides a stable I/O contract for a future command-line runner.
- **API integration** — skills can be wrapped as API endpoints; the bilingual folder structure maps cleanly to a `?lang=ua|en` query parameter.
- **Plugin ecosystem** — IDE or browser extensions can consume skills by pointing at a skill's language folder.

The design deliberately avoids a framework or runtime dependency so that the repository remains accessible to contributors who only need a text editor.
