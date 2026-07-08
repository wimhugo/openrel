# Annex B — User Stories and Requirements

| Summary | User stories, functional and non-functional requirements for the OpenREL platform |
| :---- | :---- |
| **Status** | Draft |
| **Version** | 0.1 |
| **Date** | 2026-06-16 |
| **Author** | W Hugo |

---

## 1. User Personas and Roles

OpenREL defines four roles with progressively restricted access:

| Role | Description | Primary Container |
| :-- | :-- | :-- |
| **Administrator** | Full access to all features. Configures the platform, manages permissions, and maintains the global configuration. | Both |
| **Curator** | Manages knowledge base content: runs ETL pipelines, manages vocabularies, configures facets. Cannot access platform-wide Settings. | KB Manager + KB User |
| **Contributor** | Creates and submits policy drafts via Compose. Runs workflows. Cannot manage vocabulary or ETL pipelines. | KB User |
| **End User** | Discovers, searches, and matches policies. Can run Licence and Reuse workflows. Read-only for composition. | KB User |

---

## 2. User Stories — KB Manager

Contextual Note: While OpenREL maintains ODRL as its canonical format, it acknowledges the limitations of ODRL's narrow focus on intellectual property. OpenREL defines extended action and constraint vocabularies to address the broader ecosystem of data licence governance, including privacy and ethical frameworks.

### 2.1 ETL Pipeline Management

| # | User Story | Role |
| :-- | :-- | :-- |
| M1 | As a Curator, I want to create an ETL pipeline that maps source CSV/JSON fields to a policy template, so that I can batch-import records into the knowledge base. | Curator+ |
| M2 | As a Curator, I want to run a pipeline manually and see its execution log, so that I can verify the output and diagnose failures. | Curator+ |
| M3 | As an Administrator, I want to associate pipelines with a Project, so that different initiatives can have isolated data contexts. | Admin |
| M4 | As a Curator, I want to copy an existing pipeline as a starting point, so that I can adapt it without starting from scratch. | Curator+ |
| M5 | As a Curator, I want to view a dashboard of pipeline run statistics, so that I can monitor the health of the ETL process. | Curator+ |

### 2.2 Schema and Template Management

| # | User Story | Role |
| :-- | :-- | :-- |
| M6 | As a Curator, I want to validate a JSON file against a schema, so that I can catch errors before committing data. | Curator+ |
| M7 | As a Curator, I want to upload a JSON/JSON-LD template and inspect its fields, so that I can use it as a mapping target in a pipeline. | Curator+ |
| M8 | As a Curator, I want to extract a schema from an existing JSON file, so that I can create a formal schema for a legacy dataset. | Curator+ |

### 2.3 Vocabulary Management

| # | User Story | Role |
| :-- | :-- | :-- |
| M9 | As a Curator, I want to register an external vocabulary source (GitHub, URL, or inline), so that controlled values can be resolved across the platform. | Curator+ |
| M10 | As a Curator, I want to link a vocabulary to a specific field on an entity, so that forms and filters can use controlled values for that field. | Curator+ |
| M11 | As a Curator, I want to create a new vocabulary term directly in the platform, so that I can extend the vocabulary without editing files manually. | Curator+ |
| M12 | As a Curator, I want to configure which facets appear in the KB Search filter panel, what type they are (pills, list, chart), and in what order, so that the search UX matches the vocabulary of the deployed knowledge base. | Curator+ |

### 2.4 Data Synchronisation

| # | User Story | Role |
| :-- | :-- | :-- |
| M13 | As an Administrator, I want to sync the platform configuration to a GitHub repository, so that the setup is version-controlled and reproducible. | Admin |
| M14 | As an Administrator, I want to connect a GitHub Personal Access Token and select a target repository, so that write-back operations (PR submission, config sync) work correctly. | Admin |

---

## 3. User Stories — KB User

### 3.1 Dashboard

| # | User Story | Role |
| :-- | :-- | :-- |
| U1 | As any user, I want to see an overview of the knowledge base contents (policy count, action count, constraint count, etc.), so that I can understand the scope of available data. | All |
| U2 | As any user, I want to see a summary of my workflow instances, so that I can track what I have been working on. | All |
| U3 | As any user, I want to use 'I Want To…' shortcut cards on the dashboard, so that I can quickly navigate to common tasks. | All |

### 3.2 Policy Search

