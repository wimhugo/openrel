# OpenREL Encoding Examples — Batch 4 (Source Sections 41–60)

**Status:** exploratory, bounded examples; not production-ready policy templates or legal advice. Source references are transcribed, not independently verified. No new OpenREL vocabulary terms are introduced.

**Source:** *F.65.3.6 EOSC-RML Policy Snippet Vocabulary* (uploaded DOCX). Vocabulary terms checked against uploaded OpenREL action and NamedConstraint files.

## Conversion overview

| Section | Source topic | Disposition |
|---|---|---|
| 41 | Research Misconduct Prevention | Deferred — external verification |
| 42 | Data Interoperability and Integration Rights | Converted (bounded subcase) |
| 43 | Responsible Use of AI in Research | Converted (overlap example) |
| 44 | Collaborative Open Science Projects | Existing-policy overlap |
| 45 | Ethical Data Governance in Open Science | Existing-policy overlap |
| 46 | Transparency in Research Funding and Outputs | Converted (bounded subcase) |
| 47 | Privacy and Data Protection Rights | Existing-policy overlap |
| 48 | Ethical Review and Approval Processes | Converted (overlap example) |
| 49 | Research Reporting and Accountability | Deferred — external verification |
| 50 | Governance of Cross-Border Research Projects | Converted (bounded subcase) |
| 51 | Standards for Open Data Reuse | Converted (overlap example) |
| 52 | Equitable Access to Research Resources | Deferred — governance/measurement |
| 53 | Research Infrastructure Sustainability | Deferred — infrastructure governance |
| 54 | Ethical Use of Research Metrics | Deferred — external verification |
| 55 | Public Engagement and Knowledge Dissemination | Existing-policy overlap |
| 56 | Training and Capacity Building in Open Science | Deferred — broad governance |
| 57 | Ethical and Inclusive Recruitment in Research | Deferred — legal/governance |
| 58 | Legal and Ethical Use of Research Funding | Deferred — external contractual rules |
| 59 | Intellectual Property Rights in Collaborative Research | Converted (bounded subcase) |
| 60 | Ethical Considerations in Research Partnerships | Existing-policy overlap / broad governance |

## Common prefixes

```turtle
@prefix openrel: <http://www.w3id.org/ns/openrel/0/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
```

Each Turtle example is a separate graph. Example assets are placeholder IRIs. NamedConstraints are references to registered instances; actual evaluation requires an implementation.

## Section 42 — Interoperable data integration with audit

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for ensuring interoperability and seamless integration of data across platforms, systems, and formats. It emphasizes the use of standardized protocols, metadata, and tools to promote collaboration and usability.
- Permissions: Lists allowed actions under data interoperability and integration, such as:
- Use Standardized Formats: Allowed to adopt and use standardized data formats to enhance compatibility.
- Integrate Data from Multiple Sources: Allowed to combine data from various systems for collaborative projects.
- Prohibitions: Lists prohibited actions, including:
- Ignore Standards: Not allowed to store or share data in non-standardized formats that hinder integration.
- Compromise Data Integrity During Integration: Not allowed to alter or misrepresent data when integrating from multiple sources.
- Obligations: Lists required actions, including:
- Adopt Metadata Standards: Researchers must use standardized metadata to facilitate data discovery and integration.
- Ensure Compatibility: Institutions must ensure data is compatible with commonly used tools and systems.
- Sources:
- FAIR Principles (GO FAIR Initiative):
- Description: Guidelines promoting Findable, Accessible, Interoperable, and Reusable data to support integration.
- Link: FAIR Principles
- W3C Standards for Data Interoperability:
- Description: Recommendations for ensuring data interoperability across web and research platforms.
- Link: W3C Interoperability Standards
- EOSC Data Interoperability Framework:
- Description: EOSC-specific guidance for promoting interoperability and seamless integration of research data.
- Link: EOSC Interoperability Framework

