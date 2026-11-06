# OpenREL Encoding Examples — Batch 2 (Source Sections 1–20)

**Status:** exploratory examples, not legal advice or production-ready policy definitions. The original document describes broad rights frameworks; the snippets below encode **bounded, illustrative subcases**, not the entirety of each section. No new OpenREL vocabulary terms have been introduced.

**Sources:** *F.65.3.6 EOSC-RML Policy Snippet Vocabulary* (uploaded DOCX); current OpenREL Turtle vocabulary and policy inventory. References are transcribed from the document as source labels, not independently verified.

## Conversion overview

| Section | Topic | Decision |
|---|---|---|
| 1 | Intellectual Property Rights | Existing-policy overlap / broad scope |
| 2 | Personal Data Rights | Converted (bounded subcase) |
| 3 | Ethical Rights | Existing-policy overlap / broad scope |
| 4 | Data Usage Rights | Existing-policy overlap / broad scope |
| 5 | Scientific Research Rights | Existing-policy overlap / broad scope |
| 6 | Licensing Framework Rights | Existing-policy overlap / broad scope |
| 7 | Access and Reuse Rights | Existing-policy overlap / broad scope |
| 8 | Ethical Research and Integrity Rights | Converted (bounded subcase) |
| 9 | Data Privacy and Protection Rights | Existing-policy overlap / broad scope |
| 10 | Open Access Rights | Existing-policy overlap / broad scope |
| 11 | Licensing and Rights Clearance | Existing-policy overlap / broad scope |
| 12 | Intellectual Property Management | Existing-policy overlap / broad scope |
| 13 | Collaborative Research Rights | Converted (bounded subcase) |
| 14 | Data Interoperability and Sharing Rights | Deferred — modelling gap |
| 15 | Ethical Data Sharing Rights | Converted (bounded subcase) |
| 16 | Publication and Attribution Rights | Converted (bounded subcase) |
| 17 | Data Ownership Rights | Existing-policy overlap / broad scope |
| 18 | Digital Rights Management (DRM) | Deferred — modelling gap |
| 19 | Fair Use and Fair Dealing Rights | Deferred — legal interpretation |
| 20 | Accessibility Rights | Converted (bounded subcase) |

## Common Turtle prefixes

```turtle
@prefix openrel: <http://www.w3id.org/ns/openrel/0/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
```

Each snippet is a separate graph and uses an example policy IRI. `https://example.org/` IRIs are illustrative placeholders. A NamedConstraint is used in `odrl:constraint`; it is not itself an ODRL duty. The templates are **not** asserted to be complete ODRL Profile conformance examples.

## Section 2 — Consent-controlled personal data access and processing

**Original narrative.** Provides a detailed explanation of Personal Data Rights, focusing on the protection and privacy of personal data under regulations like the GDPR.

**Turtle template**

```turtle
openrel:example-002 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/personal> ;
        odrl:action openrel:read, openrel:use ;
        odrl:constraint [
            a odrl:LogicalConstraint ;
            odrl:and ( openrel:consentLegal openrel:consentPrior )
        ] ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:log ;
            odrl:constraint openrel:logUse
        ]
    ] .
```

**Interpretation and limits.** Consent is one possible legal basis, not a universal prerequisite for GDPR processing. This template does not encode the separate source requirements for minimisation, security, or disclosure to third parties. Logging must be configured and evaluated.

**Source references as listed in the document:**
- General Data Protection Regulation (GDPR):
- Link: GDPR Overview
- European Data Protection Board (EDPB):
- Link: EDPB Guidelines
- EOSC Privacy Guidelines:
- Link: EOSC Privacy Guidelines

## Section 8 — Research ethics approval with accountable use

**Original narrative.** Details the rights and obligations related to conducting ethical research and maintaining integrity in the creation, use, and dissemination of scientific outputs. It emphasizes transparency, accountability, and adherence to ethical guidelines.

**Turtle template**

```turtle
openrel:example-008 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/ethics-controlled> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:ethicsApproval ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:log ;
            odrl:constraint openrel:logUse
        ]
    ] .
```

**Interpretation and limits.** An ethics approval check is only one aspect of the original section. Fabrication, misrepresentation, accuracy, and institutional compliance require additional evaluation or governance outside this template. This is narrower than a complete research integrity policy.

**Source references as listed in the document:**
- COPE (Committee on Publication Ethics):
- Link: COPE Ethical Guidelines
- EOSC Ethics and Integrity Framework:
- Link: EOSC Ethics Framework
- Helsinki Declaration (WMA):
- Link: Helsinki Declaration

## Section 13 — Collaborative research with attribution and institutional affiliation

**Original narrative.** Outlines the rights and responsibilities associated with collaborative research projects. It emphasizes transparency, equitable attribution, and adherence to ethical and legal standards in joint efforts.

