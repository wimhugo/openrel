# OpenREL Application Documentation

| Summary | Documentation covering the design, requirements, and specifications of the OpenREL Knowledge Base platform |
| :---- | :---- |
| **Audience** | Developers, administrators, and research stakeholders |
| **Status** | Draft |

| Date | Authors | Description | Version |
| :---- | :---- | :---- | :---: |
| 2026-06-16 | W Hugo | Initial reverse-engineered documentation from codebase | 0.1 |

| Licence | [CC 4.0 BY](https://creativecommons.org/licenses/by/4.0/deed.en) |
| :---- | :---- |
| **Funding** | TBD |
| **Contributors** | W Hugo |

---

## Overview

OpenREL is a dual-mode web application for managing, searching, composing, and reasoning about ODRL-based data licensing policies. It is structured as two tightly integrated containers:

- **KB Manager** — an ETL and curation toolset for administrators and data curators who create, maintain, and publish the knowledge base.
- **KB User** — a research-facing interface for discovering, composing, matching, and applying policies to research resources.

The platform integrates with GitHub as its primary data backbone: policies, vocabularies, actions, constraints, and scenarios are all stored as JSON files in a configurable GitHub repository. The app reads from these files at runtime and writes back via Pull Requests.

---

## Table of Contents

### A — Design Considerations
[docs/a_considerations.md](./a_considerations.md)

1. Architectural Drivers
2. Key Design Decisions
3. Constraints and Assumptions
4. Known Limitations and Technical Debt

### B — User Stories and Requirements
[docs/b_requirements.md](./b_requirements.md)

1. User Personas and Roles
2. User Stories — KB Manager
3. User Stories — KB User
4. Functional Requirements
5. Non-Functional Requirements

### C — Specifications
[docs/c_specifications.md](./c_specifications.md)

1. Data Model
2. Role and Permission Model
3. GitHub Integration Specification
4. Workflow Engine Specification
5. Policy Composition Specification
6. Faceted Search Specification
7. Provenance Specification
8. Backend Functions Reference