### Turtle template

```turtle
openrel:example-042 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/integration-input> ;
        odrl:action openrel:use, openrel:modify ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Authorises use and modification for integration; does not verify interoperability standards, metadata schemas, or transformation correctness.

## Section 43 — AI-assisted analysis subject to ethics approval

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for the ethical and responsible use of Artificial Intelligence (AI) in research activities. It emphasizes transparency, fairness, accountability, and compliance with ethical guidelines to ensure trustworthy AI applications.
- Permissions: Lists allowed actions under responsible AI use, such as:
- Use AI for Analysis: Allowed to employ AI tools for data analysis and research purposes, provided ethical standards are met.
- Develop Ethical AI Models: Allowed to design AI systems that align with transparency, inclusivity, and accountability principles.
- Prohibitions: Lists prohibited actions, including:
- Bias in AI Models: Not allowed to develop or deploy AI systems that introduce or perpetuate bias.
- Misuse AI: Not allowed to use AI for deceptive or harmful purposes in research.
- Obligations: Lists required actions, including:
- Ensure Explainability: Researchers must ensure that AI models and tools are explainable and understandable to relevant stakeholders.
- Audit for Compliance: Regular audits must be conducted to ensure AI systems comply with ethical and legal standards.
- Sources:
- OECD AI Principles:
- Description: Guidelines for the ethical and responsible use of AI, emphasizing transparency, accountability, and inclusivity.
- Link: OECD AI Principles
- EU AI Act Draft:
- Description: Proposed legislation regulating AI usage within the European Union, focusing on ethical AI development and deployment.
- Link: EU AI Act Draft
- EOSC Responsible AI Framework:
- Description: EOSC-specific guidance for ensuring the ethical use of AI in open science.
- Link: EOSC Responsible AI Framework

### Turtle template

```turtle
openrel:example-043 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/ai-analysis> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:ethicsApproval ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Strong overlap with section 23; included as a contrasting use-case, not a separate new rule pattern. No fairness, explainability, or bias assessment is encoded.

## Section 46 — Transparent dissemination of research outputs

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for ensuring transparency in research funding sources and outputs. It emphasizes accountability, openness, and adherence to ethical and legal standards to build trust and credibility in research.
- Permissions: Lists allowed actions under transparency in funding and outputs, such as:
- Disclose Funding Sources: Allowed to publicly disclose the sources of research funding.
- Share Research Outputs: Allowed to share research outputs openly to ensure public accessibility and trust.
- Prohibitions: Lists prohibited actions, including:
- Conceal Funding Sources: Not allowed to withhold information about research funding sources.
- Misrepresent Research Outputs: Not allowed to present research outputs in a misleading or deceptive manner.
- Obligations: Lists required actions, including:
- Provide Funding Transparency: Researchers must disclose all funding sources and any potential conflicts of interest.
- Ensure Open Access to Outputs: Researchers must make research outputs available in line with open access policies and agreements.
- Sources:
- OECD Guidelines on Research Transparency:
- Description: International recommendations for ensuring transparency in research funding and dissemination.
- Link: OECD Research Transparency
- UNESCO Open Science Recommendations:
- Description: Global framework for fostering openness and transparency in scientific research.
- Link: UNESCO Open Science
- EOSC Transparency Framework:
- Description: EOSC-specific guidance for promoting transparency in research funding and outputs in open science.
- Link: EOSC Transparency Framework

### Turtle template

