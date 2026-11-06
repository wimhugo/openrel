# OpenREL Encoding Examples — Batch 1 (Source Sections 91–110)

> Draft examples for implementers. These are templates, not legal opinions or fully evaluated policies. Placeholder asset IRIs and runtime parameter bindings require substitution.

## Scope and conversion decisions

The source document is *F.65.3.6 EOSC-RML Policy Snippet Vocabulary*. Sections 91–110 were screened against the supplied OpenREL policy inventory (21 entries) and current Turtle vocabularies. Six examples are retained; others are already substantially covered, duplicate another source section, or need further semantic work.

| Source section | Outcome | Existing policy / reason |
|---|---|---|
| 91 — Legal Basis Constraint for Data Usage (GDPR Consent) | Converted | Consent-only example; related to OR-EA-0.4 but not equivalent |
| 92 — Security Profile Enforcement (TRUST_PLUS) | Existing policy | OR-AI-TR-PL-0.5; TRUST+ access |
| 93 — Purpose-Bound Access (Research Use Only) | Converted | Research-purpose example |
| 94 — Role-Based Access Restriction (Researchers Only) | Existing policy | OR-IN-RO-0.5; Researcher-only access |
| 95 — Ethics Approval Requirement (requiresEthicsApproval) | Existing policy | OR-EA-0.4; Ethics approval |
| 96 — Technical Measures Constraint (requiresTOM) | Deferred | TOM evidence and requirement-set semantics need clarification |
| 97 — Data Volume Limitation (Maximum MiB) | Converted | OR-IN-HV-0.5; Related harvesting volume policy; generic per-request example retained |
| 98 — Spatial Access Constraint (Location-Based Restriction) | Existing policy | OR-EU-0.5; EU geographic restriction |
| 99 — Identity Constraint for Data Access (dpv:hasIdentity) | Existing policy | OR-BY-AC-VI-0.4; Verified identity; related existing policy |
| 100 — Access Revocation Policy | Deferred | Revocation status and authoritative source semantics require review |
| 101 — Time-Bound Policy Validity | Existing policy | OR-TL-0.4; Time-bounded access |
| 102 — Endpoint-Specific Notification | Existing policy | OR-AI-TR-PL-0.5; Notification to endpoint; related duty |
| 103 — Limited Access Count | Converted | Access-count example |
| 104 — Location-Based Access Restriction | Duplicate source section | OR-EU-0.5; Overlaps sections 98 and EU policy |
| 105 — Data Access with Deletion Duty | Converted | Deletion post-duty |
| 106 — Security Profile Enforcement | Duplicate source section | OR-AI-TR-PL-0.5; Overlaps section 92 |
| 107 — Notification Duty on Access | Existing policy | OR-AI-TR-PL-0.5; Notification duty |
| 108 — Connector-Specific Access Constraint | Converted | Connector identifier restriction |
| 109 — Maximum Number of Usages | Duplicate source section | Same pattern as section 103 |
| 110 — Duration-Based Access Permission | Existing policy | OR-TL-0.4; Duration/time-limited access; check precise elapsed-time semantics |

## Turtle conventions

The examples use existing OpenREL terms, and intentionally omit most descriptive metadata. `odrl:permission` and `odrl:duty` are rule structures; a NamedConstraint is referenced as a constraint, not used as a Duty. Runtime Parameters are referenced through `odrl:rightOperandReference` when appropriate.

```turtle
@prefix openrel: <http://www.w3id.org/ns/openrel/0/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
```

## Section 91 — Consent as the legal basis for access

**Original narrative.** This section illustrates how data usage permissions can be restricted based on the legal basis required under the GDPR. Specifically, access is only allowed if explicit consent has been given by the data subject.

**Turtle template**

```turtle
openrel:example-091 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/consent-controlled> ;
        odrl:action openrel:use ;
        odrl:constraint [
            a odrl:LogicalConstraint ;
            odrl:and ( openrel:consentLegal openrel:consentPrior )
        ]
    ] .
```

**Implementation and interpretation.** Requires both consent as legal basis and verified prior consent. Consent provenance, withdrawal, scope and validity still need evaluation by the authorisation service. This does not assert that consent is always the appropriate GDPR legal basis.

**References retained from the source:**
- https://edpb.europa.eu/
- https://harshp.com/dpv/

## Section 93 — Research-purpose restriction

**Original narrative.** This section defines a policy where access to a dataset is restricted to uses with a valid research purpose. Any other purposes such as marketing, profiling, or commercial exploitation are not permitted.

**Turtle template**

```turtle
openrel:example-093 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/research-only> ;
        odrl:action openrel:use ;
        odrl:constraint [
            a odrl:Constraint ;
            odrl:leftOperand openrel:usagePurpose ;
            odrl:operator odrl:eq ;
            odrl:rightOperand openrel:researchUse
        ]
    ] .
```

**Implementation and interpretation.** The source JSON uses dpv:AcademicResearch, a narrower purpose than the section title “Research Use Only”. This example uses openrel:researchUse. For strictly academic use, substitute the existing NamedConstraint openrel:academicUseOnly. The request purpose must be verified, not merely declared.

**References retained from the source:**
- https://besteves4.github.io/odrl-access-control-profile/oac.html
- https://harshp.com/dpv/

