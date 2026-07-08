# Annex C — Specifications

| Summary | Technical specifications for the OpenREL platform: data model, permissions, integrations, and component behaviour |
| :---- | :---- |
| **Status** | Draft |
| **Version** | 0.1 |
| **Date** | 2026-06-16 |
| **Author** | W Hugo |

---

## 1. Data Model

The following entities are persisted in the Base44 platform database:

| Entity | Purpose | Key Fields |
| :-- | :-- | :-- |
| `GlobalConfig` | Single global configuration record | `github_token`, `github_repo`, `kb_search_data_url`, `kb_search_data_api_url`, `kb_policy_file`, `kb_sub_entity_files`, `badge_mappings` |
| `Project` | Named project context for pipeline grouping | `name`, `github_repo`, `github_token`, `github_branch`, `github_output_folder`, `trl` |
| `Pipeline` | ETL pipeline definition | `name`, `project_id`, `source_type`, `source_file_url`, `template`, `field_mapping`, `github_target_folder`, `status`, `schedule` |
| `PipelineRun` | Execution history for a pipeline | `pipeline_id`, `status`, `started_at`, `completed_at`, `records_loaded`, `error_message`, `logs` |
| `WorkflowInstance` | Saved guided workflow session | `name`, `workflow_type`, `step_data`, `created_by_orcid`, `updated_by_orcid`, `last_opened_at` |
| `ObjectAnalysis` | Policy/licence analysis of a URL or text | `name`, `input_type`, `object_url`, `text_content`, `analysis_result`, `action_mappings`, `last_analysed_at` |
| `UserScenario` | Saved scenario set for policy matching | `label`, `selected_scenario_ids`, `saved_matches`, `saved_matches_at` |
| `FacetConfig` | Filter facet configuration for KB Search | `title`, `field_key`, `facet_type`, `default_logic`, `max_visible_items`, `is_active`, `sort_order`, `context` |
| `VocabularySource` | Registered external vocabulary source | `name`, `source_type`, `source_url`, `github_repo`, `github_path`, `data_format`, `value_field`, `label_field` |
| `VocabularyLink` | Links a vocabulary to an entity field | `vocabulary_source_id`, `target_entity`, `target_field`, `display_label`, `allow_multiple` |
| `ChecklistSource` | Registered checklist source | `name`, `source_type`, `github_repo`, `github_path`, `recommended_policies` |
| `ChecklistLink` | Links a checklist to an entity field | `checklist_source_id`, `target_entity`, `target_field`, `allow_multiple` |
| `FeatureCard` | 'I Want To...' dashboard shortcut card | `title`, `description`, `icon_name`, `target_path`, `linked_type`, `create_new_instance`, `order`, `is_active` |

**Note:** Policy content (policies, actions, constraints, scenarios, agents, sources) is **not** stored in the platform database. It resides in JSON files in the configured GitHub repository.

---

## 2. Role and Permission Model

### 2.1 Roles

Four roles: `Administrator`, `Curator`, `Contributor`, `End User`. Administrator access is always `true` and cannot be overridden.

### 2.2 Default Feature Access - KB Manager

| Feature | Admin | Curator | Contributor | End User |
| :-- | :--: | :--: | :--: | :--: |
| Dashboard | Y | Y | N | N |
| Projects | Y | Y | N | N |
| Knowledge Bases | Y | Y | N | N |
| ETL Pipeline | Y | Y | N | N |
| Schema Validator | Y | Y | N | N |
| Template Manager | Y | Y | N | N |
| Schema Extraction | Y | Y | N | N |
| Data Sync | Y | Y | N | N |
| Vocabulary Manager | Y | Y | N | N |
| Vocabulary Linker | Y | Y | N | N |
| Vocabulary Maker | Y | Y | N | N |
| Manual Vocab Links | Y | Y | N | N |
| Annotation Notes | Y | Y | N | N |
| Populate Sub-Objects | Y | Y | N | N |
| Provenance Viewer | Y | Y | Y | Y |
| Checklist Manager | Y | Y | N | N |
| Settings | Y | N | N | N |

