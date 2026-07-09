## Policies

Wim Hugo, DANS/ EUDAT
Melios Katsamakis, OpenAIRE
Prodromos Tsiavos, OpenAIRE
09-07-2026
[CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)

## TL;DR 

ODRL defines policy subclasses, but these define semantics largely to describe the ***life cycle role*** of a Policy rather than its narrower specialisation in terms of content, and for this reason, OpenREL extends the Policy (Set) Class with the Licence, Access Rule, and Process Rule subclasses. It also affords the capability to evaluate access requests based on a combination of policy, licence, access, and process rules.

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

These Policy subclasses, with the exception of the Privacy and Assertion Policies, are aimed at encoding the life cycle of contracting between parties. It is intended to also support an open negotiation in cases where predefined Policies applicable to an Asset do not exist. They are specialisations of odrl:Policy based on the *role the policy plays*, rather than the *rights it expresses*. They do not change the semantics of permissions, prohibitions, duties, or constraints - they provide context for how the policy is intended to be used, and they are orthogonal to the semantics of the other (non-IP) rights that OpenREL, DUO, DPV, and similar vocabularies encode.

A **typical life cycle** may include:

1. A request in respect of an Asset by an Assignee is encoded as a *Request Policy* and forwarded to the Assigner. This request may include permissions, for example, that the Assigner may or may not grant. (The scope of permissions may already be published for the Asset in an existing Policy). A Request Policy may include some of the elements of *User Context* defined by OpenREL, more about that later.
2. The Assigner produces an *Offer*, which may or may not grant all of the permissions requested, contain additional prohibitions and duties, and impose constraints. In the context of research data management use cases, this Offer Policy is equivalent to a standardised licence applicable to an Asset Collection (e.g. all our publicly available non-senstive data is subject to a CC BY 4.0 licence).
3. If a negotiation (automated or manual) is successful, this match can be encoded in an *Agreement* Policy. The Agreement is specific: it describes the Assignee, the Assigner, and the Asset unambigously, and as such, may be viewed as a custom instance of a general licence applicable to an Asset Collection. FOr example, sensitive data licences may be created as a general template, but require that the specific Asset, Assigner and Assignee be recorded in a custom licence agreement with only that scope.
4. A *Ticket* encodes specific rules in auch a way that it can be used in practical terms - for example, defining the number of times an Asset may be accessed, and being updated every time that an access event occurs.

## Motivation for Additional Subclasses

OpenREL has defined three additional Policy subclasses, and each of these have a specific specialsiation that cannot be addressed by existing IDRL classes and subclasses.


| OpenREL Policy subclass | Motivation                                                                                                                                 | Typical issuer                          | Example                                                                                                                            |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|Licence|A ***Licence*** Policy subclass introduces additional properties that are not typically applicable to other Policy subclasses, and takes its broad scope from the properties associated specifically with licences. | Generally applicable, but Agreements may be made that are specific.|SPDX, for example, makes a distinction between the legal, human-readable, and machine-readable representations of a licence, and in some cases, such licences are legally enforceable in a specific jurisdiction (for example, in the case of some Creative Commons licences).|







