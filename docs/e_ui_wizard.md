# Annex E — Policy Wizard UI Specification

| Summary | UI design and behavioural specification for the OpenREL Policy Wizard, derived from a full analysis of `data/input/v0.4/OpenREL_Wizard_mock.html` including all HTML, CSS, and JavaScript |
| :---- | :---- |
| **Status** | Draft |
| **Version** | 0.2 |
| **Date** | 2026-06-16 |
| **Author** | W Hugo |
| **Source** | `data/input/v0.4/OpenREL_Wizard_mock.html` (143 719 bytes) |

---

## Table of Contents
- [1. Purpose and Scope](#1-purpose-and-scope)
- [2. Design System](#2-design-system)
- [3. Global Layout](#3-global-layout)
- [4. Application Views](#4-application-views)
- [5. View 1 — Template Browser](#5-view-1--template-browser)
- [6. View 2 — Simple Wizard](#6-view-2--simple-wizard)
- [7. View 3 — Advanced Wizard](#7-view-3--advanced-wizard)
- [8. Shared: Policy Preview Modal](#8-shared-policy-preview-modal)
- [9. JavaScript State Model](#9-javascript-state-model)
- [10. Constraint Catalogue](#10-constraint-catalogue)
- [11. Action Catalogue](#11-action-catalogue)
- [12. Open Questions](#12-open-questions)

---

## 1. Purpose and Scope

This document is a faithful specification of the Policy Wizard mock-up located at `data/input/v0.4/OpenREL_Wizard_mock.html`. It describes the structure, interaction logic, and data model of the mock-up **as it was designed**, derived directly from the HTML markup and JavaScript source — without reference to the existing OpenREL KB User codebase.

The mock-up is a standalone, self-contained single-page HTML application. It does not connect to a backend. Its purpose is to demonstrate the intended end-user experience for composing and selecting ODRL-based data access policies.

---

## 2. Design System

### 2.1 Colour Tokens

| CSS Variable | Value | Semantic Role |
| :---- | :---- | :---- |
| `--navy` | `#0f2040` | Primary brand background (header, sidebar) |
| `--blue` | `#1a4a8a` | Secondary blue |
| `--mid` | `#2563c4` | Mid interactive |
| `--accent` | `#3b82f6` | Active highlights, links, IRI labels |
| `--pale` | `#eff6ff` | Light blue panel tones |
| `--ice` | `#f0f7ff` | Card / row backgrounds |
| `--border` | `#c7d9f5` | Default border |
| `--text` | `#0f2040` | Primary body text |
| `--muted` | `#5a7296` | Secondary / helper text |
| `--white` | `#ffffff` | Surface white |
| `--green` | `#065f46` | Success / Licence / Permission |
| `--glight` | `#ecfdf5` | Success badge background |
| `--gbord` | `#6ee7b7` | Success badge border |
| `--orange` | `#92400e` | Warning / Obligation |
| `--olight` | `#fffbeb` | Warning badge background |
| `--obord` | `#fcd34d` | Warning badge border |
| `--red` | `#991b1b` | Error / Prohibition |
| `--rlight` | `#fef2f2` | Prohibition badge background |
| `--rbord` | `#fca5a5` | Prohibition badge border |
| `--purple` | `#5b21b6` | Informational / Access policy type |
| `--plight` | `#f5f3ff` | Info badge background |
| `--pbord` | `#c4b5fd` | Info badge border |

> **Note:** This is a **light-mode** design. The existing OpenREL app uses a dark-mode Tailwind theme. Integration will require a decision on theme alignment.

### 2.2 Typography

| Role | Font Family | Weights |
| :---- | :---- | :---- |
| Display / Headings | `DM Serif Display` (Google Fonts) | Regular, Italic |
| Body / UI chrome | `DM Sans` | 300, 400, 500, 600 |
| Code / IRIs / IDs | `DM Mono` | 400, 500 |

> A fallback to `Inter` is referenced in tooltip elements, indicating mixed font usage.

### 2.3 Layout Constants

| Property | Value |
| :---- | :---- |
| Body background | `#f4f7fc` |
| Card border radius | `10px` |
| Card shadow | `0 4px 24px rgba(15,32,64,0.10)` |
| Header height | `60px` |

---

## 3. Global Layout

### 3.1 Header

A sticky navigation bar (height `60px`, `z-index: 200`) rendered on `--navy`.

| Element | Behaviour |
| :---- | :---- |
| Logo | `Open` + `REL` (REL in `#7eb3ff`), DM Serif Display. Clicking navigates to the Template Browser. |
| Separator | Thin vertical rule (`rgba(255,255,255,0.2)`) |
| Breadcrumb (`#hcrumb`) | Shows current view path. In browser: just "Template Browser". In a wizard: "Template Browser › Simple/Advanced Wizard" with the first segment as a back-link. |
| Mode toggle (browser only, `#hright-browser`) | Button group: **Simple Wizard** and **Advanced Wizard**. Clicking either starts the corresponding wizard from scratch via `startFromScratch()`. |
| Wizard mode toggle (`#hright-wizard`) | Shown only when a wizard is active. Pill-style toggle between `mbtn-simple` and `mbtn-advanced`. Switching mode calls `switchMode(v)` which resets all state. |
| User avatar | Right-aligned circular avatar placeholder. |

### 3.2 Three-View Architecture

The app switches between three top-level `<div>` views via `showView(v)`:

| `v` | Element ID | Description |
| :---- | :---- | :---- |
| `'browser'` | `#view-browser` | Template Browser (start screen) |
| `'simple'` | `#view-simple` | Simple 4-question wizard |
| `'advanced'` | `#view-advanced` | Advanced full ODRL editor |

Only one view is visible at a time; the others have the `hidden` class.

---

## 4. Application Views

The three views are independent layouts. The Simple and Advanced wizards share no sub-components with the Template Browser.

| View | Layout | Primary CTA |
| :---- | :---- | :---- |
| Template Browser | Card grid + left filter panel | "Open in Simple Wizard" / "Open in Advanced Wizard" per template card |
| Simple Wizard | Single narrow column, step-by-step question cards | "Next" / "Back" navigation; final step renders the output |
| Advanced Wizard | Two-column: sidebar checklist + main panel sections | Section-by-section form; live-updating policy preview panel |

---

## 5. View 1 — Template Browser

### 5.1 Purpose

The entry point. Displays all available policy templates and allows the user to filter them before choosing a starting point for the Simple or Advanced wizard.

### 5.2 Layout

- **Left filter panel:** Collapsible facets for Policy Type (Licence / Access), Status, and Tags.
- **Main area:** Responsive card grid. Each card is a template entry.

### 5.3 Template Card

Each card shows:

| Field | Source |
| :---- | :---- |
| Title | `tpl.label` |
| Policy type badge | `tpl.type` — green for `Licence`, purple for `Access` |
| Status badge | `tpl.status` — e.g. `draft`, `review`, `active` |
| Short description | `tpl.desc` |
| Permissions summary | Action IDs from `tpl.perms`, resolved to labels |
| Prohibitions summary | Action IDs from `tpl.prohs`, resolved to labels |
| Constraints summary | Constraint IDs from `tpl.cons`, resolved to labels |
| Fingerprint | Hash of the canonical policy, shown as a short hex string |
| Tags | Array of string tags |

Two action buttons per card:
- **Open in Simple Wizard** — calls `loadTplSimple(tpl)`, pre-populates Simple wizard state from the template's canonical mapping.
- **Open in Advanced Wizard** — calls `loadTplAdvanced(tpl)`, pre-populates Advanced wizard state directly.

### 5.4 Filtering

Client-side filter on `tpl.type` and `tpl.status`. No server calls.

---

## 6. View 2 — Simple Wizard

### 6.1 Purpose

A guided 4-question wizard for non-expert users. Questions are framed in plain language. The answers map deterministically to a canonical ODRL policy structure via `simpleToCanonical()`.

### 6.2 Simple State Object (`SS`)

The wizard's in-memory state is held in a JavaScript object:

```js
const SS = {
  q1: 'public',       // Who can access?
  q2: { share: false, modify: false, commercial: false }, // What can they do?
  q3: 'unrestricted', // Where can they access from?
  geoInc: [],         // Included countries (when q3 = 'restricted')
  geoExc: [],         // Excluded countries (when q3 = 'restricted')
  q4: 'unlimited',    // When / for how long?
  dateStart: '',
  dateEnd: '',
  tplId: null         // Source template ID if loaded from browser
};
```

### 6.3 Step Navigation

Steps are rendered as separate `<div>` panels (`#sq1` through `#sq4` and `#sq5`). Navigation is via `sGoTo(n)`. Each step is hidden/shown by toggling the `hidden` class.

| Step Panel | ID | Question |
| :---- | :---- | :---- |
| 1 | `#sq1` | **Who** can access this resource? |
| 2 | `#sq2` | **What** can they do with it? |
| 3 | `#sq3` | **Where** — any geographic restriction? |
| 4 | `#sq4` | **When** — any time limit? |
| 5 | `#sq5` | **Result** — generated policy output |

### 6.4 Step 1 — Who?

**Question:** "Who can access this resource?"

Four radio options (single-select). Each sets `SS.q1`:

| Value | Label | Policy type output |
| :---- | :---- | :---- |
| `public` | **Anyone** — No restrictions, publicly accessible | `Licence` |
| `noncommercial` | **Non-commercial users** — Free for research & education, not for profit | `Licence` |
| `researchers` | **Verified researchers** — Institutional affiliations required | `Access` |
| `managed` | **Managed access** — Specific organisations or users only | `Access` |

### 6.5 Step 2 — What?

**Question:** "What can they do with it?"

Three independent checkboxes. Each sets a boolean in `SS.q2`:

| Checkbox | `SS.q2` key | Action IDs affected |
| :---- | :---- | :---- |
| Share or redistribute | `share` | `A03` (permitted if checked, prohibited if not) |
| Modify or create derivatives | `modify` | `A04` (permitted if checked, prohibited if not) |
| Use commercially | `commercial` | `A01` (permitted if checked) |

> `A02` (read) and `A05` (reproduce) are **always** added to permissions regardless of these checkboxes.

### 6.6 Step 3 — Where?

**Question:** "Any geographic restriction?"

Two radio options (single-select). Sets `SS.q3`:

| Value | Label | Constraint output |
| :---- | :---- | :---- |
| `unrestricted` | **No restrictions** — available worldwide | No spatial constraint (`C13` not added) |
| `restricted` | **Restrict to specific countries** | `C13` (`odrl:spatial`) added with include/exclude country lists |

When `restricted` is selected, a geo-picker is revealed (`#s-geo-picker`) consisting of two searchable country lists:
- **Include (✓):** Countries where access IS permitted. Populates `SS.geoInc`.
- **Exclude (✕):** Countries where access is NOT permitted. Populates `SS.geoExc`.

An ODRL hint is shown when both include and exclude lists are non-empty: `odrl:LogicalConstraint odrl:and`.

### 6.7 Step 4 — When?

**Question:** "Any time limit?"

Two radio options (single-select). Sets `SS.q4`:

| Value | Label | Constraint output |
| :---- | :---- | :---- |
| `unlimited` | **No time limit** — policy remains valid indefinitely | No time constraint |
| `fixed` | **Available for a fixed period** — set a start and end date | `C15` (Time Interval) added with `SS.dateStart` / `SS.dateEnd` |

When `fixed` is selected, a date-range picker is revealed with two date inputs (Start date, End date).

### 6.8 Step 5 — Result

The final panel calls `sFinish()`, which:
1. Calls `simpleToCanonical(SS.q1, SS.q2, SS.q3, SS.geoInc, SS.geoExc, SS.q4, SS.dateStart, SS.dateEnd)` to compute the canonical policy object.
2. Renders the policy using `renderPolicy(policy)` into `#sq5-out`.
3. Shows the full ODRL JSON in `#sq5-json`.
4. Shows a "Switch to Advanced" button (calls `switchMode('advanced')`) for further editing.
5. Shows a "Copy JSON" button.
6. Shows a "Download JSON" button (triggers a blob download).

---

## 7. View 3 — Advanced Wizard

### 7.1 Purpose

A full-featured ODRL policy editor for expert users. It exposes the complete policy data model in a structured form and provides a live-updating preview panel.

### 7.2 Advanced State Object (`AS`)

```js
const AS = {
  policyType: null,          // 'Licence' | 'Access'
  meta: {
    title: '',
    slug: '',
    desc: '',
    issuer: '',
    status: 'draft',
    asset: '',
    pid: ''
  },
  perms: [],                 // Array of action IDs permitted
  prohs: [],                 // Array of action IDs prohibited
  oblis: {},                 // Object: actionId -> obligation type
  cons: {},                  // Object: constraintId -> value or true
  conflictTerm: 'odrl:prohibit',
  agents: {
    assigner: '',
    assigneeType: 'public',  // 'public' | 'org' | 'person'
    assigneeURI: ''
  },
  tplId: null
};
```

### 7.3 Layout

The Advanced wizard is a two-column layout:

- **Left sidebar (sticky):** A numbered checklist of sections. Active section is highlighted. Completed sections show a tick. Clicking a section scrolls to it.
- **Right main panel:** Stacked section cards, each containing a form. A **live policy preview panel** is pinned at the right side (or bottom) and updates on every user interaction via `renderAdvancedPreview()`.

### 7.4 Sections

The Advanced wizard is divided into the following named sections:

#### Section 1 — Policy Type

Two large radio cards (single-select). Sets `AS.policyType`:

| Value | Label | Description | ODRL type mapping |
| :---- | :---- | :---- | :---- |
| `Licence` | **Licence** | Grants usage rights; anyone can discover the terms | `odrl:Set` |
| `Access` | **Access Policy** | Controls access; defines who can request access | `odrl:Offer` |

#### Section 2 — Policy Metadata

Freetext form fields populating `AS.meta`:

| Field | Key | Notes |
| :---- | :---- | :---- |
| Policy title | `meta.title` | Display name |
| Slug / ID | `meta.slug` | Auto-generated from title (slugified); editable |
| Description | `meta.desc` | Short description |
| Issuer | `meta.issuer` | Organisation or person URI |
| Status | `meta.status` | Dropdown: `draft`, `review`, `active`, `deprecated` |
| Asset URI | `meta.asset` | URI of the resource this policy covers |
| PID | `meta.pid` | Persistent identifier (DOI, Handle, etc.) |

#### Section 3 — Permissions

A multi-select action picker from the Action Catalogue (see §11). Each selected action ID is pushed to `AS.perms`. Actions that overlap with `AS.prohs` are flagged as conflicts.

#### Section 4 — Prohibitions

Same action picker, results stored in `AS.prohs`. Overlap with `AS.perms` is flagged.

#### Section 5 — Obligations

An obligation builder. Selected action IDs stored in `AS.oblis` with obligation type values (e.g. `'duty'`, `'remedy'`, `'consequence'`).

#### Section 6 — Constraints

A constraint picker from the Constraint Catalogue (see §10). Selected constraints stored in `AS.cons` keyed by constraint ID. Constraints with `param: true` prompt for a parameter value (URI, integer, date range, geo-picker, duration). A **logic hint** is shown when more than one constraint is selected: `odrl:LogicalConstraint odrl:and`.

**Constraint categories:**
- Identity & Trust
- Data Sensitivity
- Security Profile
- Geography & Time
- Usage Control
- Accountability
- Open Access & Attribution

#### Section 7 — Agents

Defines the parties involved:

| Field | Key | Options / Notes |
| :---- | :---- | :---- |
| Assigner (rights holder) | `agents.assigner` | URI freetext input |
| Assignee type | `agents.assigneeType` | Radio: `public` (no URI required) / `org` (organisation URI) / `person` (ORCID URI) |
| Assignee URI | `agents.assigneeURI` | Shown when type is `org` or `person` |

#### Section 8 — Conflict Term

A single dropdown or radio controlling how permission/prohibition conflicts are resolved. Sets `AS.conflictTerm`:

| Value | ODRL mapping |
| :---- | :---- |
| `odrl:prohibit` | Prohibition wins (default) |
| `odrl:permit` | Permission wins |
| `odrl:perm` | Permissive (alias) |

---

## 8. Shared: Policy Preview Modal

Both wizards share a modal (`#policy-modal`) that renders a full policy card. It is triggered by `openModal(tpl)` from the Template Browser or by the Advanced wizard's live preview.

The modal renders:
- Policy type and status badges
- Metadata (title, description, issuer, asset, PID)
- **Permissions** section: action rows with PERM badge, action label, IRI
- **Prohibitions** section: action rows with PROH badge, action label, IRI
- **Obligations** section: action rows with OBLI badge
- **Constraints** section: constraint rows (`C`-prefixed ID, label, info tooltip with plain-language description)
- **Parameters** section: parameter rows for constraints that require values
- Full ODRL JSON block (copyable)
- Fingerprint hash

---

## 9. JavaScript State Model

### 9.1 `simpleToCanonical(q1, q2, q3, geoInc, geoExc, q4, dateStart, dateEnd)`

Maps Simple wizard answers to a canonical policy structure:

```
q1 → policyType
  'public' | 'noncommercial' → 'Licence'
  'researchers' | 'managed'  → 'Access'

perms (always include A02, A05):
  q2.share       → add A03
  q2.modify      → add A04
  q2.commercial  → add A01

prohs:
  !q2.modify     → add A04
  !q2.share      → add A03

cons:
  q1 = 'noncommercial' → add C02 (Non-commercial use only)
  q1 = 'researchers'   → add C03 (Verified researcher affiliation) + C06 (Authentication required)
  q1 = 'managed'       → add C01 (Specific party required) + C06 (Authentication required)
  q3 = 'restricted'    → add C13 (Spatial) with inc/exc lists
  q4 = 'fixed'         → add C15 (Time Interval) with dateStart/dateEnd
```

> **Important note (from source comment):** `commercial = true` never adds `C02`; `C02` is only added for `q1 = 'noncommercial'`, regardless of the "Use commercially" checkbox.

### 9.2 `fp(policy)` — Fingerprint Function

Produces a deterministic 8-character hex fingerprint of a policy object (djb2 hash of a canonicalised JSON string). Used to:
- Detect duplicates in the template library.
- Match a Simple wizard output to an existing template.

### 9.3 `resetAll()` / `switchMode(v)`

- `resetAll()` resets both `SS` and `AS` to their initial values and navigates to the Template Browser.
- `switchMode(v)` switches between `'simple'` and `'advanced'`, resetting all state.

### 9.4 `loadTplSimple(tpl)` / `loadTplAdvanced(tpl)`

Pre-populate wizard state from a template object:
- `loadTplSimple`: reverse-maps the canonical template structure back into `SS.q1`–`q4` answers, then calls `showView('simple')`.
- `loadTplAdvanced`: copies template data directly into `AS`, then calls `showView('advanced')`.

---

## 10. Constraint Catalogue

All constraints are defined in the `CONSTRAINTS` array. There are 25 constraints (`C01`–`C25`) organised in 7 categories:

| Category | IDs | Description |
| :---- | :---- | :---- |
| **Identity & Trust** | C01–C06 | Party identification, affiliation, authentication, purpose |
| **Data Sensitivity** | C07–C08 | Personal data presence / special category data |
| **Security Profile** | C09–C12 | Security levels (TRUST+, TRUST, BASE), TOM, data minimisation |
| **Geography & Time** | C13–C15 | Spatial restriction (GeoNames), access duration, time interval |
| **Usage Control** | C16–C19 | Access count cap, revocation check, connector URI, volume limit |
| **Accountability** | C20–C21 | Notification endpoint, logging clearing house |
| **Open Access & Attribution** | C22–C25 | Open access mandate, attribution, share-alike, public funding |

### Constraint Detail

| ID | Label | IRI | Param? | Param type |
| :---- | :---- | :---- | :---- | :---- |
| C01 | Specific Party Required | `openrel:constraint.party:specific` | — | — |
| C02 | Non-commercial Use Only | `openrel:constraint.purpose:noncommercial` | — | — |
| C03 | Verified Researcher Affiliation | `openrel:constraint.party:verifiedResearcher` | — | — |
| C04 | Purpose: Research Only | `openrel:constraint.purpose:research` | — | — |
| C05 | Purpose: Education Only | `openrel:constraint.purpose:education` | — | — |
| C06 | Authentication Required | `openrel:constraint.identity:authenticated` | — | — |
| C07 | Personal Data Present | `openrel:constraint.dataClass:personal` | — | — |
| C08 | Special Category Data | `openrel:constraint.dataClass:specialCategory` | — | — |
| C09 | Security Profile: TRUST+ | `openrel:constraint.security:trustPlus` | — | — |
| C10 | Security Profile: TRUST | `openrel:constraint.security:trust` | — | — |
| C11 | Security Profile: BASE | `openrel:constraint.security:base` | — | — |
| C12 | TOM Required | `openrel:constraint.tom:required` | — | — |
| C13 | Data Minimisation | `openrel:constraint.dataMinimization` | — | — |
| C14 | Spatial (GeoNames) | `odrl:spatial` | ✓ | `geo` (include/exclude country lists) |
| C15 | Access Duration | `openrel:constraint.duration:accessDuration` | ✓ | `duration` (ISO 8601, e.g. `PT24H`) |
| C16 | Time Interval | `openrel:constraint.timeInterval:accessWindow` | ✓ | `daterange` (start + end date) |
| C17 | Access Count | `openrel:constraint.count:accessCount` | ✓ | `integer` (max count) |
| C18 | Revocation Status Active | `openrel:constraint.revocation:active` | — | — |
| C19 | Connector Auth URI | `openrel:constraint.connector:authorisedURI` | ✓ | `uri` |
| C20 | Data Volume Limit (MiB) | `openrel:constraint.volume:maxVolume` | ✓ | `integer` (max MiB) |
| C21 | Notification Endpoint | `openrel:constraint.accountability:notifyEndpoint` | ✓ | `uri` |
| C22 | Logging Clearing House | `openrel:constraint.accountability:loggingCH` | ✓ | `uri` |
| C23 | Open Access | `openrel:constraint.openAccess` | — | — |
| C24 | Attribution Required | `openrel:constraint.attribution:required` | — | — |
| C25 | Share-Alike | `openrel:constraint.shareAlike` | — | — |

> **Note from source:** The CONSTRAINTS array in the mock-up lists C01–C25, but the catalogue section order means C13 appears as "Spatial (GeoNames)" under Geography & Time, while C12 in the Security category is actually "Data Minimisation". The IDs in the table above preserve the source array ordering.

---

## 11. Action Catalogue

Actions are defined in the `ACTIONS` array with the following fields: `id`, `label`, `iri`, `cat` (category).

| ID | Label | IRI | Category |
| :---- | :---- | :---- | :---- |
| A01 | Commercial Use | `odrl:commercialUse` | Usage |
| A02 | Read / View | `odrl:read` | Usage |
| A03 | Share / Redistribute | `odrl:distribute` | Usage |
| A04 | Modify / Derive | `odrl:modify` | Usage |
| A05 | Reproduce | `odrl:reproduce` | Usage |
| A06 | Archive | `odrl:archive` | Usage |
| A07 | Print | `odrl:print` | Usage |
| A08 | Annotate | `odrl:annotate` | Usage |
| A09 | Index (search engine) | `odrl:index` | Usage |
| A10 | Extract | `odrl:extract` | Data Operations |
| A11 | Aggregate | `odrl:aggregate` | Data Operations |
| A12 | Anonymise | `openrel:action.anonymise` | Data Operations |
| A13 | Translate | `odrl:translate` | Content |
| A14 | Present | `odrl:present` | Content |
| A15 | Inform (notify) | `odrl:inform` | Obligation |
| A16 | Attribute | `odrl:attribute` | Obligation |
| A17 | Delete after use | `openrel:action.deleteAfterUse` | Obligation |
| A18 | Report to clearing house | `openrel:action.reportToCH` | Obligation |

---

## 12. Open Questions

| # | Question |
| :---- | :---- |
| 1 | Should the wizard adopt the mock-up’s light-mode palette, or be adapted to the existing dark-mode theme? |
| 2 | The mock-up is entirely standalone (no backend calls). Which steps should trigger live backend calls (e.g. PID resolution, ORCID lookup) in the integrated version? |
| 3 | The Simple wizard’s reverse-mapping from canonical policy → Q1–Q4 answers is not fully specified for all edge cases. How should ambiguous templates be handled when loaded into Simple mode? |
| 4 | The constraint numbering (C01–C25) is internal to the mock-up. Should these IDs be retained in the implementation, or should the IRI-based identifiers be used as primary keys? |
| 5 | Should the Advanced wizard’s live preview replace the existing `ComposePolicyCard` component, or coexist with it? |
| 6 | The `fp()` fingerprint function uses djb2 hashing. Should this be reproduced identically in the implementation to allow template matching, or replaced with a formal content-addressable hash? |