### 2.3 Default Feature Access - KB User

| Feature | Admin | Curator | Contributor | End User |
| :-- | :--: | :--: | :--: | :--: |
| Dashboard | Y | Y | Y | Y |
| My Workflows | Y | Y | Y | Y |
| Search | Y | Y | Y | Y |
| Annotate | Y | Y | Y | N |
| Match | Y | Y | Y | Y |
| Compose | Y | Y | Y | N |
| Preferences | Y | Y | Y | N |
| Configuration | Y | Y | N | N |

### 2.4 Workflow Type Access

| Type | Admin | Curator | Contributor | End User |
| :-- | :--: | :--: | :--: | :--: |
| Licence a Resource | Y | Y | Y | Y |
| Reuse a Resource | Y | Y | Y | Y |
| Policy/Licence Analysis | Y | Y | Y | N |

### 2.5 Permission Overrides
Stored in `localStorage` under `openrel_permissions` as `{ [path]: { Administrator, Curator, Contributor, 'End User' } }`. Editable via Settings > Role Permissions Editor (Administrator only).

---

## 3. GitHub Integration Specification

### 3.1 Configuration Fields

| Config Field | Description |
| :-- | :-- |
| `github_token` | Personal Access Token with `repo` scope |
| `github_repo` | Repository in `owner/repo` format |
| `github_branch` | Target branch (default: `main`) |
| `github_output_folder` | Base folder for ETL output files |
| `kb_search_data_url` | Raw content base URL for KB data files |
| `kb_search_data_api_url` | GitHub API URL for listing KB data files |
| `kb_policy_file` | Filename of the policy JSON file |
| `kb_sub_entity_files` | Map of `{ actions, constraints, states, scenarios, agents, sources }` to filenames |

### 3.2 Backend Function: `githubFiles`

| Action | Description |
| :-- | :-- |
| `listRepos` | Lists all repos accessible to the PAT |
| `testToken` | Verifies the PAT is valid |
| `listFolder` | Lists files in a repository path |
| `getFile` | Fetches and Base64-decodes a file, returns SHA |
| `putFile` | Creates or updates a file (SHA required for updates) |

### 3.3 `submitPolicyPR`
Creates a feature branch, commits a modified policy JSON file, opens a Pull Request.

### 3.4 `syncConfigToGithub`
Serialises pipeline configuration to YAML and writes it to `.openrel/pipelines`.

---

## 4. Workflow Engine Specification

### 4.1 Workflow Types

| Type ID | Label | Steps |
| :-- | :-- | :-- |
| `licence` | Licence a Resource | User Context, Find Resource, Intended Use / Checklist, Review, Generate Draft |
| `reuse` | Reuse a Resource | User Context, Resource, Reuse Context, Licence Examination, Review |
| `policy_analysis` | Policy/Licence Analysis | Content Source, Run Analysis |

### 4.2 Step Persistence
Step data is serialised to `localStorage` under `wf_{instanceId}_{stepId}`. On Save, all step keys are written to `WorkflowInstance.step_data`.

### 4.3 Step Components

| Step ID | Component | Description |
| :-- | :-- | :-- |
| `user-context` | WorkflowStep1UserContext | ORCID, institution affiliation, role/badge data |
| `find` | WorkflowStep2FindResource | PID resolution and metadata extraction |
| `resource` | WorkflowStep2Resource | Manual resource description |
| `reuse-context` | WorkflowStep3IntendedUse | Intended use, reuse purpose, scenario flags |
| `licence` | WorkflowStep3ExamineContent | Content fetched and evaluated against checklists |
| `checklist` | WorkflowStep3ChecklistSelection | Checklist item selection |
| `review` | WorkflowStep4Review | Matching policies presented for selection |
| `generate` | WorkflowStep5Generate | Merges selected policies into a draft |
| `content-source` | OAStepContentSource | URL / text / file input for analysis |
| `run-analysis` | OAStepRunAnalysis | LLM analysis against KB actions and constraints |

---

## 5. Policy Composition Specification

### 5.1 Policy Data Structure

