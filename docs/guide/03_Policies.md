## Policies

>Wim Hugo, DANS/ EUDAT | 

>Melios Katsamakis, OpenAIRE | 

>Prodromos Tsiavos, OpenAIRE | 

>09-07-2026 | 

>[CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

## Summary

ODRL defines Policy subclasses, but the semantics largely aim to describe the *life cycle role* of a Policy rather than its narrower specialisation in terms of content or origin. For this reason, OpenREL extends the Policy (Set) Class with the ***Licence***, ***Access Rule***, and ***Process Rule*** subclasses. It also affords the capability to evaluate access requests based on a combination of policy, licence, access, and process rules. To support this requirement, OpenREL  defines a new subclass of Policy (***Negotiation***) that allows one or more Policy instances to be combined by reference in a single instance, and/ or for a record of combination or request/offer outcomes to be recorded.

[RDF Turtle representation](https://github.com/wimhugo/openrel/blob/main/.openrel/vocabs/openrel/policies.ttl)

## Context

A Policy is the foundational class defined in ODRL for encoding of sets of rules (permissions, prohibitions, and duties), and can be elaborated with constraints.

A Policy allows a number of properties to be defined, and it can be made into a custom policy for a very specific Asset (e.g. a specific dataset), and made applicable to a very specific Party (e.g. an individual or institution).

ODRL defines a sumber of sub-classes for a Policy, and these are:

| ODRL Policy subclass | Main intent                                                                                                                                  | Typical issuer                          | Example                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `odrl:Set`           | A generic collection of permissions, prohibitions and duties. This is the default policy type when no more specific semantics are required.  | Anyone                                  | A licence allowing users to use and derive a dataset provided attribution is given.                                                |
| `odrl:Offer`         | An offer of rights that another party may choose to accept, often leading to an agreement or contract.                                       | Rights holder or service provider       | "You may use this dataset commercially if you purchase a licence."                                                                 |
| `odrl:Agreement`     | A policy that records mutually agreed rights and obligations between parties.                                                                | Contracting parties                     | A signed data sharing agreement between a university and a pharmaceutical company.                                                 |
| `odrl:Request`       | A request for permission or rights from another party. It expresses what the requester wishes to obtain rather than what is already granted. | Requester                               | A researcher requests permission to use a restricted dataset for cancer research.                                                  |
| `odrl:Ticket`        | A token or credential proving that specific rights have already been granted. Often generated following an Offer or Agreement.               | Rights issuer                           | A download token permitting access to a licensed dataset until a specified expiry date.                                            |
| `odrl:Privacy`       | A policy describing permissions, prohibitions and obligations relating to the processing of personal data.                                   | Data controller                         | A GDPR privacy notice stating that personal data may be processed only for research purposes and must be deleted after five years. |
| `odrl:Assertion`     | A statement by a party asserting that certain permissions, prohibitions or duties apply. It represents a claim rather than an agreement.     | Rights holder, repository, or authority | A repository asserts that all deposited software is licensed under the MIT Licence and may be redistributed.                       |

These Policy subclasses, with the exception of the Privacy and Assertion Policies, are aimed at encoding the life cycle of contracting between parties. Moreover, it is intended to support an open negotiation in cases where predefined Policies applicable to an Asset do not exist. They are specialisations of odrl:Policy based on the *role the policy plays*, rather than the *rights it expresses*. They do not change the semantics of permissions, prohibitions, duties, or constraints - they provide context for how the policy is intended to be used, and they are orthogonal to the semantics of the other (non-IP) rights that OpenREL, DUO, DPV, and similar vocabularies encode.

A **typical life cycle** may include:

1. A request in respect of an Asset by an Assignee is encoded as a *Request Policy* and forwarded to the Assigner. This request may include permissions, for example, that the Assigner may or may not grant. (The scope of permissions could already be published for the Asset in an existing Policy). A Request Policy may include some of the elements of *User Context* defined by OpenREL, more about that later.
2. The Assigner produces an *Offer*, which may or may not grant all of the permissions requested, contain additional prohibitions and duties, and impose constraints. In the context of research data management use cases, this Offer Policy is equivalent to a standardised licence applicable to an Asset Collection (e.g. all our publicly available non-senstive data is subject to a CC BY 4.0 licence).
3. If a negotiation (automated or manual) is successful, this match can be encoded in an *Agreement* Policy. The Agreement is specific: it describes the Assignee, the Assigner, and the Asset unambigously, and as such, may be viewed as a custom instance of a general licence applicable to an Asset Collection. FOr example, sensitive data licences may be created as a general template, but require that the specific Asset, Assigner and Assignee be recorded in a custom licence agreement with only that scope.
4. A *Ticket* encodes specific rules in auch a way that it can be used in practical terms - for example, defining the number of times an Asset may be accessed, and being updated every time that an access event occurs.

## Motivation for Additional Subclasses

OpenREL has defined four additional Policy subclasses, and each of these have a specialisation that is not addressed by existing IDRL classes and subclasses.
 

| OpenREL Policy subclass | Uniqueness Criterion | Motivation                                                                                                                                 | Typical issuer                          | Example                                                                                                                            |
| -------------------- | -------------------- |-------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|Licence|Unique to all Assets of the same class or type|A ***Licence*** Policy subclass introduces additional properties that are not typically applicable to other Policy subclasses, and takes its broad scope from the properties associated specifically with licences. It could be viewed as a special case (non-negotiable) of an Offer or an Agreement that will not be modified. | Could be the rights holder, repository, or authority. Generally applicable, but Agreements may be made that are specific in terms of the Asset, Assignee, and Assigner.|SPDX, for example, makes a distinction between the legal, human-readable, and machine-readable representations of a licence, and in some cases, such licences are legally enforceable in a specific jurisdiction (for example, in the case of some Creative Commons licences).|
|Access Rule(s)| Unique to a Data Subject, repository, or institution|***Access Rules*** define conditions of access that are not generally considered to be part of a licence, but depends on the context. Such access rules may include, for example, the terms and conditions of use associated with a specific repository, data service, or institution. It may also encapsulate the requirements of the data subject(s) and encode their consent. It is usually policy-driven.| Repository, institution, or authority - usually the entity hosting the Asset.| An institution may require anyone interested in using an Asset to assent to its terms and conditions of use of the institution's services - clearly these are not part of a licence, and could be different for each insititution.|
|Process Rule(s)| Unique to a software platform or dissemination channel|***Process Rules*** are formalities associated with the process of gaining access that do not concern access or licences, but are, for example, related to *interaction of a software platform or dissemination channel with an Assignee*. |The institution or software developer| A dissemination channel could, for example, have different rate limits applicable to human and machine users. It does not preclude access, and does not form part of the licence, but it determines in practical terms whether access is possible at a agven moment. Likewise, there could be a requirement to register in a software platform for purposes of maintaining a profile, preferences, and settings prior to allowing downloads. |
Negotiation|Often unique to repositories, but anyone can create and persist a Negotiation. |This Policy subclass captures additional metadata that contextualises a combination of other Policies that it includes by reference, either in terms of compatibility, and/ or in terms of the reason for collective reference.|Usually the repository or platform offering the Asset|For example, capturing the reasons a request for access was refused, or whether two input Policies are compatible.|

## Encoding User Context

User context broadly refers to the characterisation of the user (requestor, Assignee), and OpenREL makes explicit provision for encoding this, since it forms an important part of determining whether access can be granted - especially for sensitive data.

OpenREL provides vocabulary to encode several categories of user context, for example:

1. Researcher status: verification of user status, based on a number of verification methods.
2. Affiliation (with an academic or research-performing organisation).
3. Organisation type - non-profit, for-profit, or academic, and whether it performs research and development or not.

Using OpenREL vocabulary, user context can be encoded as one or more constraints with resolved Right Operands and persisted as an Assertion Policy that is unique to the end user. These can be included into Requests, and matched with an Offer or an existing Rule Set to determine compliance. It can be used pre-emptively to filter Rule Sets (policies, licences, access rules, process rules, and other combinations of rules) so that end users understand what types of Assets and Asset collections are available to them. A specific use case involves filtering of catalogue content to reflect whether access will be possible, and what should be changed to gain access in cases where it will not currently be possible.

## Negotiation

A ***Negotiation*** allows the combination of Policy instances (which can be of any Policy subclass) into a single instance. There are three use cases for this:

1. **Record of Negotiation**: As described above, a negotiation between parties to arrange access to and use of an Asset may require several inputs and outputs, including a Request, an Offer, an Agreement, and any number of Tickets. It may be convenient to reference all of these artefacts in a single instance for record purposes, and especially if the negotiation was a failure, to keep record of the reasons why this was the case.
2. **Ease of Processing**: In some cases, access or use will depend on satisfying the constraints included in a Licence, Access Rules, and Process Rules, and finding all of these via the Asset reference may be cumbersome. The ***Negotiation*** allows combination of references to all of these instances to assist with processing and verification of compatibility. In some cases, the record of such incompatibility will be useful.
3. ***Licence Combinations***: The Policies (especially Licences) applicable to two or more input Assets that are used in the creation of a derived Asset may not be compatible, and a record of such incompatibility is useful at times. The output from a combination of compatible Licences will be a new Licence applicable to the derived Asset.

A Policy Collection has the same properties as a Policy, and in addition, must include a new property to indicate at least one constitutent Policy. This is reformulated as openrel:hasPolicy, based on the odrl:hasPolicy property. This property is related to the odrl:inheritFrom property, but since the inheritance direction is reversed, a new property is required. A policy Collection cannot be open-ended, and has to indicate the Asset Collection to which it applies. For example, a Policy Collection must specify the catalogue (asset collection) that it applies to in the context of an institution and its software platform(s). It corresponds to statements such as

>"This Policy Collection applies to all datasets containing personal data, hosted by [Institution] in its [Repository] using [Software Platform]".

>"This Policy Collection references all policy instances describing the negotiation for access to [Asset/ Asset Collection] requested by [Assignee] and granted by [Assigner]".

## Summary of Policy Classes and Subclasses

Figure 3.1 shows the scope of Policy subclasses available in OpenREL, and their main relationships and context. 

![Policy Classes and Subclasses](/docs/guide/images/03-01.png)
***Figure 3.1 Policy Classes and Subclasses***

### Application of Policy Subclasses: Assertions

- Any Party can assert a set of rights (Assertion), and these can be very general (I am a verified researcher) to very specific (I am the creator and rights owner for this work/ Asset). The Parties do not have to be individuals or organisations, but can be Groups or Agents (Party Collections), such as ‘End Users’ or ‘Rights Owners’ or ‘Data Subjects’ or ‘Curators’.
- Each of these Parties Party Collections can, in practice, express these Assertions in specific ways:
 - Data Subjects can predefine the terms of access to sensitive data (Asset), including aspects such as use only for a defined purpose, and that only a subset of the data (through minimisation or a specific qualification of data elements) is available to end users.
 - Rights Holders can assert their rights over an Asset in a predefined manner, for example the right to grant use of the asset, set conditions for use, and to earn income from it.
 - Repositories and Curators can predefine their rights by way of Assertions, such as the right to modify data and metadata, create derived Assets, and so on.
 - Platforms have rights and rules, and could for example require more stringent or different identification of end users that that required by a repository, or impose additional notification duties,
 - End Users can assert context or credentials, for example that theta re a researcher or affiliated with a research institution.

### ODRL and Agreements

ODRL is specifically designed to allow an Agreement (subclass of Policy) to be reached between a Party that wants to Use an Asset (if agreed, that Party becomes the Assignee), and the Party that is the rights holder or acts on behalf of the rights holder (this Party becomes the Assigner). 

To support this negotiated Agreement, a Request can be compiled by the future Assignee, and an Offer may be made in response by the rights holder. Both a Request and an Offer are also Policy subclasses, and the arbitrated result of these two inputs becomes an Agreement.

ODRL is very specific that the Request, Offer, and Agreement instances MUST include the Assignee, the Assigner, and the Asset (or Collections of these), since it is specific to the negotiation. 

Moreover, the Agreement may set out the negotiated Permissions, Prohibitions, and Duties, but need not be specific in respect of some Constraints. To enable an Agreement to be reused multiple times after reconfirmation, for example, one can create a Ticket based on the Agreement as a ‘parent’ Policy.  This Ticket (also a Policy subclass) can, for example, specify an end date for itself, after which a new Ticket needs to be created based on the Agreement for continued Use of the Asset.

Using these to enact a negotiated workflow is straightforward, and since a Policy can reference another ‘parent’ Policy, maintaining provenance links is simple. 

This default workflow, with other options enabled by OpenREL extensions, is shown in Figure 3.2.

![OpenREL-enabled Negotiation Workflows and Records](/docs/guide/images/03-02.png)
***Figure 3.2 OpenREL-enabled Negotiation Workflows and Records***

### The Role of an OpenREL Licence Subclass

By requiring that the Assigner, Assignee, and Asset be specified in the Offer subclass, ODRL limits its application in the context of what is commonly understood to be a software, scholarly publication, or dataset ‘licence’. Examples of these include MIT and GNU licences for software, and the CC BY and CC BY NC licences that are often used for datasets and articles. 

These licences are ‘open-ended’, in that they do not specifically identify the Asset, Assignee, or Assigner, even though they might do so indirectly. For example, the Asset is indirectly indicated by pasting the text of the MIT Licence into source code, or by indicating the licence in metadata for a dataset or publication. Such licences cannot be encoded in ODRL using existing subclasses because of the lack of specificity. 

OpenREL addresses this gap by defining an additional subclass of Policy - the openrel:Licence subclass. A Licence can, in the typical negotiated workflow, take the place of the Offer, in the sense that it is non-negotiable. If the Request from the future Assignee does not match the Rules of the Licence, an Agreement is not possible.
In many real-life situations, an Agreement is not always necessary (although some repositories might record assent to the Licence from the Assignee), and a Ticket may not be required.

Many datasets are published with Licences that require Attribution, and it may be useful to capture the fact that a given Party already agrees to such a Duty in a Request, which means that automated matching can be done, and that there is no need to record assent to the Licence except as a record of a Negotiation. 

The mid-section of Figure 3.2 shows this typical workflow.

### Records of Negotiations

The Agreement subclass is designed to capture the results of a negotiation between Parties, but lacks the ability to record metadata about that negotiation. By definition, rejected Requests do not end up in Agreements, and as such, there will be no record of them.

OpenREL adds a subclass that is a specialisation of odrl:Agreement, called an openrel:Negotation. This subclass can record additional metadata about a negotiated Agreement (or ‘disagreement’), and by definition contains records of unsuccessful Requests and the reason(s) why they were not successful. 

Such ‘disagreements’ will be much more common in cases where a Request is evaluated against a Licence, since a Licence is not negotiable. 

Negotiation instances also encode two other cases:

1. The combined outcome of one or more Licences, Access Rules, and Process Rules that apply in a given context. It might be a common occurrence for this negotiation to fail, for example if Access Rules satisfying a Data Subjects requirements do not match the Licence applied to the Asset.
2. The combination of a number of input Policies (typically Licences) that are associated with Assets that are combined into a new derived Asset, since if these input Policies cannot be merged, it is technically not feasible to create the derivation since it cannot be licenced (no Policy can be formulated that satisfies the rules of all input Policies). The outcome of this negotiation is either a new combined Licence, or a Negotiation record of the incompatibility.

The righht-hand panel in Figure 3.2 shows this workflow.

In practice there will likely be a very large number of Negotiation instances and these are not centralised or even federated, and hence will be accessible only locally (for example, in repository records). The exception will be generalised Negotiation instances that are quite common - we will discuss these in more detail later on.






