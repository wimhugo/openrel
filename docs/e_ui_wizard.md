# Annex E — Policy Wizard UI Specification

| Summary | UI design and behavioural specification for the OpenREL Policy Wizard, derived from a full analysis of `data/input/v0.4/OpenREL_Wizard_mock.html` including all HTML, CSS, and JavaScript |
| :---- | :---- |
| **Status** | Draft |
| **Version** | 0.3 |
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
- [9. JavaScript Function Reference](#9-javascript-function-reference)
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
- **Exclude (✗):** Countries where access is NOT permitted. Populates `SS.geoExc`.

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

## 9. JavaScript Function Reference

This section documents all significant JavaScript functions in the mock-up, grouped by concern. Where the source code is non-trivial, the exact implementation is shown and annotated.

---

### 9.1 View Routing

#### `showView(v)`

The central view router. Switches the application between its three top-level views by toggling the CSS `hidden` class.

```js
function showView(v) {
  // Hide all three root view divs
  ['browser','simple','advanced'].forEach(id => {
    document.getElementById('view-' + id).classList.toggle('hidden', id !== v);
  });
  // Swap header controls: breadcrumb mode toggle
  document.getElementById('hright-browser').classList.toggle('hidden', v !== 'browser');
  document.getElementById('hright-wizard').classList.toggle('hidden',  v === 'browser');
  // Update breadcrumb text
  updCrumb(v);
}
```

**Notes:**
- No history/routing is used. The URL does not change between views.
- `updCrumb(v)` updates `#hcrumb` to show `"Template Browser"` in browser mode, or `"Template Browser › [Simple|Advanced] Wizard"` in wizard modes, with the first segment rendered as a back-link that calls `showView('browser')`.

---

#### `startFromScratch(mode)`

Called by the header **Simple Wizard** / **Advanced Wizard** buttons in the Template Browser.

```js
function startFromScratch(mode) {
  resetAll();       // zero all SS and AS state
  showView(mode);   // navigate to 'simple' or 'advanced'
  if (mode === 'simple') sGoTo(1);  // jump to step 1
}
```

---

#### `switchMode(v)`

Called by the in-wizard mode toggle pill. Switches between Simple and Advanced **and resets all state**.

```js
function switchMode(v) {
  resetAll();
  showView(v);
  if (v === 'simple') sGoTo(1);
}
```

**Important:** Switching modes discards all current wizard answers. There is no state transfer between modes (except when explicitly loaded via `loadTplSimple` / `loadTplAdvanced`).

---

### 9.2 Simple Wizard Navigation

#### `sGoTo(n)`

Navigates the Simple wizard to step `n` (1–5).

```js
function sGoTo(n) {
  [1,2,3,4,5].forEach(i => {
    document.getElementById('sq' + i).classList.toggle('hidden', i !== n);
  });
  // Update step indicator dots
  updStepDots(n);
  // On step 5 (Result), trigger output rendering
  if (n === 5) sFinish();
}
```

- Step dots are small circular indicators shown above the wizard card; the active step is filled, completed steps are half-filled.
- Calling `sGoTo(5)` automatically triggers `sFinish()`, so output is always regenerated when the result step is entered.

---

#### `sFinish()`

Computes and renders the final policy output for the Simple wizard.

```js
function sFinish() {
  const policy = simpleToCanonical(
    SS.q1, SS.q2, SS.q3, SS.geoInc, SS.geoExc, SS.q4, SS.dateStart, SS.dateEnd
  );
  document.getElementById('sq5-out').innerHTML  = renderPolicy(policy);
  document.getElementById('sq5-json').textContent = JSON.stringify(toODRL(policy), null, 2);
  // Show/hide the fingerprint match banner
  const match = TEMPLATES.find(t => fp(t) === fp(policy));
  const banner = document.getElementById('s-match-banner');
  if (match) {
    banner.classList.remove('hidden');
    banner.querySelector('.match-label').textContent = match.label;
  } else {
    banner.classList.add('hidden');
  }
}
```

**Notes:**
- `toODRL(policy)` converts the internal canonical structure to a standards-compliant ODRL JSON-LD object.
- If the computed policy's fingerprint matches a known template, a banner is shown: *"This matches the '[Template Name]' template."*

---

### 9.3 Fingerprinting

#### `fp(policy)` — Policy Fingerprint

This is the most algorithmically significant function in the mock-up. It produces a deterministic, order-independent 8-character hexadecimal fingerprint of a policy object.

**Source code (exact):**

```js
function fp(policy) {
  const str = JSON.stringify({
    t:  policy.type || '',
    p:  [...(policy.perms || [])].sort(),
    pr: [...(policy.prohs || [])].sort(),
    ob: Object.keys(policy.oblis || {}).sort().map(k => k + ':' + policy.oblis[k]),
    co: Object.keys(policy.cons  || {}).sort().map(k => {
      const v = policy.cons[k];
      if (v === true)                     return k;
      if (typeof v === 'string' && v !== '') return k + '=' + v;
      if (v && typeof v === 'object') {
        if (Array.isArray(v.inc) || Array.isArray(v.exc)) {
          const inc = (v.inc || []).map(x => x.iso || x).sort().join(',');
          const exc = (v.exc || []).map(x => x.iso || x).sort().join(',');
          return k + '=' + inc + '|' + exc;
        }
        if (v.from !== undefined) return k + '=' + v.from + '>' + v.to;
        return k + '=' + JSON.stringify(v);
      }
      return k;
    })
  });
  let h = 5381;
  for (let i = 0; i < str.length; i++) h = ((h << 5) + h) ^ str.charCodeAt(i);
  return (h >>> 0).toString(16).padStart(8, '0');
}
```

**Step-by-step breakdown:**

**Step 1 — Canonical serialisation**

A normalised JavaScript object is constructed with five keys:

| Key | Source | Normalisation applied |
| :---- | :---- | :---- |
| `t` | `policy.type` | Lowercased string; empty string if absent |
| `p` | `policy.perms` | Array of action IDs, **sorted alphabetically** |
| `pr` | `policy.prohs` | Array of action IDs, **sorted alphabetically** |
| `ob` | `policy.oblis` | Object entries serialised as `"actionId:obligationType"`, **sorted by key** |
| `co` | `policy.cons` | Object entries serialised per constraint value type (see below), **sorted by key** |

The sorting is critical: it ensures that `["A02", "A05"]` and `["A05", "A02"]` produce the same fingerprint.

**Step 2 — Constraint value serialisation (the `co` field)**

Each entry in `policy.cons` is serialised to a string using type-dispatch:

| Constraint value type | Serialisation format | Example |
| :---- | :---- | :---- |
| `true` (boolean flag) | `"constraintId"` | `"C02"` |
| Non-empty string | `"constraintId=value"` | `"C14=PT24H"` |
| Object with `inc`/`exc` arrays (geo) | `"constraintId=isoList\|isoList"` | `"C13=DE,FR\|CN,RU"` |
| Object with `from`/`to` (date range) | `"constraintId=start>end"` | `"C15=2024-01-01>2024-12-31"` |
| Other object | `"constraintId=" + JSON.stringify(value)` | fallback |

For geo constraints, ISO codes are extracted from `{ iso, label, flag }` objects (or taken as-is if already a string), then sorted — ensuring that `[DE, FR]` and `[FR, DE]` produce the same hash.

**Step 3 — djb2 Hash**

The normalised object is serialised with `JSON.stringify` (key order is deterministic because the object is constructed with fixed key names), then hashed using the **djb2** algorithm:

```
initial hash:  h = 5381
per character: h = ((h << 5) + h) XOR charCode
             = h * 33 XOR charCode
```

The final value is converted to an unsigned 32-bit integer via `>>> 0`, then rendered as an 8-character, zero-padded lowercase hexadecimal string.

**Properties and implications:**

| Property | Detail |
| :---- | :---- |
| **Algorithm** | djb2 (Daniel J. Bernstein, 1990s) — fast, non-cryptographic |
| **Output** | 8 hex characters (32-bit unsigned integer), e.g. `"a3f8c1d2"` |
| **Collision resistance** | Low — 2³² possible values (~4.3 billion). Suitable for UI duplicate detection, not security. |
| **Order-independence** | Yes — arrays are sorted before hashing; geo ISO lists are sorted. |
| **Parameter-sensitivity** | Yes — two policies differing only in a constraint parameter value produce different fingerprints. |
| **Type-sensitivity** | Yes — `C02 = true` vs `C02 = "true"` produce different serialisations and thus different hashes. |

**Use cases in the mock-up:**
1. **Template deduplication** — the Template Browser can detect if two templates are semantically identical.
2. **Simple wizard match banner** — after completing the Simple wizard, `sFinish()` calls `TEMPLATES.find(t => fp(t) === fp(policy))`. If a match is found, a banner tells the user their selections correspond to an existing named template.
3. **Template card display** — each template card in the browser shows its own fingerprint as a short identifier in a monospace badge.

**Reproduction note:** To reproduce this function identically in an implementation, the input `policy` object must use the same internal structure (`perms`, `prohs`, `oblis`, `cons`, `type`). If the implementation uses different field names (e.g. `permissions` instead of `perms`) the fingerprint will not match the mock-up's.

---

### 9.4 Policy Mapping

#### `simpleToCanonical(q1, q2, q3, geoInc, geoExc, q4, dateStart, dateEnd)`

Maps Simple wizard answers to a canonical internal policy structure. This is the core business logic of the Simple wizard.

**Source code (exact):**

```js
function simpleToCanonical(q1, q2, q3, geoInc, geoExc, q4, dateStart, dateEnd) {
  const type = { public:'Licence', noncommercial:'Licence',
                 researchers:'Access', managed:'Access' }[q1] || 'Licence';
  // permissions — always read + reproduce; add others when selected
  const perms = ['A02', 'A05'];
  if (q2.share)      perms.push('A03');
  if (q2.modify)     perms.push('A04');
  if (q2.commercial) perms.push('A01');
  // prohibitions — only what is explicitly prohibited
  const prohs = [];
  if (!q2.modify) prohs.push('A04');
  if (!q2.share)  prohs.push('A03');
  // constraints
  const cons = {};
  if (q1 === 'noncommercial') { cons['C02'] = true; }
  if (q1 === 'researchers')   { cons['C03'] = true; cons['C06'] = true; }
  if (q1 === 'managed')       { cons['C01'] = true; cons['C06'] = true; }
  if (q3 === 'restricted')    { cons['C13'] = { inc: geoInc, exc: geoExc }; }
  if (q4 === 'fixed')         { cons['C15'] = { from: dateStart, to: dateEnd }; }
  return { type, perms, prohs, oblis: {}, cons };
}
```

**Mapping table:**

| Input | Output field | Logic |
| :---- | :---- | :---- |
| `q1 = 'public'` | `type = 'Licence'` | No extra constraints |
| `q1 = 'noncommercial'` | `type = 'Licence'`, `cons.C02 = true` | Adds non-commercial constraint |
| `q1 = 'researchers'` | `type = 'Access'`, `cons.C03 = true`, `cons.C06 = true` | Requires verified researcher + authentication |
| `q1 = 'managed'` | `type = 'Access'`, `cons.C01 = true`, `cons.C06 = true` | Requires specific party + authentication |
| `q2.share = true` | `A03` in `perms` | Otherwise `A03` in `prohs` |
| `q2.modify = true` | `A04` in `perms` | Otherwise `A04` in `prohs` |
| `q2.commercial = true` | `A01` in `perms` | No prohibition added if false |
| `q3 = 'restricted'` | `cons.C13 = { inc, exc }` | Geographic constraint with country lists |
| `q4 = 'fixed'` | `cons.C15 = { from, to }` | Time interval constraint |
| Always | `A02`, `A05` in `perms` | Read and reproduce always permitted |

> **Design note (from source comment):** `commercial = true` never adds `C02`; `C02` is added only for `q1 = 'noncommercial'`, regardless of the commercial checkbox state. The commercial checkbox is purely additive (adds `A01` to permissions); it never produces a prohibition.

---

#### `toODRL(policy)`

Converts the internal canonical policy structure to a standards-compliant ODRL 2.2 JSON-LD document.

**Behaviour:**
- Maps `type = 'Licence'` → `@type: "odrl:Set"`; `type = 'Access'` → `@type: "odrl:Offer"`.
- Constructs `odrl:permission`, `odrl:prohibition`, and `odrl:duty` arrays.
- Each action entry includes `odrl:action` (the action IRI from the Action Catalogue) and an `odrl:constraint` array (constraint entries from the Constraint Catalogue IRIs).
- Geo constraints (`C13`) are serialised as `odrl:spatial` with a `odrl:LogicalConstraint` wrapping include and exclude sets when both are non-empty.
- The output includes `@context`, `@type`, `uid`, `profile`, `permission`, `prohibition`, and `obligation` fields.

---

### 9.5 Template Loading

#### `loadTplSimple(tpl)`

Loads a template from the Template Browser into the Simple wizard by reverse-mapping the canonical structure back to Q1–Q4 answers.

```js
function loadTplSimple(tpl) {
  resetAll();
  SS.tplId = tpl.id;
  // Reverse-map type
  if      (tpl.cons['C03']) SS.q1 = 'researchers';
  else if (tpl.cons['C01']) SS.q1 = 'managed';
  else if (tpl.cons['C02']) SS.q1 = 'noncommercial';
  else                      SS.q1 = 'public';
  // Reverse-map What checkboxes
  SS.q2.share      = tpl.perms.includes('A03');
  SS.q2.modify     = tpl.perms.includes('A04');
  SS.q2.commercial = tpl.perms.includes('A01');
  // Reverse-map Where
  if (tpl.cons['C13']) {
    SS.q3    = 'restricted';
    SS.geoInc = tpl.cons['C13'].inc || [];
    SS.geoExc = tpl.cons['C13'].exc || [];
  }
  // Reverse-map When
  if (tpl.cons['C15']) {
    SS.q4       = 'fixed';
    SS.dateStart = tpl.cons['C15'].from || '';
    SS.dateEnd   = tpl.cons['C15'].to   || '';
  }
  showView('simple');
  sGoTo(1);
}
```

**Limitation:** The reverse-mapping is lossy. Templates with constraints that have no Q1–Q4 counterpart (e.g. `C04` Purpose: Research, `C07` Personal Data Present) are silently dropped. The Simple wizard can only represent a subset of the full policy space.

---

#### `loadTplAdvanced(tpl)`

Loads a template directly into the Advanced wizard state object with no lossy conversion.

```js
function loadTplAdvanced(tpl) {
  resetAll();
  AS.tplId      = tpl.id;
  AS.policyType = tpl.type;
  AS.perms      = [...tpl.perms];
  AS.prohs      = [...tpl.prohs];
  AS.oblis      = { ...tpl.oblis };
  AS.cons       = { ...tpl.cons  };
  if (tpl.meta) Object.assign(AS.meta, tpl.meta);
  showView('advanced');
  renderAdvancedPreview();
}
```

---

### 9.6 Slug Generation

#### `updSlug(pfx)`

Auto-generates a URL-safe slug from the policy title field and updates the slug preview URL.

```js
function updSlug(pfx) {
  const titleEl = document.getElementById(pfx + '-title');
  const slugEl  = document.getElementById(pfx + '-slug');
  const slug = titleEl.value
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .trim()
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .slice(0, 60);
  slugEl.value = slug;
  if (pfx === 's') SS.slug = slug;
  else             AS.meta.slug = slug;
  updSlugPrev(pfx);
}

function updSlugPrev(pfx) {
  const slug = (pfx === 's' ? SS.slug : AS.meta.slug) || '[slug]';
  document.getElementById(pfx + '-slug-prev').textContent =
    'https://openrel.eu/policy/' + slug;
}
```

**Slug rules:**
- Lowercased.
- All characters except `a-z`, `0-9`, spaces, and hyphens are removed.
- Leading/trailing whitespace is trimmed.
- Spaces are replaced with hyphens.
- Consecutive hyphens are collapsed to one.
- Maximum 60 characters.
- Preview URL: `https://openrel.eu/policy/{slug}`

---

### 9.7 State Reset

#### `resetAll()`

Resets both `SS` and `AS` to their initial values and clears all DOM form elements.

```js
function resetAll() {
  // Simple state
  SS.q1 = null; SS.slug = ''; SS.policyTitle = '';
  Object.assign(SS.q2, { read:true, share:false, modify:false,
                          commercial:false, attribution:false, sharealike:false });
  SS.q3 = 'worldwide'; SS.geoInc = []; SS.geoExc = [];
  SS.q4 = 'unlimited'; SS.dateStart = ''; SS.dateEnd = '';
  SS.tplId = null;
  // Advanced state
  AS.policyType = null;
  Object.assign(AS.meta, { title:'', slug:'', desc:'', issuer:'',
                             status:'draft', asset:'', pid:'' });
  AS.perms = []; AS.prohs = []; AS.oblis = {}; AS.cons = {};
  AS.conflictTerm = 'odrl:prohibit';
  Object.assign(AS.agents, { assigner:'', assigneeType:'public', assigneeURI:'' });
  AS.tplId = null;
  // DOM reset (form fields, selection states, visibility)
  // ... clears input values, removes .sel classes, hides conditional panels
}
```

**Note:** `resetAll()` also includes DOM-side cleanup (clearing `<input>` values, removing `.sel` CSS classes from radio/checkbox options, hiding conditional panels like the geo-picker and date-picker). These DOM operations mirror the state reset.

---

### 9.8 Advanced Wizard Preview

#### `renderAdvancedPreview()`

Re-renders the live policy preview panel in the Advanced wizard. Called after every user interaction that modifies `AS`.

**Behaviour:**
- Reads current `AS` state.
- Renders a compact policy card (same structure as the Preview Modal in §8 but inline in the two-column layout).
- Shows placeholder text (`"Select a policy type to begin"`, `"No permissions selected"`, etc.) when sections are empty.
- Calls `fp(AS)` and displays the current fingerprint in a monospace badge.
- Calls `toODRL(AS)` and renders the current JSON-LD in a collapsible code block.

---

### 9.9 Geo Picker

#### `toggleGeo(type, iso)` / `toggleGeoA(type, iso)`

Handles country selection in the geographic constraint pickers. Two variants exist: `toggleGeo` for the Simple wizard (`SS.geoInc` / `SS.geoExc`), `toggleGeoA` for the Advanced wizard (`AS.cons['C13']`).

```js
function toggleGeo(type, iso) {
  const arr = type === 'inc' ? SS.geoInc : SS.geoExc;
  const country = COUNTRIES.find(x => x.iso === iso);
  const idx = arr.findIndex(x => x.iso === iso);
  if (idx >= 0) arr.splice(idx, 1);   // deselect
  else          arr.push(country);     // select
  renderGeoList(type, /*current search value*/);
  renderGeoTags(type);
}
```

- Each country object in `COUNTRIES` has the shape `{ iso: 'DE', label: 'Germany', flag: '🇩🇪' }`.
- Selected countries appear as removable tag chips below the search list.
- The ODRL hint (`odrl:LogicalConstraint odrl:and`) is shown when both `inc` and `exc` are non-empty.

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
| 1 | Should the wizard adopt the mock-up's light-mode palette, or be adapted to the existing dark-mode theme? |
| 2 | The mock-up is entirely standalone (no backend calls). Which steps should trigger live backend calls (e.g. PID resolution, ORCID lookup) in the integrated version? |
| 3 | The Simple wizard's reverse-mapping from canonical policy → Q1–Q4 answers is lossy (see §9.5). How should templates with constraints beyond the Simple wizard's scope be handled? |
| 4 | The constraint numbering (C01–C25) is internal to the mock-up. Should these IDs be retained in the implementation, or should the IRI-based identifiers be used as primary keys? |
| 5 | Should the Advanced wizard's live preview replace the existing `ComposePolicyCard` component, or coexist with it? |
| 6 | The `fp()` fingerprint uses djb2 (32-bit). For production use, should this be replaced with a cryptographic hash (e.g. SHA-256 truncated) for stronger collision resistance? |
| 7 | The `toODRL()` function's handling of geo constraints with both include and exclude lists uses `odrl:LogicalConstraint odrl:and`. Is this the intended ODRL serialisation, or should separate `odrl:spatial` constraints be used? |