Policies follow an ODRL-compatible structure, extended by OpenREL to accommodate additional concerns (privacy, ethics, data subject rights) not strictly covered by ODRL's creator-rights focus. Actions and constraints have been expanded beyond native ODRL definitions to address these broader licensing and policy requirements.


| Field | Type | Description |
| :-- | :-- | :-- |
| `id` | string | Unique policy identifier (CURIE or URI) |
| `label` | string | Human-readable name |
| `odrl_type` | string | ODRL class (odrl:Agreement, odrl:Offer, odrl:Set, etc.) |
| `status` | string | Lifecycle status |
| `assigner` | string | Entity assigning the policy |
| `assignee` | string | Entity receiving the policy |
| `derived_from` | string | Parent policy ID |
| `permissions` | Rule[] | Permission rules |
| `prohibitions` | Rule[] | Prohibition rules |
| `duties` | Rule[] | Duty rules |
| `created_by_orcid` | string | ORCID of original author |
| `updated_by_orcid` | string | ORCID of last editor |

Rule structure: `{ "action": "<action-id>", "constraint": [ { "id": "<constraint-id>", "leftOperand": "", "operator": "", "rightOperand": "" } ] }`

### 5.2 Draft Lifecycle

```
Template (remote) -> New Draft (localStorage, status=draft)
    -> Edit -> Submit PR (status=pending)
    -> GitHub review -> Merged (status=active)
```

---

## 6. Faceted Search Specification

### 6.1 FacetConfig Fields

| Field | Type | Description |
| :-- | :-- | :-- |
| `title` | string | Label in the filter panel |
| `field_key` | string | Policy field used for filtering |
| `facet_type` | enum | pills, search_list, chart, timeline, map |
| `default_logic` | enum | OR (default) or AND |
| `max_visible_items` | number | Items before scroll (default: 6) |
| `is_active` | boolean | Shown in filter panel |
| `sort_order` | number | Display order |
| `context` | enum | policies, actions, constraints |

### 6.2 Filter Logic
- **OR:** field must match at least one selected value
- **AND:** field must match all selected values
- Array fields (e.g., `jurisdiction`) supported via `some()` / `every()`

### 6.3 Fallback
If no active FacetConfig exists, defaults to `odrl_type` (pills) and `status` (pills).

---

## 7. Provenance Specification

| Field | Applies To | Description |
| :-- | :-- | :-- |
| `created_by_orcid` | Policy drafts, WorkflowInstance | ORCID of original creator; set once, never overwritten |
| `updated_by_orcid` | Policy drafts, WorkflowInstance | ORCID of last editor; updated on every save |

Resolved from `base44.auth.me().orcid`; falls back to retroactive ORCID `0000-0002-0255-5101`. On first load, records missing `created_by_orcid` are backfilled.

---

## 8. Backend Functions Reference

| Function | Purpose |
| :-- | :-- |
| `githubFiles` | Read/write files in a GitHub repository |
| `submitPolicyPR` | Submit a policy change as a GitHub Pull Request |
| `syncConfigToGithub` | Write pipeline config YAML to GitHub |
| `executePipeline` | Run an ETL pipeline: extract, transform, load to GitHub |
| `parseSourceFile` | Parse source file and return field names + sample data |
| `parseTemplate` | Parse a template and return its field list |
| `analyzeJsonStructure` | Infer schema of a JSON file |
| `getVocabulary` | Fetch and cache a VocabularySource |
| `getChecklist` | Fetch and cache a ChecklistSource |
| `analyzeContentWithChecklists` | LLM content analysis against checklists |
| `analyzeObject` | LLM analysis of URL/text against KB actions and constraints |
| `resolvePid` | Resolve a PID (DOI, Handle, URL) to its metadata |
| `extractLicenseInfo` | Extract licence information from a resource |
| `matchLicenseSpdx` | Match a licence string to an SPDX identifier |
| `fetchOrcidAffiliations` | Fetch affiliation data for an ORCID iD |
| `verifyInstitution` | Verify institutional affiliation via an external registry |