| # | User Story | Role |
| :-- | :-- | :-- |
| U4 | As any user, I want to search policies by label or ID using a text query, so that I can quickly find a specific policy. | All |
| U5 | As any user, I want to filter policies by ODRL type, status, or other facets, so that I can narrow down to relevant policies. | All |
| U6 | As any user, I want to expand a policy card to see its full rules (permissions, prohibitions, duties), so that I can understand what it allows and restricts. | All |
| U7 | As any user, I want to export a policy as a JSON file, so that I can use it in external tools. | All |
| U8 | As any user, I want to combine multiple facets with AND or OR logic, so that I can perform precise multi-criteria searches. | All |

### 3.3 Policy Composition

| # | User Story | Role |
| :-- | :-- | :-- |
| U9 | As a Contributor, I want to create a new policy draft from a template, so that I have a valid starting structure without writing JSON. | Contributor+ |
| U10 | As a Contributor, I want to copy an existing policy and modify it, so that I can create a derivative policy efficiently. | Contributor+ |
| U11 | As a Contributor, I want to edit a policy's metadata, permissions, prohibitions, and duties in a structured form, so that I don't have to edit raw JSON. | Contributor+ |
| U12 | As a Contributor, I want to submit a policy draft as a GitHub Pull Request, so that it can be reviewed and merged into the authoritative dataset. | Contributor+ |
| U13 | As a Contributor, I want my draft policies to persist between sessions, so that I can resume editing without losing work. | Contributor+ |
| U14 | As a Contributor, I want to delete a draft or hide a remote policy from my view, so that I can manage my working set. | Contributor+ |

### 3.4 Policy Matching

| # | User Story | Role |
| :-- | :-- | :-- |
| U15 | As any user, I want to define a user scenario as a set of applicable scenario flags, so that I can describe my research context formally. | All |
| U16 | As any user, I want to run a scenario against the policy database and see which policies match, so that I can identify which licences apply to my use case. | All |
| U17 | As any user, I want to save the results of a match run against a scenario, so that I can refer back to them later. | All |
| U18 | As any user, I want to clone a scenario, so that I can create variations without starting from scratch. | All |

### 3.5 Guided Workflows

| # | User Story | Role |
| :-- | :-- | :-- |
| U19 | As a researcher, I want to follow a guided 'Licence a Resource' workflow that captures my user context, the resource I want to licence, and generates a draft licence policy, so that I can produce a valid policy without deep ODRL knowledge. | Contributor+ |
| U20 | As a researcher, I want to follow a guided 'Reuse a Resource' workflow that evaluates the conditions under which I can reuse someone else's resource, so that I can assess compliance with existing policies. | All |
| U21 | As a Curator, I want to analyse the content of a URL or pasted text against the policy knowledge base, so that I can identify which existing policies or constraints are relevant to that resource. | Curator+ |
| U22 | As any user, I want to save my progress in a workflow and return to it later, so that I can complete multi-step processes across sessions. | All |
| U23 | As any user, I want to clone a workflow instance, so that I can apply the same context to a different resource. | All |

### 3.6 Provenance and Attribution

| # | User Story | Role |
| :-- | :-- | :-- |
| U24 | As any user, I want all artefacts I create (policies, workflows) to be attributed to my ORCID iD, so that I receive credit for my contributions. | All |
| U25 | As an Administrator, I want to view the provenance of all workflow instances and local policy drafts, so that I can audit who created what. | Admin |
| U26 | As an Administrator, I want to retroactively assign ORCID attribution to records created before this feature was introduced, so that the historical record is complete. | Admin |

### 3.7 Configuration

| # | User Story | Role |
| :-- | :-- | :-- |
| U27 | As a Curator, I want to configure the GitHub folder URL that serves as the KB data source, so that the platform reads from the correct repository location. | Curator+ |
| U28 | As a Curator, I want to assign specific JSON files to the policy, actions, constraints, and scenario roles, so that the platform knows which file to read for each entity type. | Curator+ |
| U29 | As an Administrator, I want to configure badge mappings that link user verification statuses to constraint keys, so that the Match module can automatically map a user's profile to applicable policy constraints. | Admin |
| U30 | As an Administrator, I want to edit the 'I Want To…' dashboard cards, so that I can customise the quick-access links for the users of my deployment. | Admin |

---

## 4. Functional Requirements

### 4.1 KB Manager

