# OpenREL Encoding Examples — Batch 3 (Source Sections 21–40)

**Status:** exploratory bounded templates; not production-ready or legal advice. Original text and source labels are preserved below; source references have not been independently verified. No new OpenREL vocabulary terms are introduced.

**Source:** *F.65.3.6 EOSC-RML Policy Snippet Vocabulary* (uploaded DOCX), current OpenREL vocabularies and policy inventory.

## Conversion overview

| Section | Source topic | Disposition |
|---|---|---|
| 21 | User Privacy Rights | Existing-policy overlap |
| 22 | Reproducibility and Data Integrity Rights | Converted (bounded subcase) |
| 23 | Ethical AI Usage Rights | Converted (bounded subcase) |
| 24 | Sustainable Research Practices | Deferred — modelling gap |
| 25 | Collaborative Data Governance | Converted (bounded subcase) |
| 26 | Research Ethics and Compliance | Existing-policy overlap |
| 27 | Long-Term Data Stewardship Rights | Converted (bounded subcase) |
| 28 | Public Engagement and Outreach Rights | Existing-policy overlap / broad scope |
| 29 | Data Ethics and Fairness | Deferred — modelling gap |
| 30 | Copyright Exceptions and Limitations | Deferred — legal interpretation |
| 31 | Research Data Sharing Rights | Existing-policy overlap |
| 32 | Data Security and Risk Mitigation Rights | Converted (bounded subcase) |
| 33 | Research Data Provenance Rights | Converted (bounded subcase) |
| 34 | Ethical Research Collaboration Rights | Existing-policy overlap |
| 35 | Open Access Publication Rights | Existing-policy overlap |
| 36 | Intellectual Property Licensing Rights | Existing-policy overlap |
| 37 | Data Collaboration and Sharing Agreements | Converted (bounded subcase) |
| 38 | Data Curation and Management Responsibilities | Deferred — modelling gap |
| 39 | Digital Preservation and Accessibility Standards | Deferred — modelling gap |
| 40 | Compliance with Open Science Policies | Deferred — broad governance |

## Common prefixes

```turtle
@prefix openrel: <http://www.w3id.org/ns/openrel/0/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
```

Each example is a separate graph. Example target IRIs are placeholders, not real assets. `odrl:constraint` references existing NamedConstraints; post-duties use `openrel:PostDuty`.

## Section 22 — Reproducible research with recorded methods and audit trail

### Original narrative and rule summary

- Description: Defines the rights and responsibilities related to ensuring the reproducibility of research and maintaining the integrity of data. This includes adhering to best practices for data documentation, versioning, and validation to support transparent and trustworthy research.
- Permissions: Lists allowed actions under reproducibility and data integrity, such as:
- Replicate Studies: Allowed when data and methods are openly shared.
- Verify Data: Allowed to perform checks to ensure data accuracy and consistency.
- Prohibitions: Lists prohibited actions, including:
- Manipulate Data: Not allowed to alter or fabricate data to misrepresent results.
- Suppress Errors: Not allowed to conceal errors or inconsistencies in data or methods.
- Obligations: Lists required actions, including:
- Document Methods: Researchers must provide detailed documentation of methodologies to enable reproducibility.
- Ensure Data Integrity: Researchers must maintain accurate and verifiable records of data and changes.
- Description: Guidelines for promoting research reproducibility and integrity in scientific studies.
- Description: EOSC-specific recommendations for ensuring reproducibility and maintaining data integrity in open science.
- Description: Emphasizes the importance of data reproducibility and integrity in open research ecosystems.

### Turtle template