## Section 97 — Volume-limited data access

**Original narrative.** This section defines a policy that restricts the maximum volume of data a user or connector can download or access, expressed in megabytes (MiB). This constraint is relevant for datasets that involve bandwidth restrictions, sensitive material exposure control, or incremental access strategies.

**Turtle template**

```turtle
openrel:example-097 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/volume-controlled> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:volumeLimit
    ] .
```

**Implementation and interpretation.** openrel:volumeLimit uses openrel:usageVolume with odrl:lteq and odrl:rightOperandReference openrel:parameterVolume. The source illustrates 100 MiB per request; the parameter must be bound to an agreed quantity and unit, and the accounting scope must explicitly be per request if that is intended. Related but not identical to harvesting volume conditions in OR-IN-HV-0.5.

**References retained from the source:**
- https://www.w3.org/TR/odrl-model/
- https://www.eosc.eu/sites/default/files/eosc-fair-metrics-framework.pdf

## Section 103 — Maximum number of accesses

**Original narrative.** What This Section Includes:
 • Description: Restricts the number of times a dataset may be accessed. After the defined count is exceeded, further access is denied.
 • Permissions:
  o Access Within Limit – Allowed as long as the total access count does not exceed the specified threshold.
 • Prohibitions:
  o Access Beyond Limit – Not allowed once the maximum number of accesses has been reached.
 • Obligations:
  o Track Access Count – The system must track and evaluate access events against the defined count.
 • Sources:

**Turtle template**

```turtle
openrel:example-103 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/count-controlled> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:countLimit
    ] .
```

**Implementation and interpretation.** Bind openrel:parameterUsageCount to the intended maximum (five in the original example). The counting period, subject, action and whether the current request is included must be defined. Section 109 is a duplicate of this pattern.

**References retained from the source:**
- No URL was present in the extracted section.

## Section 105 — Access followed by deletion

**Original narrative.** What This Section Includes:
 • Description: Grants access to a dataset under the condition that the data must be deleted by the requester after a specific time or event.
 • Permissions:
  o Access with Timed Deletion – Permitted if the requester deletes the data after a predefined interval or upon completion of usage.
 • Prohibitions:
  o Retain Data Beyond Allowed Duration – Not permitted to keep the data beyond the declared retention window.
 • Obligations:
  o Enforce Deletion Mechanism – Requesters must have a system in place to delete the data after usage.
 • Sources:

**Turtle template**

```turtle
openrel:example-105 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/delete-after-access> ;
        odrl:action openrel:use ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:delete ;
            odrl:constraint [
                a odrl:Constraint ;
                odrl:leftOperand odrl:dateTime ;
                odrl:operator odrl:lteq ;
                odrl:rightOperandReference openrel:endDateParameter
            ]
        ]
    ] .
```

**Implementation and interpretation.** This is a post-duty template, not proof that deletion occurred. Bind endDateParameter to a future deadline; the source date (2025-12-31) is historical. The implementation must define whether the deadline applies to the duty completion time and how deletion evidence is captured.

**References retained from the source:**
- No URL was present in the extracted section.

## Section 108 — Approved connector only

**Original narrative.** What This Section Includes:
 • Description: Allows access to a dataset only if the requesting system (connector) matches a specific, pre-approved identifier. This ensures tight control over which systems may consume sensitive data.
 • Permissions:
  o Access from Approved Connector – Permitted if the request originates from a connector with a validated URI.
 • Prohibitions:
  o Access from Unrecognized Connector – Not allowed when the connector does not match the approved identifier.
 • Obligations:
  o Validate Connector Identity – The system must check the requesting connector’s identifier before granting access.
 • Sources:

**Turtle template**

```turtle
openrel:example-108 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/connector-restricted> ;
        odrl:action openrel:use ;
        odrl:constraint [
            a odrl:Constraint ;
            odrl:leftOperand openrel:connector ;
            odrl:operator odrl:eq ;
            odrl:rightOperand <https://approved.connector.org/id>
        ]
    ] .
```

**Implementation and interpretation.** The connector identifier is an illustrative IRI from the source. Verification must establish that the requester actually controls the identified connector. openrel:parameterAuthorisedIRI is currently a multi-valued endpoint parameter, so it is not substituted here as though it were a scalar connector parameter.

**References retained from the source:**
- No URL was present in the extracted section.

## Deferred modelling questions

**Section 96 — Technical and Organisational Measures.** The original requires encryption, access control and logging as a group. The current terms include `openrel:tomLimitation` and TOM concepts, but a precise assertion/evidence mechanism for satisfaction of all required measures is not established by the JSON. Do not encode a mere requirement declaration as proof of implementation.

**Section 100 — Revocation.** The source uses an `active`/`revoked` status; a reliable runtime revocation check requires an authoritative revocation registry, evaluation time and failure handling. This is not automatically equivalent to a policy publication status.

**Section 110 — Duration.** Existing time-limited policies are related, but an elapsed-duration rule (e.g., ten hours since first access) is not necessarily the same as an absolute end date. Retain as an explicit semantic comparison before marking it fully covered.

## Validation and limitations

The Turtle examples have been checked for parseability. This does not establish complete ODRL evaluation conformance, authorisation-service behaviour, legal validity or that the source references remain accessible. The conversion register provides a section-by-section disposition.