| ID | Requirement |
| :-- | :-- |
| FR-M1 | The system shall allow authenticated Curators and Administrators to create, configure, run, copy, edit, and delete ETL pipelines. |
| FR-M2 | The system shall support CSV, TXT, and JSON as pipeline source formats, and JSON or CSV as output formats. |
| FR-M3 | The system shall detect field names from uploaded source files and templates, and provide a mapping UI to link them. |
| FR-M4 | The system shall write pipeline output to a configurable GitHub repository path via the GitHub Contents API. |
| FR-M5 | The system shall log pipeline run history including start/end time, record counts, and status. |
| FR-M6 | The system shall validate JSON files against a user-provided or auto-detected schema. |
| FR-M7 | The system shall allow vocabulary sources to be registered from GitHub files, arbitrary URLs, or inline JSON. |
| FR-M8 | The system shall allow vocabulary sources to be linked to entity fields, with configurable display and value fields. |
| FR-M9 | The system shall allow facet configuration (title, field key, type, logic, visibility, order) for the KB Search and Detail pages. |

### 4.2 KB User — Search and Browse

| ID | Requirement |
| :-- | :-- |
| FR-U1 | The system shall fetch the configured policy JSON file from GitHub at runtime and display it as a searchable, filterable list. |
| FR-U2 | The system shall support free-text search against policy label and ID fields. |
| FR-U3 | The system shall support multi-value faceted filtering driven by FacetConfig records, with per-facet AND/OR logic. |
| FR-U4 | The system shall resolve action, constraint, and status references in policy rules to their full labels and descriptions. |
| FR-U5 | The system shall allow any policy to be exported as a formatted JSON file via a browser download. |

### 4.3 KB User — Composition

| ID | Requirement |
| :-- | :-- |
| FR-U6 | The system shall allow Contributors to create new policy drafts from template policies (policies with status `template`). |
| FR-U7 | The system shall allow draft policies to be edited via a structured form covering all ODRL fields. |
| FR-U8 | The system shall persist draft policies in `localStorage` between sessions. |
| FR-U9 | The system shall allow draft policies to be submitted as GitHub Pull Requests via the `submitPolicyPR` backend function. |
| FR-U10 | The system shall stamp all draft policies with the contributor's ORCID iD (`created_by_orcid`, `updated_by_orcid`). |

### 4.4 KB User — Workflow

| ID | Requirement |
| :-- | :-- |
| FR-U11 | The system shall support two guided workflow types: 'Licence a Resource' (5 steps) and 'Reuse a Resource' (5 steps), with a third 'Policy/Licence Analysis' type for object analysis. |
| FR-U12 | The system shall persist workflow step data to the `WorkflowInstance.step_data` field when the user clicks Save. |
| FR-U13 | The system shall attribute workflow instances to the creator's ORCID iD. |
| FR-U14 | The system shall allow workflow instances to be cloned, renamed, and deleted. |
| FR-U15 | Access to each workflow type shall be configurable per role via the permissions system. |

---

## 5. Non-Functional Requirements

| ID | Category | Requirement |
| :-- | :-- | :-- |
| NFR-1 | Performance | The policy list shall render within 3 seconds of the GitHub data file being fetched on a standard broadband connection. |
| NFR-2 | Availability | The application shall be available 24/7 as hosted by the Base44 platform; no additional uptime SLA is defined for this version. |
| NFR-3 | Security | GitHub Personal Access Tokens shall not be exposed to the browser; all authenticated GitHub API calls via the app shall use the token stored in GlobalConfig and accessed server-side. |
| NFR-4 | Security | Role-based access control shall be enforced in the UI; feature routes not permitted for the active role shall be hidden from navigation. |
| NFR-5 | Usability | The application shall be fully responsive and usable on desktop and tablet viewports. |
| NFR-6 | Usability | All policy data shall be presented in human-readable form (labels and descriptions), not raw JSON IDs, wherever possible. |
| NFR-7 | Maintainability | All policy content (data) shall reside in the GitHub repository, separate from application code, so that data can be updated without redeployment. |
| NFR-8 | Traceability | All policy artefacts created via the platform shall include ORCID-based provenance fields. |
| NFR-9 | Portability | Policy JSON files shall conform to the ODRL standard and be importable by any ODRL-compliant system. |
| NFR-10 | Extensibility | The facet filter system shall be configurable without code changes, so that new vocabulary dimensions can be added by administrators. |
