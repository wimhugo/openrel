# OpenREL Application Documentation

| Summary | Documentation covering the design, requirements, and specifications of the OpenREL Knowledge Base platform |
| :---- | :---- |
| **Audience** | Developers, administrators, and research stakeholders |
| **Status** | Draft |

| Date | Authors | Description | Version |
| :---- | :---- | :---- | :---: |
| 2026-06-16 | W Hugo | Initial reverse-engineered documentation from codebase | 0.1 |
| 2026-06-16 | W Hugo | Added Annex D: System Architecture (C1 + C2) | 0.3 |
| 2026-06-16 | W Hugo | Added Annex E: Policy Wizard UI Specification (v0.1) | 0.4 |
| 2026-06-16 | W Hugo | Rewrote Annex E based on full mock-up source analysis | 0.5 |

| Licence | [CC 4.0 BY](https://creativecommons.org/licenses/by/4.0/deed.en) |
| :---- | :---- |
| **Funding** | TBD |
| **Contributors** | W Hugo |

---

## Overview

OpenREL is a dual-mode web application for managing, searching, composing, and reasoning about data licensing policies. It extends the ODRL (Open Digital Rights Language) standard to capture concerns such as data subject rights, privacy legislation, and ethical considerations that fall outside of ODRL’s traditional focus on creator (IP) rights.

The platform is structured as two tightly integrated containers:

- **KB Manager** — an ETL and curation toolset for administrators and data curators who create, maintain, and publish the knowledge base.
- **KB User** — a research-facing interface for discovering, composing, matching, and applying policies to research resources.

The platform integrates with GitHub as its primary data backbone: policies, vocabularies, actions, constraints, and scenarios are all stored as JSON files in a configurable GitHub repository. The app reads from these files at runtime and writes back via Pull Requests.

---

## Table of Contents

### A — Design Considerations
[docs/a_considerations.md](./a_considerations.md)

### B — User Stories and Requirements
[docs/b_requirements.md](./b_requirements.md)

### C — Specifications
[docs/c_specifications.md](./c_specifications.md)

### D — System Architecture
[docs/d_architecture.md](./d_architecture.md)

Covers the C4 model architecture of the OpenREL platform:
- **C1 — System Context:** OpenREL as a single unit; key external actors (Users, Administrators) and systems (GitHub, ORCID, External Vocabularies).
- **C2 — Container Diagram:** Decomposition into KB Manager, KB User, Auth Service, App Database, and Backend Functions; data flows between containers and external systems.

### E — Policy Wizard UI Specification
[docs/e_ui_wizard.md](./e_ui_wizard.md)

Faithful UI specification derived from a full analysis of all HTML, CSS, and JavaScript in `data/input/v0.4/OpenREL_Wizard_mock.html`:
- **Three-view architecture:** Template Browser, Simple Wizard, Advanced Wizard — switched via `showView(v)`.
- **Simple Wizard:** 4-question flow — **Who** (access audience), **What** (permitted actions), **Where** (geographic restriction), **When** (time limit) — mapped to a canonical policy via `simpleToCanonical()`.
- **Advanced Wizard:** Full ODRL editor with 8 named sections: Policy Type, Metadata, Permissions, Prohibitions, Obligations, Constraints, Agents, Conflict Term. Live preview panel.
- **Constraint Catalogue:** 25 constraints (C01–C25) across 7 categories with IRIs and parameter types.
- **Action Catalogue:** 18 actions (A01–A18) with ODRL/OpenREL IRIs.
- **JavaScript State Model:** `SS` and `AS` state objects, `fp()` fingerprint function, template load/reverse-map logic.