```turtle
openrel:example-046 a openrel:ProcessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/research-output> ;
        odrl:action openrel:distribute ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

This encodes distribution and logging only. It does not require disclosure of funding sources or validate the accuracy of such disclosures.

## Section 48 — Research use gated by ethical review

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for conducting ethical reviews and obtaining approval for research projects. It emphasizes adherence to ethical standards, transparency, and accountability to protect participants and ensure integrity.
- Permissions: Lists allowed actions under ethical review and approval processes, such as:
- Submit Research for Ethical Review: Allowed to submit research proposals to ethics committees for evaluation.
- Implement Approved Protocols: Allowed to conduct research in accordance with approved ethical protocols.
- Prohibitions: Lists prohibited actions, including:
- Bypass Ethical Review: Not allowed to conduct research without undergoing an ethical review process.
- Deviate from Approved Protocols: Not allowed to make changes to research protocols without obtaining additional approval.
- Obligations: Lists required actions, including:
- Ensure Ethical Compliance: Researchers must comply with the guidelines and decisions of ethical review boards.
- Document Review Outcomes: Researchers must maintain records of ethical reviews and approvals as part of the project documentation.
- Sources:
- Declaration of Helsinki:
- Description: International ethical principles for research involving human subjects.
- Link: Declaration of Helsinki
- OECD Guidelines on Ethical Research Review:
- Description: Recommendations for implementing effective and transparent ethical review processes.
- Link: OECD Ethical Research Guidelines
- EOSC Ethical Review Framework:
- Description: EOSC-specific guidance for conducting and documenting ethical reviews in open science research.
- Link: EOSC Ethical Review Framework

### Turtle template

```turtle
openrel:example-048 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/ethics-reviewed-study> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:ethicsApproval ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Reuses the existing ethics-approval gate; cannot demonstrate that the actual protocol conforms to the approval, or that a review committee followed appropriate procedures. Overlaps section 8 and existing ethics policy.

## Section 50 — Controlled cross-border data distribution

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for managing and governing research projects that involve international collaboration. It emphasizes compliance with legal frameworks, ethical standards, and effective coordination across jurisdictions.
- Permissions: Lists allowed actions under cross-border research governance, such as:
- Collaborate Internationally: Allowed to establish partnerships with institutions across borders under mutual agreements.
- Share Data Across Jurisdictions: Allowed to share research data internationally, provided legal and ethical standards are met.
- Prohibitions: Lists prohibited actions, including:
- Ignore Local Regulations: Not allowed to conduct research activities without adhering to the laws of each participating country.
- Disregard Data Transfer Agreements: Not allowed to transfer data internationally without proper agreements in place.
- Obligations: Lists required actions, including:
- Ensure Legal Compliance: Researchers and institutions must comply with the laws and regulations of all involved jurisdictions.
- Foster Transparent Communication: Institutions must establish clear communication channels to coordinate activities across borders effectively.
- Sources:
- OECD Guidelines on Cross-Border Collaboration:
- Description: Recommendations for managing international research collaborations effectively and ethically.
- Link: OECD Cross-Border Collaboration
- General Data Protection Regulation (GDPR):
- Description: European Union regulation addressing the transfer of personal data across borders.
- Link: GDPR Overview
- EOSC Framework for International Research Projects:
- Description: EOSC-specific guidance for governing cross-border research initiatives in open science.
- Link: EOSC International Framework

### Turtle template

