# Why OpenREL? Rationale and Context

>Wim Hugo, DANS/ EUDAT | [orcid:0000-0002-0255-5101](https://orcid.org/0000-0002-0255-5101)

>Melios Katsamakis, OpenAIRE | 

>Prodromos Tsiavos, OpenAIRE | 

>09-07-2026 | [CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

## The Landscape

The use of ***Licences*** to define aspects such as copyright, access conditions (if any), and obligations of and limitations on the user of a work is a common feature not only of the Research Data Management landscape, but generally applies to creative work or outputs that are produced for reuse and dissemination.

Licensing of creative works in the broader entertainment industry is a critical part of that business fabric, and was the original driver for the development of **ODRL** (Open Digital Rights Language) - a W3C standard that defines the concept of a ***Policy***: a container for the ***Rules*** (***Permissions***, ***Duties***, and ***Prohibitions***,) that the rights holder confers on those who want to use the work (***Asset***). ODRL is widely adopted in many industries and is actively maintained by the W3C. It is a natural baseline for any effort that aims to support rights management in the research domain.

>ODRL has some shortcomings, but by far and away the most significant one for practitioners and users involved in the research landscape is that it ***focuses on creator and intellectual property rights***, and is not easily used for the other rights (subject rights in particular) that may apply to the use of a work. More broadly, non-IP considerations such as ethical norms are also out of scope for ODRL.
>
>It has, as a result, become common practice to supplement a 'licence' for sensitive data with additional 'access conditions'.

Automated processing of access requests to sensitive data is one of the major bottlenecks facing automated research workflows becasue access conditions and limitations are not systematically encoded in licences and policies. As a result, requests almost always have to be adjudicated by a human agent: this is costly and slow. Moreover, sensitive data is often assumed to mean only personal data, given the prominence of GDPR in Europe. There is, however, many other categories of senstive data, including data that is commercially, environmentally, and culturally sensitive or has security implications. 

Encoding these considerations can be addressed in part by the **DPV** (Data Privacy Vocabulary) specification - also a W3C standard - that aligns strongly with GDPR. It provides a large set of vocabulary classes and concepts that can be used to encode a wide range of personal data definitions and scenarios, supplemented by a number of equally comprehensive extensions (Location, Legal and Jurisdiction, Purpose, Personal Data Categories, Technology Measures, and more). As a result, encoding sensitive personal data in machine-readable format is well supported.

>DPV cannot be used to describe the scope and nature of other sensitive data categories - doing so requires one or more similar sets of vocabulary that captures the considerations applicable to commercially, environmentally, and culturally sensitive data. DPV provides a conceptual framework for doing so, and one should aim to create any extensions in such a way that the computational logic required to process them is similar to that required for DPV.

Two additional vocabularies are specifically focused on encoding what is generally considered to be a 'licence': **CC** (Creative Commons) has defined a number of terms that are required to encode Creative Commons Licences, and **DALICC** (Data License Clearance Center), a now-concluded project, developed a supporting vocabulary and encoded upwards of 350 common licences using a combination of ODRL, CC, and their own vocabulary. The DALICC resources are no longer maintained, even thjought he project outputs remain available.

There are a number of additional vocabularies that are applicable to the context, but for brevity we highlight only two others: **DUO** (Data Use Ontology), which is specifically developed to define restrictions on data access in the bioinformatics and health domain, and **IDSC** (International Data Spaces Core vocabulary), which encodes the processes and protocols for trusted access and exchange of data resources between Data Space nodes. Clearly, both of these are applicable and reusable should one aim to automate the adjudication of access requests to resources - one of the core objectives of OpenREL.

>With the exception of DALICC (now defunct), none of the resources described above provides infrastructure and services - they are *specifications* and not *implementations*. This means that even if it is possible to encode a policy describing all of the permissions granted to, prohibitions on, and duties of the actors involved, finding and reusing that encoding is far from guaranteed. In the context of EOSC, such infrastructure is clearly necessary to simplify widespread use and adoption of encodings.

## Summary of OpenREL Design Considerations

![Scope Limitations of Existing Resources](/docs/guide/images/01-01.png)
***Figure 1.1 Scope Limitations of Existing Resources***

OpenREL aims to rectify the scope-related deficiencies and limit the diversity in the established resources for encoding and automated processing of Policies, based on the following considerations:

- Use ODRL as a foundational conceptual framework, and extend the classes, properties, and concept schemes already present as a means of addressing its scope limitations.
- Similary, DPV and 
