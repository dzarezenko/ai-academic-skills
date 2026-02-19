# Roadmap

This document tracks the planned milestones for **ai-academic-skills**.

---

## v0.1 — Structure Initialization *(current)*

**Goal:** Establish a clean, well-documented project scaffold that can support 20+ future skills.

- [x] Define directory structure (`skills/`, `shared/`, `docs/`)
- [x] Create bilingual skeleton (UA/EN) for all planned skills
- [x] Write project README
- [x] Write architecture documentation
- [x] Write contribution guidelines
- [x] Add MIT license and `.gitignore`

---

## v0.2 — First Skill Implementations

**Goal:** Ship the first two working skills with complete UA and EN variants.

- [ ] Implement `skills/citations/citation-to-dstu` (UA + EN)
- [ ] Implement `skills/writing/abstract-ua-en` (UA + EN)
- [ ] Define initial JSON schemas in `shared/schemas/`
- [ ] Add usage examples in `shared/examples/`
- [ ] Validate skills against schemas

---

## v0.3 — Writing & Review Skills

**Goal:** Cover the most common academic writing and review tasks.

- [ ] Implement `skills/writing/plagiarism-risk-check` (UA + EN)
- [ ] Implement `skills/literature-review/paper-triage` (UA + EN)
- [ ] Implement `skills/literature-review/related-work-synthesis` (UA + EN)
- [ ] Add reusable templates to `shared/templates/`

---

## v0.4 — Experimental Documentation Skills

**Goal:** Support researchers in documenting datasets and reporting metrics.

- [ ] Implement `skills/experiments/dataset-card` (UA + EN)
- [ ] Implement `skills/experiments/metrics-report` (UA + EN)

---

## v1.0 — Stable Academic Toolkit

**Goal:** A production-ready, fully documented academic AI toolkit.

- [ ] All planned skills implemented and reviewed
- [ ] Complete shared schema coverage
- [ ] CLI integration prototype
- [ ] Comprehensive examples for every skill
- [ ] Community contributions welcome (first external PR merged)
- [ ] Stable versioning policy established

---

## Beyond v1.0

Potential future directions:

- Additional language variants (e.g., `DE/`, `PL/`).
- API wrapper for programmatic skill invocation.
- IDE / browser extension integration.
- Automated quality checks via CI for skill completeness and schema compliance.