```turtle
openrel:example-050 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/cross-border> ;
        odrl:action openrel:distribute ;
        odrl:constraint openrel:managedAccess ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

Managed access is NOT a jurisdiction or transfer-law check. This does not enforce GDPR international-transfer conditions, adequacy decisions, SCCs, or institutional agreements.

## Section 51 — Open data reuse with attribution

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for ensuring that open data is reused ethically and effectively. It emphasizes adherence to licensing terms, proper attribution, and compliance with technical standards for interoperability.
- Permissions: Lists allowed actions under open data reuse, such as:
- Reuse Open Data with Attribution: Allowed to reuse open data provided proper attribution is given.
- Integrate Open Data into Research: Allowed to use open data in research projects, provided licensing terms are respected.
- Prohibitions: Lists prohibited actions, including:
- Ignore Licensing Terms: Not allowed to reuse open data in ways that violate its license.
- Misattribute Data Sources: Not allowed to use data without acknowledging the original source.
- Obligations: Lists required actions, including:
- Ensure Data Integrity: Researchers must ensure that reused data is accurate and unaltered in ways that could mislead.
- Document Data Sources: Researchers must document the sources of reused data to ensure transparency and reproducibility.
- Sources:
- FAIR Principles for Open Data:
- Description: Guidelines for ensuring that data is Findable, Accessible, Interoperable, and Reusable.
- Link: FAIR Principles
- Creative Commons Licensing Standards:
- Description: Framework for applying licenses to ensure ethical reuse of open data and resources.
- Link: Creative Commons Licenses
- EOSC Open Data Reuse Framework:
- Description: EOSC-specific guidance for promoting the reuse of open data in compliance with licensing and ethical standards.
- Link: EOSC Open Data Framework

### Turtle template

```turtle
openrel:example-051 a openrel:Licence ;
    odrl:permission [
        odrl:target <https://example.org/data/open-reuse> ;
        odrl:action openrel:use, openrel:derive ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:attribute ;
            odrl:constraint openrel:attribution ]
    ] .
```

### Interpretation and limitations

Likely duplicates existing attribution and reuse licences. This is a narrow illustrative variant; it does not enforce metadata or technical interoperability standards.

## Section 59 — Collaborative IP sharing with managed access

### Original narrative, rule summary and references

The following text is preserved from the source section (before its early JSON encoding):

- Description: Defines the rights and responsibilities for managing intellectual property (IP) in collaborative research projects. It emphasizes fairness, transparency, and adherence to agreements to ensure equitable distribution of IP rights among participants.
- Permissions: Lists allowed actions under IP management in collaboration, such as:
- Share Pre-existing IP: Allowed to share pre-existing intellectual property under agreed terms for collaborative use.
- Develop Joint IP: Allowed to create and manage jointly developed intellectual property with partners.
- Prohibitions: Lists prohibited actions, including:
- Claim Exclusive Ownership Without Agreement: Not allowed to claim sole ownership of jointly developed IP without explicit consent from all contributors.
- Use Collaborative IP Without Authorization: Not allowed to use intellectual property developed in the collaboration without mutual agreement.
- Obligations: Lists required actions, including:
- Establish IP Agreements: Collaborators must formalize IP ownership, use, and sharing agreements before the project begins.
- Respect Contributor Rights: Researchers must acknowledge and respect the contributions of all collaborators to jointly developed IP.
- Sources:
- WIPO Guidelines on Collaborative IP Management:
- Description: International recommendations for managing intellectual property in collaborative projects.
- Link: WIPO Collaborative IP Guidelines
- OECD Principles for Collaborative IP Sharing:
- Description: Guidance for equitable and transparent sharing of intellectual property rights in research collaborations.
- Link: OECD IP Sharing Guidelines
- EOSC IP Management Framework:
- Description: EOSC-specific guidance for managing intellectual property in open science collaborations.
- Link: EOSC IP Framework

### Turtle template

```turtle
openrel:example-059 a openrel:AccessRules ;
    odrl:permission [
        odrl:target <https://example.org/data/background-ip> ;
        odrl:action openrel:use ;
        odrl:constraint openrel:managedAccess ;
        odrl:duty [ a openrel:PostDuty ; odrl:action openrel:log ;
            odrl:constraint openrel:logUse ]
    ] .