```turtle
openrel:example-022 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/reproducibility> ;
        odrl:action openrel:reproduce ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Logging is not equivalent to documenting a methodology or proving integrity. The original prohibition against fabrication and error suppression remains outside the encoded subcase.

## Section 23 — AI research access with ethics gate and audit

### Original narrative and rule summary

- Description: Defines the rights and responsibilities related to the ethical use of artificial intelligence (AI) in research and digital environments. It emphasizes transparency, fairness, accountability, and compliance with legal and ethical standards for AI systems.
- Permissions: Lists allowed actions under ethical AI usage, such as:
- Deploy AI for Research: Allowed when AI systems are used transparently and align with ethical guidelines.
- Analyze Data: Allowed for AI systems to analyze data, provided privacy and data protection regulations are adhered to.
- Prohibitions: Lists prohibited actions, including:
- Bias in AI Systems: Not allowed to deploy AI systems with discriminatory biases.
- Use Without Transparency: Not allowed to use AI systems without disclosing their purpose or methodology.
- Obligations: Lists required actions, including:
- Ensure Explainability: AI systems must be explainable, with clear documentation of their processes and outputs.
- Audit for Bias: Regular auditing of AI systems must be conducted to identify and mitigate biases.
- Description: Proposed legislation regulating AI usage within the European Union, focusing on ethical and accountable AI practices.
- Description: Guidelines for ethical AI use, emphasizing transparency, accountability, and fairness.
- Description: EOSC-specific recommendations for the ethical integration of AI in open science.

### Turtle template

```turtle
openrel:example-023 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/ai-research> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:ethicsApproval ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Ethics approval and audit logging do not demonstrate explainability, fairness, bias testing, or transparency. This overlaps with the earlier ethics example (section 8), but is presented as an AI-specific use case; consolidate if the published catalogue needs one example per rule pattern.

## Section 25 — Governed collaboration with logged data access

### Original narrative and rule summary

- Description: Defines the rights and responsibilities for collaboratively managing data, ensuring that all stakeholders have a clear understanding of their roles, responsibilities, and shared benefits in governing research data. It emphasizes transparency, equitable decision-making, and compliance with legal and ethical standards.
- Permissions: Lists allowed actions under collaborative data governance, such as:
- Share Governance: Allowed for stakeholders to share governance responsibilities and decision-making authority.
- Access Shared Data: Allowed when all parties agree and proper governance protocols are in place.
- Prohibitions: Lists prohibited actions, including:
- Exclude Stakeholders: Not allowed to exclude relevant stakeholders from data governance processes.
- Misuse Shared Data: Not allowed to use shared data outside agreed-upon terms.
- Obligations: Lists required actions, including:
- Define Roles and Responsibilities: Governance structures must clearly outline the roles and responsibilities of all stakeholders.
- Ensure Transparency: Data governance processes must be transparent and equitable, ensuring all stakeholders have access to information and decision-making mechanisms.
- Description: International guidelines for collaborative and responsible data governance.
- Description: EOSC-specific recommendations for collaboratively managing data in open science ecosystems.
- Description: Global guidelines for fostering collaboration and equity in data governance.

### Turtle template

```turtle
openrel:example-025 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/shared-governance> ;
        odrl:action openrel:read, openrel:use ;
        odrl:constraint openrel:managedAccess ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Managed access is not evidence of stakeholder agreement, shared decision rights, or governance-role allocation. A formal agreement and membership check must be evaluated outside this snippet.

## Section 27 — Preservation and format migration

### Original narrative and rule summary

- Description: Defines the rights and responsibilities related to the long-term preservation, management, and accessibility of research data. It emphasizes sustainability, compliance with archival standards, and ensuring data usability for future generations.
- Permissions: Lists allowed actions under long-term data stewardship, such as:
- Preserve Data: Allowed for institutions and repositories to archive data for long-term use.
- Migrate Formats: Allowed to convert data to newer formats to maintain accessibility and usability.
- Prohibitions: Lists prohibited actions, including:
- Neglect Maintenance: Not allowed to leave archived data unmanaged, leading to degradation or loss.
- Restrict Future Access: Not allowed to impose unnecessary restrictions that hinder future accessibility.
- Obligations: Lists required actions, including:
- Ensure Data Integrity: Repositories must implement measures to protect data from corruption and unauthorized access.
- Adopt Preservation Standards: Institutions must follow recognized standards for data archiving and stewardship.
- Description: Guidelines emphasizing the importance of long-term data stewardship to ensure data is Findable, Accessible, Interoperable, and Reusable.
- Description: Recommendations for sustainable data stewardship and long-term digital preservation.
- Description: EOSC-specific guidance for ensuring sustainable data preservation and accessibility.

### Turtle template

```turtle
openrel:example-027 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/preservation-object> ;
        odrl:action openrel:archive, openrel:modify ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

The modify action is used only as a proxy for authorised format migration; it does not constrain changes to preservation-safe transformations. Archiving and logging do not establish OAIS compliance, fixity, retention, or future accessibility.

## Section 32 — Encryption-controlled data handling with audit

### Original narrative and rule summary

