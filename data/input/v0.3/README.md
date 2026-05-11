# OpenREL Normalized Vocabulary

**Version:** 1.0.0  
**Status:** Draft for Technical Review  
**Namespace:** `https://openrel.eu/vocab/`  
**Base standard:** [ODRL Information Model 2.2](https://www.w3.org/TR/odrl-model/)

---

## Overview

This repository contains the normalized OpenREL Rights Machine Language (RML) vocabulary for the EOSC ecosystem. It transforms the EOSC-RML_Policy_Snippet_Vocabulary Draft v0.2 (119 sections) into a clean, consistent, machine-actionable model suitable for ODRL policy engines and future pipeline integration.

The vocabulary is organized into modular, reusable components that can be referenced independently or composed into compound policies.

---

## Repository Structure

```
openrel-vocab/
├── actions/
│   └── actions.json           # 14 normalized actions (replaces 200+ draft action labels)
├── constraints/
│   └── constraints.json       # 25 typed, reusable constraints
├── agents/
│   └── agents.json            # 7 canonical agent types (assigner/assignee)
├── sources/
│   └── sources.json           # 40 deduplicated, granularly referenced sources
├── policies/
│   └── policies.json          # 17 normalized machine-actionable policy templates
├── examples/
│   └── example-policies.json  # 2 instantiated example policies (simple + complex)
└── meta/
    └── normalization-decisions.json  # Full modeling decisions and section treatment map
```

---

## Key Design Principles

**1. ODRL compliance first.** Every policy, constraint, and action maps to ODRL 2.2 or a documented extension in the `openrel:` namespace. Non-standard operators (`definesAs`, `isNull`, `outside`) from the draft have been removed.

**2. Actions normalize, constraints qualify.** The draft used 200+ action names. The normalized vocabulary uses 14 canonical actions (e.g., `openrel:use`, `openrel:distribute`, `openrel:modify`) and expresses variations (non-commercial, attribution-required, researcher-only) as typed constraints.

**3. Agents are mandatory.** The draft contained no assigner/assignee modelling. Every policy template requires `assigner` and `assignee` declarations. Instance-specific URIs are marked `[INSTANCE]`.

**4. Sources are granular.** The draft cited `https://eosc-portal.eu/` for 46+ sections with no specificity. The sources registry provides specific document URIs, article numbers, and issuer metadata for all 40 sources.

**5. Deduplication is explicit.** Sections 92/106/119, 103/109/114, 108/118, 102/107/113, 110/115, 101/111/116, 98/104, and 105/117 were exact or near-exact duplicates. Each group is merged into one parameterizable template.

**6. DPV for privacy semantics.** Purpose (`dpv:hasPurpose`), legal basis (`dpv:hasLegalBasis`), and role (`dpv:hasRole`) constraints use [Data Privacy Vocabulary](https://w3id.org/dpv) terms — not informal strings.

---

## Namespaces and Prefixes

| Prefix | URI | Description |
|--------|-----|-------------|
| `openrel:` | `https://openrel.eu/vocab/` | OpenREL vocabulary extensions |
| `odrl:` | `http://www.w3.org/ns/odrl/2/` | ODRL 2.2 core |
| `dpv:` | `https://w3id.org/dpv#` | Data Privacy Vocabulary |
| `ids:` | `https://w3id.org/idsa/core/` | IDS Reference Architecture |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` | XML Schema datatypes |
| `foaf:` | `http://xmlns.com/foaf/0.1/` | FOAF vocabulary |
| `dcterms:` | `http://purl.org/dc/terms/` | Dublin Core |

---

## Policy Templates: Instantiation

Policy templates use `[INSTANCE]` placeholders for values that must be set per use case:

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `[ASSIGNER_URI]` | Data provider's persistent URI | `https://ror.org/04wxnsj81` |
| `[ASSIGNEE_URI]` | Data consumer's persistent URI | `https://orcid.org/0000-0001-2345-6789` |
| `[TARGET_URI]` | Dataset or resource URI | `https://doi.org/10.1234/dataset` |
| `[START_DATETIME]` | ISO 8601 start datetime | `2025-01-01T00:00:00Z` |
| `[END_DATETIME]` | ISO 8601 end datetime | `2025-12-31T23:59:59Z` |
| `[DURATION]` | ISO 8601 duration | `PT24H` |
| `[NOTIFICATION_ENDPOINT_URI]` | Notification service URI | `https://audit.example.org/notify` |
| `[CLEARINGHOUSE_URI]` | Logging clearing house URI | `https://clearinghouse.eosc.eu/logs` |
| `[CONNECTOR_URI]` | Authorized connector URI | `https://connector.example.org/id` |

---

## Policy Index

| ID | Label | Source Sections |
|----|-------|----------------|
| `openrel:policy:p001` | GDPR Consent-Gated Data Use | §91, §2, §9, §47 |
| `openrel:policy:p002` | Security Profile Enforcement — TRUST+ | §92, §106, §119 |
| `openrel:policy:p003` | Purpose-Bound Access — Academic Research | §93 |
| `openrel:policy:p004` | Role-Based Access — Researchers Only | §94 |
| `openrel:policy:p005` | Ethics Approval Gate | §95, §8, §26, §48 |
| `openrel:policy:p006` | Technical and Organisational Measures | §96 |
| `openrel:policy:p007` | Data Volume Limitation | §97 |
| `openrel:policy:p008` | Spatial Access Restriction — EU | §98, §104 |
| `openrel:policy:p009` | Verified Identity Gate (eIDAS) | §99 |
| `openrel:policy:p010` | Access Revocation Gate | §100 |
| `openrel:policy:p011` | Time-Bound Access Window | §101, §111, §116 |
| `openrel:policy:p012` | Notification Duty on Access | §102, §107, §113 |
| `openrel:policy:p013` | Usage Count Limit | §103, §109, §114 |
| `openrel:policy:p014` | Duration-Based Access Window | §110, §115 |
| `openrel:policy:p015` | Access with Deletion Duty | §105, §117 |
| `openrel:policy:p016` | Logging Duty After Access | §112 |
| `openrel:policy:p017` | Connector-Restricted Access | §108, §118 |

---

## Example Policies

Two instantiated examples are provided in `examples/example-policies.json`:

**Example A — Non-Commercial Reuse with Attribution**  
Models CC BY-NC semantics in ODRL. A researcher may use, distribute, and modify a dataset for academic purposes, subject to an attribution duty. Commercial use is prohibited.

**Example B — Restricted Sensitive Data Access (Compound)**  
A complex compound policy for a health research dataset. Combines six simultaneous constraints (consent, researcher role, EU geography, TRUST+ security profile, ethics approval, 24h duration) with three mandatory postDuties (notify, log, delete). Demonstrates full compound constraint composition and multi-duty orchestration.

---

## Sections Treatment Summary

| Treatment | Count | Notes |
|-----------|-------|-------|
| Transformed into normalized policies | 17 | From Sections 91-119 |
| Merged (duplicates eliminated) | 8 groups | See normalization-decisions.json |
| Used as conceptual source only | ~72 sections | Sections 1-90 (most); concepts extracted into registries |
| Dropped (purely narrative, no extractable model) | ~18 sections | Sections 53-90 second half; closing remarks, advocacy sections |

---

## Future Work

- `meta/conceptual-map.json` — explicit mapping of Sections 1-90 themes to vocabulary concepts
- `meta/namespace.json` — formal OpenREL namespace declaration (JSON-LD context file)
- ODRL validation schema for policy instances
- Google Sheets → JSON pipeline template
- OpenREL ODRL profile specification document

---

## Dependencies

- [ODRL 2.2](https://www.w3.org/TR/odrl-model/) — W3C Recommendation
- [Data Privacy Vocabulary (DPV)](https://w3id.org/dpv) — W3C DPVCG
- [IDS Reference Architecture](https://w3id.org/idsa/core/) — IDSA
- [GDPR](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32016R0679) — EU 2016/679
- [eIDAS Regulation](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2014.257.01.0073.01.ENG) — EU 910/2014

---

*Generated by the OpenREL normalization process. Basis: EOSC-RML_Policy_Snippet_Vocabulary_Draft_v0_2.*