**Turtle template**

```turtle
openrel:example-013 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/collaboration> ;
        odrl:action openrel:use, openrel:distribute ;
        odrl:constraint openrel:institutionalAffiliation ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:attribute ;
            odrl:constraint openrel:notifyCitation
        ]
    ] .
```

**Interpretation and limits.** Institutional affiliation is not equivalent to a signed collaboration agreement or membership of a particular project. The source also calls for contributor consensus and role assignment, which this example does not assert. Attribution needs implementation rules for identifying all contributors.

**Source references as listed in the document:**
- OECD Principles for Access to Research Data:
- Link: OECD Principles
- EOSC Collaborative Research Guidelines:
- Link: EOSC Collaborative Research
- Vancouver Guidelines (ICMJE):
- Link: ICMJE Vancouver Guidelines

## Section 15 — Ethical sharing with prior consent and audit

**Original narrative.** Defines the ethical considerations and responsibilities associated with sharing data, ensuring respect for privacy, consent, and the rights of individuals and communities. It focuses on promoting responsible data sharing practices while adhering to ethical and legal standards.

**Turtle template**

```turtle
openrel:example-015 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/sensitive> ;
        odrl:action openrel:distribute ;
        odrl:constraint openrel:consentPrior ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:log ;
            odrl:constraint openrel:logUse
        ]
    ] .
```

**Interpretation and limits.** The original includes community interests, anonymisation and avoidance of exploitation. Those are not established by a prior-consent check. This is a consent-and-audit subcase, not a complete ethical sharing policy. Do not treat anonymisation as proven.

**Source references as listed in the document:**
- Declaration of Helsinki (WMA):
- Link: Declaration of Helsinki
- GDPR Ethical Data Sharing Guidelines:
- Link: GDPR Ethical Guidelines
- EOSC Ethical Data Sharing Framework:
- Link: EOSC Ethical Data Sharing

## Section 16 — Publication with citation duty

**Original narrative.** Defines the rights and obligations related to the publication of research outputs and the proper attribution of authors and contributors. It emphasizes fairness, transparency, and compliance with ethical standards.

**Turtle template**

```turtle
openrel:example-016 a openrel:Licence ;
    odrl:permission [
        odrl:target <https://example.org/research/output> ;
        odrl:action openrel:distribute ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:attribute ;
            odrl:constraint openrel:notifyCitation
        ]
    ] .
```

**Interpretation and limits.** Captures a narrow publication-and-attribution pattern. It does not determine author order, originality, journal policies or rights clearance. Compare with existing attribution licences before publishing this as a standalone example.

**Source references as listed in the document:**
- COPE Guidelines for Publication Ethics:
- Link: COPE Guidelines
- ICMJE Authorship Guidelines:
- Link: ICMJE Guidelines
- EOSC Publication Standards:
- Link: EOSC Publication Standards

## Section 20 — Accessible adaptation and distribution

**Original narrative.** Defines the rights and responsibilities to ensure that digital content, research outputs, and platforms are accessible to all users, including individuals with disabilities. It emphasizes compliance with accessibility standards and inclusive design principles.

**Turtle template**

```turtle
openrel:example-020 a openrel:Licence ;
    odrl:permission [
        odrl:target <https://example.org/research/content> ;
        odrl:action openrel:modify, openrel:distribute ;
        odrl:duty [
            a openrel:PostDuty ;
            odrl:action openrel:attribute ;
            odrl:constraint openrel:notifyInAsset
        ]
    ] .
```

**Interpretation and limits.** Allows adaptations and distribution, with a change notice. This does not encode compliance with WCAG, a legal entitlement to accessible copies, or non-discrimination. Those need separate conformance and legal interpretation. Check the existing no-derivatives policies for possible conflicts.

**Source references as listed in the document:**
- W3C Web Content Accessibility Guidelines (WCAG):
- Link: WCAG Overview
- UN Convention on the Rights of Persons with Disabilities (CRPD):
- Link: CRPD Overview
- EOSC Accessibility Framework:
- Link: EOSC Accessibility Framework

## Review priorities

1. **Authorisation vs. legal basis:** consent, ethics approval and organisational affiliation are distinct claims; an ODRL permission does not independently prove them.
2. **Duty timing:** the illustrative PreDuty/PostDuty design requires an execution/evaluation contract. Audit evidence must be available to the policy evaluator.
3. **Scope:** original sections contain numerous permissions, prohibitions and obligations beyond the bounded examples. Omission is not permission to violate those requirements.
4. **Overlaps:** the policy inventory already includes licence, attribution, consent, ethics and restricted-access examples. Confirm semantic differences before publication.
5. **Deferred cases:** metadata conformance (14), DRM (18), and fair use/fair dealing (19) should be modelled only after the relevant external decision criteria and rights exceptions are defined.