- Description: Defines the rights and responsibilities for ensuring the security of research data and mitigating risks associated with data breaches, unauthorized access, or corruption. It emphasizes proactive measures, compliance with legal standards, and the safeguarding of sensitive information.
- Permissions: Lists allowed actions under data security and risk mitigation, such as:
- Encrypt Data: Allowed to use encryption methods to protect sensitive data during storage and transmission.
- Control Access: Allowed to implement access controls to ensure only authorized personnel can access specific datasets.
- Prohibitions: Lists prohibited actions, including:
- Neglect Security Measures: Not allowed to store or share data without implementing adequate security protections.
- Share Security Credentials: Not allowed to share access credentials or encryption keys with unauthorized individuals.
- Obligations: Lists required actions, including:
- Monitor Data Security: Organizations must continuously monitor and audit data security measures to identify vulnerabilities.
- Implement Incident Response Plans: Researchers and institutions must establish protocols for responding to data breaches or security incidents.
- Description: International standard for implementing and maintaining information security management systems.
- Description: Recommendations for safeguarding research data against risks and breaches.
- Description: EOSC-specific guidance for ensuring data security in open science environments.

### Turtle template

```turtle
openrel:example-032 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/security-sensitive> ;
        odrl:action openrel:read ;
        odrl:constraint openrel:managedAccess ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

This is a controlled-read and audit subcase, NOT a rule requiring encryption. Although openrel:encrypt is an available action, authorising encryption is not equivalent to mandating encryption at rest or in transit. Incident response and security controls need additional verifiable constraints.

## Section 33 — Provenance-aware distribution with recorded use

### Original narrative and rule summary

- Description: Defines the rights and responsibilities for maintaining and verifying the provenance of research data. It emphasizes tracking the origin, transformations, and ownership of data to ensure transparency, accountability, and reproducibility in research.
- Permissions: Lists allowed actions under data provenance, such as:
- Track Data Provenance: Allowed to use tools and methods to document the origin and history of data.
- Share Provenance Metadata: Allowed to share metadata about data provenance with collaborators and repositories.
- Prohibitions: Lists prohibited actions, including:
- Omit Provenance Information: Not allowed to omit or falsify information about the origin or transformations of data.
- Obfuscate Data Sources: Not allowed to obscure or misrepresent the sources of data.
- Obligations: Lists required actions, including:
- Maintain Provenance Records: Researchers must maintain detailed and accurate records of data provenance.
- Verify Provenance: Researchers must verify the authenticity and reliability of data sources and documentations.
- Description: Standards for documenting and exchanging provenance information for data and research workflows.
- Description: International guidelines promoting the documentation of research data provenance to ensure transparency and reproducibility.
- Description: EOSC-specific guidance for ensuring the provenance of research data in open science environments.

### Turtle template

```turtle
openrel:example-033 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/provenance-object> ;
        odrl:action openrel:distribute ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

A usage log is not a PROV record and does not verify source authenticity or capture transformations. A provenance artefact, conformance profile and verification service would be needed for the original obligations.

## Section 37 — Managed collaboration data sharing with audit

### Original narrative and rule summary

- Description: Defines the rights and responsibilities for establishing agreements related to data collaboration and sharing. It emphasizes clarity, transparency, and adherence to legal and ethical standards in defining terms for access, usage, and ownership of shared data.
- Permissions: Lists allowed actions under data collaboration and sharing agreements, such as:
- Share Data with Agreements: Allowed to share data with collaborators under mutually agreed terms and conditions.
- Establish Joint Ownership: Allowed to define joint ownership of collaboratively generated data.
- Prohibitions: Lists prohibited actions, including:
- Share Without Agreement: Not allowed to share data without a formal agreement outlining roles, responsibilities, and usage terms.
- Misuse Shared Data: Not allowed to use shared data for purposes not covered by the agreement.
- Obligations: Lists required actions, including:
- Document Agreements: Researchers and institutions must formalize collaboration and sharing agreements in writing.
- Ensure Compliance: Parties must adhere to the terms and conditions specified in the agreement.
- Description: International guidelines for creating clear and equitable data sharing agreements.
- Description: EOSC-specific guidance for facilitating effective and ethical data sharing agreements.
- Description: Recommendations for creating agreements that promote transparency and protect data rights.

### Turtle template

