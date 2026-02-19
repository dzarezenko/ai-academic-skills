# ai-academic-skills

A modular collection of AI-powered academic skills for research workflows, citation normalization, scientific writing, literature review, and experimental documentation.

---

## Mission Statement

**ai-academic-skills** aims to provide researchers, students, and academic writers with a structured, reusable toolkit of AI-assisted skills that streamline the most demanding parts of the academic research process — from managing citations and writing abstracts to conducting literature reviews and documenting experiments.

The project is built on three core principles:
- **Modularity** — each skill is self-contained and independently usable.
- **Bilinguality** — every skill supports both Ukrainian (UA) and English (EN).
- **Openness** — the toolkit is open-source and community-driven.

---

## Bilingual Structure (UA / EN)

Every skill in this repository is organized into two language subfolders:

```
skills/<category>/<skill-name>/
├── UA/   ← Ukrainian version of the skill
└── EN/   ← English version of the skill
```

This separation ensures that each skill can be maintained, extended, and localized independently, without coupling between language variants.

---

## Skill Categories

### 📚 `skills/citations/`
Skills related to citation formatting and normalization.
- **citation-to-dstu** — Converts references to the DSTU 8302:2015 standard (Ukrainian academic standard).

### ✍️ `skills/writing/`
Skills that assist with academic writing tasks.
- **abstract-ua-en** — Generates or refines structured abstracts in Ukrainian and English.
- **plagiarism-risk-check** — Identifies high-risk paraphrasing patterns and suggests rewrites.

### 🔬 `skills/literature-review/`
Skills for discovering, evaluating, and synthesizing academic literature.
- **paper-triage** — Quickly assesses the relevance and quality of a paper.
- **related-work-synthesis** — Synthesizes related work sections from a set of references.

### 🧪 `skills/experiments/`
Skills for documenting and reporting on experimental work.
- **dataset-card** — Generates structured dataset documentation cards.
- **metrics-report** — Produces a formatted evaluation report from experiment results.

---

## Shared Resources

The `shared/` directory contains cross-skill assets:
- **`templates/`** — Reusable document templates.
- **`examples/`** — Sample inputs and outputs for demonstration.
- **`schemas/`** — JSON/YAML schemas for structured skill I/O.

---

## Roadmap

| Version | Milestone |
|---------|-----------|
| **v0.1** | Base project structure and documentation scaffolding |
| **v0.2** | First skill implementations (citation-to-dstu, abstract-ua-en) |
| **v1.0** | Stable academic toolkit with full skill coverage and shared schemas |

See [`docs/roadmap.md`](docs/roadmap.md) for the full roadmap.

---

## Documentation

- [Architecture](docs/architecture.md) — Design decisions and extensibility notes.
- [Contribution Guidelines](docs/contribution-guidelines.md) — How to add new skills.
- [Roadmap](docs/roadmap.md) — Planned versions and milestones.

---

## License

This project is licensed under the [MIT License](LICENSE).
