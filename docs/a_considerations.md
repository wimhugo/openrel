# Annex A — Design Considerations

| Summary | Architectural drivers, key design decisions, and known constraints for the OpenREL platform |
| :---- | :---- |
| **Status** | Draft |
| **Version** | 0.1 |
| **Date** | 2026-06-16 |
| **Author** | W Hugo |

---

## 1. Architectural Drivers

The following forces shaped the overall design of the OpenREL platform:

### 1.1 Open Standards Alignment
OpenREL is designed around ODRL (Open Digital Rights Language) as the canonical policy model. All policies, actions, and constraints follow ODRL vocabulary and structure. This allows interoperability with other rights management systems and ensures policies are machine-readable.

### 1.2 GitHub as the Single Source of Truth
Rather than a proprietary database for policy content, OpenREL uses a GitHub repository as its data backbone. JSON files in a configurable folder are the authoritative source for policies, actions, constraints, scenarios, agents, and vocabulary terms. This provides:
- Version-controlled policy history
- Collaboration via Pull Requests
- Transparency and auditability
- Independence from vendor lock-in for the data layer

### 1.3 Role-Based, Multi-Persona Design
The platform serves distinct user types with very different needs:
- **Administrators** configure the platform and manage permissions
- **Curators** manage knowledge base content (ETL, vocabulary, templates)
- **Contributors** create and submit policy drafts
- **End Users** search, match, and apply policies to resources

This drove a dual-container architecture (KB Manager / KB User) with configurable role-based access per feature.

### 1.4 ORCID as Researcher Identity
All policy authorship is attributed via ORCID iDs rather than platform usernames. This decouples policy provenance from the platform's own auth system and aligns with academic publishing norms.

### 1.5 Progressive Disclosure
The KB User interface is designed so that End Users encounter only the features appropriate to their role. Complexity (vocabulary management, ETL pipelines, facet configuration) is hidden from lower-privilege roles.

---

## 2. Key Design Decisions

### 2.1 Browser-Side Drafts via localStorage
**Decision:** Policy drafts in the Compose module are stored in `localStorage`, not in the platform database.

**Rationale:** This avoids polluting the shared policy database with in-progress work and allows contributors to iterate freely. Drafts are only written to GitHub via Pull Request when explicitly submitted.

**Trade-off:** Drafts are device- and browser-specific. Clearing browser storage loses unsaved work.

### 2.2 Runtime Data Fetching from GitHub
**Decision:** Policy, action, constraint, and scenario data is fetched at runtime directly from GitHub raw content URLs, not imported into the platform database.

**Rationale:** Keeps GitHub as the authoritative source; avoids sync complexity. Changes in GitHub are reflected immediately on the next fetch.

**Trade-off:** The app requires network access to GitHub at runtime. Public-rate-limited GitHub API calls are used for directory listing (authenticated via PAT in GlobalConfig).

### 2.3 FacetConfig as a Configurable Entity
**Decision:** Filter facets in KB Search and Compose are driven by a `FacetConfig` entity stored in the platform database rather than being hardcoded.

**Rationale:** Allows administrators to tailor the search experience to the specific vocabulary of their deployed knowledge base without code changes.

**Trade-off:** Requires initial configuration; falls back to hardcoded defaults (odrl_type, status) if no FacetConfig records exist.

### 2.4 Workflow Engine as a Multi-Step Wizard
**Decision:** The guided workflows (Licence, Reuse, Policy Analysis) are implemented as step-based wizards with `localStorage` persistence per step.

**Rationale:** Workflows involve external lookups (ORCID affiliations, PID resolution, checklist evaluation) and may take multiple sessions to complete. Persisting each step locally avoids losing work on navigation.

**Trade-off:** Step data is stored partially in `localStorage` and partially in the `WorkflowInstance` entity's `step_data` field; the manual Save button is required to sync them.

### 2.5 Pull Request Model for Policy Submission
**Decision:** Policy changes are submitted to GitHub via Pull Requests rather than direct commits.

**Rationale:** Enforces a review and approval gate before any policy change is merged into the authoritative dataset. Aligns with open-source governance norms.

### 2.6 Badge Mapping as a Configuration Artefact
**Decision:** User profile verification badges (e.g., 'Verified Researcher', 'EU Member') are mapped to ODRL constraint keys via a configurable YAML file stored in GitHub.

**Rationale:** Allows the constraint-matching logic in the Match module to be tuned per deployment without code changes.

---

## 3. Constraints and Assumptions

| # | Constraint / Assumption |
| :-- | :-- |
| C1 | GitHub is available and the configured PAT has read/write access to the target repository |
| C2 | All policy data files are valid JSON and follow the agreed ODRL-derived schema |
| C3 | The platform runs on a modern browser (ES2020+); no IE or legacy browser support |
| C4 | Users must have a valid ORCID iD to attribute authorship; the platform does not mint ORCIDs |
| C5 | The Base44 BaaS platform provides auth, realtime, and entity persistence; these are not reimplemented |
| C6 | Role permissions can be overridden per deployment via the Settings page; defaults are defined in code |
| C7 | Sub-entity files (actions, constraints, etc.) are co-located in the same GitHub folder as the policy file |
| C8 | The `submitPolicyPR` backend function requires a GitHub PAT with `repo` scope |

---

## 4. Known Limitations and Technical Debt

| # | Item | Impact | Priority |
| :-- | :-- | :-- | :-- |
| L1 | Workflow step data is split between `localStorage` and the `step_data` DB field; manual Save is required to sync | Data loss risk if browser is closed before saving | High |
| L2 | Annotate page is a placeholder — annotation functionality is not yet implemented | Missing feature for KB Users | Medium |
| L3 | Draft policies are device-specific (localStorage); no cross-device or collaborative editing | Limits multi-author policy workflows | Medium |
| L4 | GitHub API rate limits apply to unauthenticated file listing; heavy use may hit limits | Degraded performance for large teams | Medium |
| L5 | Policy submission creates a PR against the raw policy file path, not a branch-per-policy | Potential merge conflicts if multiple contributors submit simultaneously | Medium |
| L6 | The FacetConfig `chart` and `timeline` facet types render as placeholders and are not fully implemented | Limited facet variety | Low |
| L7 | Badge mapping YAML serialisation is hand-rolled and fragile for special characters | Potential data corruption in badge configs | Low |
| L8 | TRL (Technology Readiness Level) field exists in the Project entity but is not surfaced in the UI beyond settings | Underutilised metadata | Low |