```turtle
openrel:example-037 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/collaboration-agreement> ;
        odrl:action openrel:distribute ;
        odrl:constraint openrel:managedAccess ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Managed access is not evidence of a signed data-sharing agreement, joint ownership or permitted-purpose scope. The agreement must be represented and validated separately. Overlaps with sections 13 and 25.

## Deferred and overlapping sections

### Section 21 — Section 21: User Privacy Rights
**Disposition:** Existing-policy overlap. Consent and privacy already covered by sections 2, 15, 91 and existing consent rules.

**Source narrative:** Description: Defines the rights and responsibilities related to safeguarding user privacy, focusing on the protection of personal data and ensuring transparency in data collection, processing, and storage. It emphasizes compliance with regulations such as GDPR and promotes ethical data handling practices.

**Source references (as listed):**
- General Data Protection Regulation (GDPR):
- Link: GDPR Overview
- OECD Privacy Principles:
- Link: OECD Privacy Guidelines
- EOSC User Privacy Framework:
- Link: EOSC Privacy Framework

### Section 24 — Section 24: Sustainable Research Practices
**Disposition:** Deferred — modelling gap. Sustainability measures and resource-use thresholds need explicit verifiable operands.

**Source narrative:** Description: Defines the rights and responsibilities for promoting sustainability in research practices, emphasizing the efficient use of resources, reducing environmental impact, and supporting long-term accessibility and reuse of research outputs.

**Source references (as listed):**
- UN Sustainable Development Goals (SDGs):
- Link: UN SDGs
- OECD Guidelines on Sustainable Research Practices:
- Link: OECD Sustainability Guidelines
- EOSC Sustainability Framework:
- Link: EOSC Sustainability Framework

### Section 26 — Section 26: Research Ethics and Compliance
**Disposition:** Existing-policy overlap. Research ethics and compliance substantially overlaps sections 8 and 23.

**Source narrative:** Description: Defines the rights and responsibilities for maintaining ethical standards and compliance in research practices. It focuses on ensuring integrity, accountability, and adherence to institutional, legal, and ethical guidelines.

**Source references (as listed):**
- Declaration of Helsinki (WMA):
- Link: Declaration of Helsinki
- OECD Research Ethics Guidelines:
- Link: OECD Research Ethics
- EOSC Research Ethics Framework:
- Link: EOSC Research Ethics Framework

### Section 28 — Section 28: Public Engagement and Outreach Rights
**Disposition:** Existing-policy overlap / broad scope. Public outreach overlaps publication/distribution examples; consent and communication rights need narrower case.

**Source narrative:** Description: Defines the rights and responsibilities related to engaging the public in research activities and sharing scientific knowledge with non-specialist audiences. It emphasizes accessibility, inclusivity, and ethical communication.

**Source references (as listed):**
- UNESCO Science Communication Guidelines:
- Link: UNESCO Science Communication
- OECD Public Engagement in Science Policy:
- Link: OECD Public Engagement
- EOSC Public Engagement Framework:
- Link: EOSC Public Engagement

### Section 29 — Section 29: Data Ethics and Fairness
**Disposition:** Deferred — modelling gap. Fairness and non-discrimination require measurable external assessments.

**Source narrative:** Description: Defines the rights and responsibilities for ensuring ethical and fair practices in data collection, usage, and sharing. It emphasizes respect for individuals, equity in data handling, and adherence to ethical guidelines.

**Source references (as listed):**
- OECD Data Ethics Framework:
- Link: OECD Data Ethics
- GDPR Ethical Data Handling Principles:
- Link: GDPR Ethical Principles
- EOSC Data Ethics Framework:
- Link: EOSC Data Ethics Framework

### Section 30 — Section 30: Copyright Exceptions and Limitations
**Disposition:** Deferred — legal interpretation. Copyright exceptions depend on jurisdiction, purpose and specific legal tests.

**Source narrative:** Description: Defines the rights and responsibilities regarding exceptions and limitations to copyright laws, allowing limited use of copyrighted material without requiring explicit permission. It includes provisions for purposes such as education, research, and criticism.

**Source references (as listed):**
- WIPO Guide to Copyright Exceptions:
- Link: WIPO Copyright Exceptions
- US Copyright Act (Fair Use, Section 107):
- Link: US Copyright Act Section 107
- EU Copyright Directive:
- Link: EU Copyright Directive

### Section 31 — Section 31: Research Data Sharing Rights
**Disposition:** Existing-policy overlap. Research data sharing already represented by licence and sharing examples.

**Source narrative:** Description: Defines the rights and responsibilities related to sharing research data, emphasizing open access, transparency, and adherence to ethical and legal standards. It encourages collaboration while safeguarding sensitive and proprietary information.

**Source references (as listed):**
- FAIR Principles (GO FAIR Initiative):
- Link: FAIR Principles Overview
- OECD Guidelines for Research Data Sharing:
- Link: OECD Research Data Sharing
- EOSC Data Sharing Framework:
- Link: EOSC Data Sharing Framework

### Section 34 — Section 34: Ethical Research Collaboration Rights
**Disposition:** Existing-policy overlap. Ethical collaboration overlaps sections 13, 15 and 25.

**Source narrative:** Description: Defines the rights and responsibilities for ensuring ethical practices in collaborative research. It emphasizes fairness, transparency, mutual respect, and adherence to ethical and legal standards in all collaborative activities.

**Source references (as listed):**
- ICMJE Guidelines for Authorship and Collaboration:
- Link: ICMJE Guidelines
- OECD Guidelines on Research Collaboration:
- Link: OECD Research Collaboration
- EOSC Collaboration Framework:
- Link: EOSC Collaboration Framework

### Section 35 — Section 35: Open Access Publication Rights
**Disposition:** Existing-policy overlap. Open-access publication and attribution already covered.

**Source narrative:** Description: Defines the rights and responsibilities for ensuring open access to research publications, promoting transparency, accessibility, and equitable knowledge sharing. It emphasizes compliance with open access mandates and ethical standards.

**Source references (as listed):**
- Plan S Guidelines:
- Link: Plan S Guidelines
- UNESCO Open Science Recommendations:
- Link: UNESCO Open Science
- EOSC Open Access Framework:
- Link: EOSC Open Access Framework

### Section 36 — Section 36: Intellectual Property Licensing Rights
**Disposition:** Existing-policy overlap. IP licensing already represented in existing licence inventory.

**Source narrative:** Description: Defines the rights and responsibilities related to licensing intellectual property (IP) to ensure proper usage, distribution, and protection of creators’ rights. It emphasizes transparency, compliance with licensing terms, and ethical practices.

**Source references (as listed):**
- Creative Commons Licensing Framework:
- Link: Creative Commons Licenses
- WIPO Guide on Licensing IP Rights:
- Link: WIPO Licensing Guide
- EOSC Licensing Framework:
- Link: EOSC Licensing Framework

### Section 38 — Section 38: Data Curation and Management Responsibilities
**Disposition:** Deferred — modelling gap. Curation quality, retention and metadata compliance need verification model.

**Source narrative:** Description: Defines the rights and responsibilities for the curation and management of research data, ensuring that data remains accurate, organized, and accessible throughout its lifecycle. It emphasizes adherence to best practices, compliance with standards, and promoting long-term usability.

**Source references (as listed):**
- FAIR Principles for Data Management:
- Link: FAIR Principles
- OECD Guidelines on Data Curation:
- Link: OECD Data Curation
- EOSC Data Curation Framework:
- Link: EOSC Curation Framework

### Section 39 — Section 39: Digital Preservation and Accessibility Standards
**Disposition:** Deferred — modelling gap. Preservation standards and future accessibility need explicit external assessment.

**Source narrative:** Description: Defines the rights and responsibilities for ensuring the long-term preservation and accessibility of digital content and research outputs. It emphasizes compliance with preservation standards, proactive maintenance, and the use of sustainable technologies.

**Source references (as listed):**
- ISO 14721: Open Archival Information System (OAIS):
- Link: ISO OAIS Standard
- UNESCO Guidelines on Digital Preservation:
- Link: UNESCO Digital Preservation
- EOSC Preservation and Accessibility Framework:
- Link: EOSC Preservation Framework

### Section 40 — Section 40: Compliance with Open Science Policies
**Disposition:** Deferred — broad governance. Compliance with open science policy needs concrete requirements and evidence.

**Source narrative:** Description: Defines the rights and responsibilities for adhering to open science policies, ensuring transparency, accessibility, and collaboration in research practices. It emphasizes compliance with institutional, national, and international guidelines for open science.

**Source references (as listed):**
- UNESCO Open Science Recommendations:
- Link: UNESCO Open Science
- European Open Science Cloud (EOSC) Policies:
- Link: EOSC Policies
- Plan S and cOAlition S Guidelines:
- Link: Plan S Guidelines

## QA and modelling notes

- All seven snippets were parsed individually using RDFLib; RDF syntax validity does not establish ODRL Profile conformance or operational enforceability.
- Existing named constraints are reused without asserting that their evaluation mechanisms have been implemented.
- Examples 23, 25, 33 and 37 deliberately leave important source obligations outside the encoded rule; do not represent them as full compliance policies.
- Before publication, confirm exact registry term semantics, policy-class suitability and duty timing against the current OpenREL specification.
