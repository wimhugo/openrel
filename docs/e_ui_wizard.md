# Annex E — Policy Wizard UI Specification

| Summary | UI design and behavioural specification for the OpenREL Policy Wizard, derived from the mock-up at `data/input/v0.4/OpenREL_Wizard_mock.html` |
| :---- | :---- |
| **Status** | Draft — awaiting integration review |
| **Version** | 0.1 |
| **Date** | 2026-06-16 |
| **Author** | W Hugo |
| **Source** | `data/input/v0.4/OpenREL_Wizard_mock.html` |

---

## Table of Contents
- [1. Purpose and Scope](#1-purpose-and-scope)
- [2. Design System](#2-design-system)
- [3. Global Layout](#3-global-layout)
- [4. Wizard Steps](#4-wizard-steps)
- [5. UI Components](#5-ui-components)
- [6. Behavioural Notes](#6-behavioural-notes)
- [7. Mapping to Existing KB User Workflows](#7-mapping-to-existing-kb-user-workflows)
- [8. Open Questions for Integration](#8-open-questions-for-integration)

---

## 1. Purpose and Scope

This document describes the intended UI design and interaction behaviour for the OpenREL Policy Wizard as specified in the HTML mock-up. The wizard is intended to replace or significantly enhance the existing multi-step workflow experience in the **KB User** container, covering the end-to-end process from user context identification through to policy composition and submission.

The mock-up presents a single-page, JavaScript-driven wizard with multiple named steps. It does **not** connect to a backend; all state is held in-page. This document captures its design intent to guide implementation in the existing React codebase.

---

## 2. Design System

### 2.1 Colour Tokens

The mock-up defines a bespoke colour system via CSS custom properties. These differ from the current OpenREL dark-mode Tailwind theme.

| Token | Value | Usage |
| :---- | :---- | :---- |
| `--navy` | `#0f2040` | Primary background (header, sidebar) |
| `--blue` | `#1a4a8a` | Secondary blue elements |
| `--mid` | `#2563c4` | Mid-level interactive elements |
| `--accent` | `#3b82f6` | Active highlights, links |
| `--pale` | `#eff6ff` | Light blue background tones |
| `--ice` | `#f0f7ff` | Very light card backgrounds |
| `--border` | `#c7d9f5` | Default border colour |
| `--text` | `#0f2040` | Primary body text |
| `--muted` | `#5a7296` | Secondary/muted text |
| `--green` | `#065f46` | Success / compliant status |
| `--glight` | `#ecfdf5` | Success badge background |
| `--gbord` | `#6ee7b7` | Success badge border |
| `--orange` | `#92400e` | Warning / review-needed status |
| `--olight` | `#fffbeb` | Warning badge background |
| `--obord` | `#fcd34d` | Warning badge border |
| `--red` | `#991b1b` | Error / non-compliant status |
| `--rlight` | `#fef2f2` | Error badge background |
| `--rbord` | `#fca5a5` | Error badge border |
| `--purple` | `#5b21b6` | Special/informational status |
| `--plight` | `#f5f3ff` | Info badge background |
| `--pbord` | `#c4b5fd` | Info badge border |

> **Integration note:** The mock-up uses a **light-mode** palette. The current OpenREL app uses a **dark-mode** theme. Integration will require mapping these tokens to the existing Tailwind design system (or extending it with light-mode equivalents).

### 2.2 Typography

| Role | Font | Weights |
| :---- | :---- | :---- |
| Headings / display | `DM Serif Display` (Google Fonts) | Regular, Italic |
| Body / UI | `DM Sans` | 300, 400, 500, 600 |
| Code / IDs | `DM Mono` | 400, 500 |

> The current app uses `Inter` (body) and `JetBrains Mono` (code). The mock-up proposes a shift to the DM family. This is a deliberate design decision to be confirmed.

### 2.3 Layout Constants

| Property | Value |
| :---- | :---- |
| Border radius | `10px` |
| Card shadow | `0 4px 24px rgba(15,32,64,.10)` |
| Body background | `#f4f7fc` |

---

## 3. Global Layout

### 3.1 Header

A **sticky top navigation bar** with height `60px` on a `--navy` background.

| Element | Description |
| :---- | :---- |
| Logo | `OpenREL` in DM Serif Display; `REL` portion coloured `#7eb3ff` |
| Separator | Thin vertical rule |
| Breadcrumb | Hierarchical path showing current wizard location; active step highlighted in `#93c5fd` |
| Mode Toggle | Right-aligned pill toggle switching between app modes (e.g. KB User / KB Manager) |
| User avatar | Right-aligned circular avatar |

### 3.2 Page Body

The main content area below the header is divided into:
- A **left sidebar** (fixed width) showing wizard step progress.
- A **main content panel** (flexible width) showing the active step content.

Both panels scroll independently; the sidebar remains sticky while content scrolls.

---

## 4. Wizard Steps

The mock-up defines a sequential, named-step wizard for the **Licence Workflow** (and likely the **Reuse Workflow**). Steps are shown in the left sidebar; the active step is highlighted.

### Step 1 — User Context

**Purpose:** Identify the user, their role, and institutional affiliation.

| Field / Element | Description |
| :---- | :---- |
| ORCID input | User enters or confirms their ORCID iD; triggers affiliation lookup |
| Name display | Resolved full name shown once ORCID is confirmed |
| Affiliation display | Institution name and verification badge (linked to `verifyInstitution` backend function) |
| Role selection | User selects their role in the current activity (e.g. creator, depositor, data steward) |

### Step 2 — Resource Identification

**Purpose:** Identify the research object or dataset being licensed or reused.

| Field / Element | Description |
| :---- | :---- |
| PID / URL input | User enters a persistent identifier (DOI, Handle, URL) |
| Resolve button | Triggers PID resolution via `resolvePid` backend function |
| Resource metadata display | Title, description, type, and source shown after resolution |
| Manual override | Allows manual entry if PID resolution fails |

### Step 3 — Checklist Evaluation

**Purpose:** Evaluate the resource against a configured checklist (e.g. FAIR, reproducibility).

| Field / Element | Description |
| :---- | :---- |
| Checklist selector | Dropdown or pill selector for available checklists (from `ChecklistSource` entities) |
| Checklist items | Rendered as cards or rows; each has a yes/no/N-A toggle |
| Status badges | Per-item colour-coded status: green (compliant), amber (review needed), red (non-compliant) |
| Progress indicator | Shows % of items evaluated |
| Notes field | Free-text notes per item |

### Step 4 — Intended Use / Reuse Context

**Purpose:** Capture the intended use of the resource and any constraints on reuse.

| Field / Element | Description |
| :---- | :---- |
| Use type selector | Multi-select for intended use categories (e.g. research, teaching, commercial) |
| Jurisdiction selector | Country/region picker (maps to `jurisdiction` field on Policy) |
| Data sensitivity | Toggle for personal data / special categories |
| Ethical considerations | Freetext or structured input for ethics notes |

### Step 5 — Policy Composition

**Purpose:** Select or compose a policy from the knowledge base that fits the identified context.

| Field / Element | Description |
| :---- | :---- |
| Recommended policies panel | List of auto-matched policies based on steps 1–4 context |
| Policy card | Expandable card showing ODRL type, permissions, prohibitions, duties |
| Select policy button | Marks a policy as selected for this workflow |
| Compose custom option | Option to open the KB Compose editor to build a bespoke policy |

### Step 6 — Review & Submit

**Purpose:** Final review of all collected context data and selected policy before submission.

| Field / Element | Description |
| :---- | :---- |
| Summary panel | Read-only display of all step data collected |
| Provenance block | ORCID, timestamp, workflow ID |
| Download JSON button | Export the assembled policy + context as a JSON-LD file |
| Submit PR button | Triggers `submitPolicyPR` backend function to create a GitHub Pull Request |
| Edit step links | Inline links to jump back to any previous step for correction |

---

## 5. UI Components

### 5.1 Status Badges

Four semantic badge variants are defined:

| Variant | Text colour | Background | Border | Use |
| :---- | :---- | :---- | :---- | :---- |
| Success | `--green` | `--glight` | `--gbord` | Compliant / approved |
| Warning | `--orange` | `--olight` | `--obord` | Review needed / partial |
| Error | `--red` | `--rlight` | `--rbord` | Non-compliant / blocked |
| Info/Purple | `--purple` | `--plight` | `--pbord` | Informational / pending |

### 5.2 Step Progress Sidebar

- Vertical list of numbered steps.
- Completed steps show a tick icon with `--green` colouring.
- Active step highlighted with `--accent` border and bold label.
- Future steps shown in `--muted`.
- Clicking a completed step navigates back (non-destructive).

### 5.3 Policy Cards (in Step 5)

Inherits from the existing `PolicyCard` component pattern but adapted to the light theme:
- Expandable/collapsible.
- Shows ODRL type badge, status badge, and rule summary (permissions / prohibitions / duties).
- A prominent "Select" action button.

### 5.4 Form Fields

- Input fields use a bordered, light-background style consistent with `--border` / `--ice`.
- Labels above inputs in `--muted`.
- Error states use `--red` border + inline message.
- Focus ring in `--accent`.

---

## 6. Behavioural Notes

| Behaviour | Description |
| :---- | :---- |
| Step validation | Each step validates before advancing; errors shown inline, navigation blocked until resolved |
| State persistence | Wizard state must be persisted across page navigations; current `WorkflowInstance.step_data` entity field supports this |
| Back navigation | Users can freely navigate back to completed steps without data loss |
| Sticky header | Header remains fixed at top of viewport at all times |
| Responsive layout | The sidebar collapses on mobile; steps accessible via a hamburger or step-count indicator |
| Mode toggle | Header mode toggle allows switching between KB User and KB Manager contexts without losing wizard state |
| Loading states | PID resolution, ORCID lookup, and checklist fetching all show spinner/skeleton states |

---

## 7. Mapping to Existing KB User Workflows

The mock-up wizard maps to the existing `KBWorkflow` page and its associated step components as follows:

| Mock-up Step | Existing Component | Status |
| :---- | :---- | :---- |
| Step 1 — User Context | `WorkflowStep1UserContext` | Exists — may need UI refresh |
| Step 2 — Resource Identification | `WorkflowStep2Resource` / `WorkflowStep2FindResource` | Exists — may need consolidation |
| Step 3 — Checklist Evaluation | `WorkflowStep3ChecklistSelection` / `WorkflowStep3ExamineContent` | Exists — needs review against mock-up |
| Step 4 — Intended Use | `WorkflowStep3IntendedUse` | Exists (step numbering differs) |
| Step 5 — Policy Composition | `WorkflowStep4Review` | Partial — policy selection UI not fully implemented |
| Step 6 — Review & Submit | `WorkflowStep5Generate` | Exists — may need provenance + PR submission additions |

> **Note:** There is a numbering mismatch between the mock-up steps and existing component names. Integration should align on a canonical step numbering scheme.

---

## 8. Open Questions for Integration

| # | Question | Owner |
| :---- | :---- | :---- |
| 1 | Should the mock-up's light-mode theme be adopted app-wide, or only for the wizard? | W Hugo |
| 2 | Should `DM Serif Display` / `DM Sans` replace `Inter` globally, or coexist? | W Hugo |
| 3 | Is Step 4 (Intended Use) a standalone step or merged with Step 3 (Checklist)? | W Hugo |
| 4 | Should the wizard support both Licence and Reuse workflow types within the same step shell, or remain separate? | W Hugo |
| 5 | What is the exact data schema for the Step 6 JSON-LD export? | W Hugo |
| 6 | Should the sidebar step navigator be a new shared component, or extend the existing workflow panel? | W Hugo |