```

### Interpretation and limitations

This only represents controlled use and an audit duty. It does not encode joint ownership, background/foreground IP allocations, licensing scope or contractual agreement validity.

## Deferred and overlapping sections

### Section 41 — Research Misconduct Prevention

**Disposition:** Deferred — external verification. Research misconduct requires evidence, investigations and determinations; logging alone is insufficient.

**Source description:** Defines the rights and responsibilities for preventing research misconduct, such as fabrication, falsification, plagiarism, or other unethical practices. It emphasizes fostering integrity, accountability, and adherence to ethical guidelines in research activities.

**Source references (as listed):**

- Singapore Statement on Research Integrity:
- Description: An international framework promoting integrity in research and providing guidelines for responsible conduct.
- Link: Singapore Statement
- OECD Best Practices for Research Integrity:
- Description: Guidelines for fostering integrity and addressing research misconduct.
- Link: OECD Research Integrity
- EOSC Research Integrity Framework:
- Description: EOSC-specific recommendations for promoting integrity and preventing misconduct in open science.
- Link: EOSC Research Integrity Framework

### Section 44 — Collaborative Open Science Projects

**Disposition:** Existing-policy overlap. Collaboration and sharing overlap sections 13, 25 and 37.

**Source description:** Defines the rights and responsibilities for participating in collaborative open science projects. It emphasizes inclusivity, transparency, and adherence to ethical and legal standards to foster equitable and productive collaborations.

**Source references (as listed):**

- UNESCO Open Science Guidelines:
- Description: International recommendations for fostering collaboration and inclusivity in open science initiatives.
- Link: UNESCO Open Science
- EOSC Collaboration and Open Science Framework:
- Description: EOSC-specific guidance for supporting and managing collaborative open science projects.
- Link: EOSC Open Science Framework
- OECD Principles for Research Collaboration:
- Description: Guidelines for promoting fairness, transparency, and equity in collaborative research practices.
- Link: OECD Research Collaboration

### Section 45 — Ethical Data Governance in Open Science

**Disposition:** Existing-policy overlap. Governed sharing and privacy overlap sections 15, 25 and 37.

**Source description:** Defines the rights and responsibilities for ethical data governance in open science. It emphasizes accountability, transparency, inclusivity, and compliance with legal and ethical standards for managing research data in open environments.

**Source references (as listed):**

- OECD Guidelines on Data Governance:
- Description: Recommendations for promoting ethical and effective data governance practices.
- Link: OECD Data Governance
- FAIR Principles for Data Governance:
- Description: Guidelines for implementing data governance practices that align with the principles of Findability, Accessibility, Interoperability, and Reusability.
- Link: FAIR Principles
- EOSC Ethical Data Governance Framework:
- Description: EOSC-specific guidance for ethical data governance in open science environments.
- Link: EOSC Data Governance Framework

### Section 47 — Privacy and Data Protection Rights

**Disposition:** Existing-policy overlap. Consent and privacy overlap sections 2, 15, 21 and 91.

**Source description:** Defines the rights and responsibilities for ensuring the privacy and protection of personal data in research. It emphasizes compliance with legal frameworks, ethical standards, and the implementation of safeguards to protect sensitive information.

**Source references (as listed):**

- General Data Protection Regulation (GDPR):
- Description: European Union regulation outlining requirements for the processing and protection of personal data.
- Link: GDPR Overview
- OECD Guidelines on Privacy and Data Protection:
- Description: Recommendations for ensuring the privacy and protection of personal data in research.
- Link: OECD Privacy Guidelines
- EOSC Data Protection Framework:
- Description: EOSC-specific guidance for compliance with privacy and data protection requirements in open science.
- Link: EOSC Data Protection Framework

### Section 49 — Research Reporting and Accountability

**Disposition:** Deferred — external verification. Accuracy of research reports and misreporting require evidence and assessment.

**Source description:** Defines the rights and responsibilities for accurate, transparent, and accountable reporting of research activities and outcomes. It emphasizes adherence to ethical standards, openness, and the responsibility to provide reliable and reproducible results.

**Source references (as listed):**

- COPE Guidelines for Research Reporting:
- Description: Ethical guidelines from the Committee on Publication Ethics (COPE) for transparent and accurate reporting in research publications.
- Link: COPE Guidelines
- OECD Principles on Research Accountability:
- Description: Recommendations for fostering accountability and transparency in research reporting.
- Link: OECD Research Accountability
- EOSC Reporting and Accountability Framework:
- Description: EOSC-specific guidance for reporting research activities and ensuring accountability in open science.
- Link: EOSC Reporting Framework

### Section 52 — Equitable Access to Research Resources

**Disposition:** Deferred — governance/measurement. Equity of access and non-discrimination require operational criteria and assessment.

**Source description:** Defines the rights and responsibilities for ensuring equitable access to research resources, including data, tools, and infrastructure. It emphasizes inclusivity, fairness, and the removal of barriers to access for underrepresented groups.

**Source references (as listed):**

- UNESCO Recommendations on Equity in Research Access:
- Description: Guidelines for promoting fairness and inclusivity in access to research resources.
- Link: UNESCO Equity Guidelines
- OECD Principles for Inclusive Research Access:
- Description: Recommendations for ensuring equitable access to research tools and infrastructure.
- Link: OECD Inclusive Access
- EOSC Access and Inclusivity Framework:
- Description: EOSC-specific guidance for ensuring equitable access to resources in open science.
- Link: EOSC Access Framework

### Section 53 — Research Infrastructure Sustainability

**Disposition:** Deferred — infrastructure governance. Sustainability and maintenance require measurable service obligations.

**Source description:** Defines the rights and responsibilities for ensuring the long-term sustainability of research infrastructure, including digital tools, platforms, and physical resources. It emphasizes proactive maintenance, sustainable funding, and efficient resource utilization.

**Source references (as listed):**

- OECD Guidelines on Infrastructure Sustainability:
- Description: Recommendations for ensuring the long-term sustainability of research infrastructure.
- Link: OECD Infrastructure Sustainability
- UNESCO Sustainability Framework for Research Infrastructure:
- Description: Global guidelines for maintaining sustainable research environments.
- Link: UNESCO Sustainability Framework
- EOSC Infrastructure Sustainability Framework:
- Description: EOSC-specific guidance for sustaining digital and physical research infrastructures in open science.
- Link: EOSC Sustainability Framework

### Section 54 — Ethical Use of Research Metrics

**Disposition:** Deferred — external verification. Metrics manipulation and responsible use need verifiable assessment criteria.

**Source description:** Defines the rights and responsibilities for using research metrics ethically and transparently. It emphasizes fairness, accountability, and adherence to best practices to avoid misuse or misrepresentation of research performance.

**Source references (as listed):**

- Leiden Manifesto for Research Metrics:
- Description: Principles for the responsible use of research metrics in the evaluation of research performance.
- Link: Leiden Manifesto
- DORA (San Francisco Declaration on Research Assessment):
- Description: Guidelines promoting the use of qualitative assessment methods over inappropriate reliance on journal-based metrics.
- Link: DORA Declaration
- OECD Best Practices for Research Evaluation:
- Description: Recommendations for ethical and effective evaluation of research using metrics.
- Link: OECD Research Evaluation

### Section 55 — Public Engagement and Knowledge Dissemination

**Disposition:** Existing-policy overlap. Public dissemination overlaps sections 16, 28 and 46.

**Source description:** Defines the rights and responsibilities for engaging the public and disseminating research knowledge effectively. It emphasizes transparency, accessibility, and inclusivity to ensure that research benefits society.

**Source references (as listed):**

- UNESCO Guidelines on Public Engagement in Science:
- Description: Global recommendations for fostering public involvement and understanding in scientific research.
- Link: UNESCO Public Engagement
- OECD Best Practices for Science Communication:
- Description: Recommendations for effective communication of research to the public and policymakers.
- Link: OECD Science Communication
- EOSC Public Engagement Framework:
- Description: EOSC-specific guidance for integrating public engagement into research dissemination efforts.
- Link: EOSC Engagement Framework

### Section 56 — Training and Capacity Building in Open Science

**Disposition:** Deferred — broad governance. Training and capacity building need a concrete resource and duty scope.

**Source description:** Defines the rights and responsibilities for providing training and building capacity in open science. It emphasizes skill development, inclusivity, and the promotion of open science principles among researchers and stakeholders.

**Source references (as listed):**

- UNESCO Recommendations on Open Science Education:
- Description: Guidelines for fostering education and capacity building in open science.
- Link: UNESCO Open Science Education
- OECD Framework for Research Training:
- Description: Recommendations for enhancing research training and capacity building globally.
- Link: OECD Research Training
- EOSC Skills and Training Framework:
- Description: EOSC-specific guidance for training and skill development in open science.
- Link: EOSC Skills Framework

### Section 57 — Ethical and Inclusive Recruitment in Research

**Disposition:** Deferred — legal/governance. Recruitment discrimination and fairness need jurisdictional and assessment context.

**Source description:** Defines the rights and responsibilities for ensuring ethical and inclusive recruitment practices in research. It emphasizes fairness, diversity, transparency, and compliance with ethical and legal standards.

**Source references (as listed):**

- UNESCO Guidelines on Diversity in Research Recruitment:
- Description: International recommendations for fostering diversity and inclusivity in recruitment practices.
- Link: UNESCO Diversity Guidelines
- OECD Best Practices for Inclusive Hiring:
- Description: Recommendations for ethical recruitment practices that promote equity and fairness.
- Link: OECD Inclusive Hiring
- EOSC Recruitment and Diversity Framework:
- Description: EOSC-specific guidance for ethical and inclusive recruitment in open science projects.
- Link: EOSC Recruitment Framework

### Section 58 — Legal and Ethical Use of Research Funding

**Disposition:** Deferred — external contractual rules. Approved budget, expense categories and funder permissions need agreement-specific constraints.

**Source description:** Defines the rights and responsibilities for ensuring the legal and ethical use of research funding. It emphasizes accountability, transparency, and adherence to the terms set by funding bodies to promote trust and efficiency.

**Source references (as listed):**

- OECD Principles for Financial Accountability in Research:
- Description: Recommendations for promoting ethical and efficient use of research funding.
- Link: OECD Financial Accountability
- UNESCO Guidelines on Research Funding Ethics:
- Description: International guidance for ensuring ethical use of research grants and funds.
- Link: UNESCO Research Funding Guidelines
- EOSC Funding Accountability Framework:
- Description: EOSC-specific guidance for managing and reporting the use of research funding.
- Link: EOSC Funding Framework

### Section 60 — Ethical Considerations in Research Partnerships

**Disposition:** Existing-policy overlap / broad governance. Ethical partnership overlaps collaborative governance and agreements.

**Source description:** Defines the rights and responsibilities for fostering ethical and equitable research partnerships. It emphasizes transparency, mutual respect, and adherence to ethical principles to ensure fair collaboration among all stakeholders.

**Source references (as listed):**

- UNESCO Principles for Ethical Research Partnerships:
- Description: International guidance for ensuring fairness and ethics in research collaborations.
- Link: UNESCO Ethical Partnerships
- OECD Guidelines for Research Collaboration:
- Description: Recommendations for fostering equitable and ethical partnerships in research.
- Link: OECD Research Collaboration
- EOSC Partnership Ethics Framework:
- Description: EOSC-specific guidance for managing ethical considerations in research partnerships.
- Link: EOSC Ethics Framework

## Quality and modelling notes

- All seven snippets passed RDFLib Turtle syntax parsing individually. This does not establish SHACL or ODRL Profile conformance.
- Sections 43, 48 and 51 are intentionally identified as overlapping examples. They may be removed in a deduplicated publication catalogue.
- `openrel:managedAccess` does not itself imply legal authorisation for international transfer.
- Duties and named constraints require external evaluators and evidence to be operationally meaningful.
- No assertions of legal or ethical compliance follow from the existence of these RDF triples.
