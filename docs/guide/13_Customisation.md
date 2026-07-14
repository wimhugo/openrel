# Customising OpenREL

>Wim Hugo, DANS/ EUDAT | 
>Melios Katsamakis, OpenAIRE | 
>Prodromos Tsiavos, OpenAIRE | 
>09-07-2026 | 
>[CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

## Context

Vocabularies that can be used to encode rights-, access-, sensitive data-related policies and licences (e.g. ODRL, DPV, IDSC, DALICC, and ccREL) often entrench context-specific considerations into RDF Class Instances. The implication is that if a new context is identified or is different from what is encodable already, class instances have to be added to the vocabulary to accomodate the new context, spawning a new version and for stable vocabulries, with a potentially lengthy review and release process. Some examples are:

|Vocabulary|IRI|Description|Issue|
| -------- | -------- | -------- | -------- |
|ODRL| odrl:textToSpeech|To have a text Asset read out loud.|ODRL is relatively free of context-specific class instance definitions, with one or two exceptions - such as this one. It is just one of many possible transformations of content and should be made more flexible, since each context may want to encode a different set of applicable transformations|
|ccREL|cc:CommercialUse| Using the Work for commercial purposes.|This is just one of many potential ways in which revenue can be generated from disseminated, derived or modified Assets - it is, for example, also possible to have non-commercial revenue by recovering dissemination and packaging costs.|
|DALICC|dalicc:attributionNotice|Notification that attribution was done|Potentially just one of many notification duties, and these may well be very context-specific.|
|IDSC|idsc:AGGREGATE_BY_CONSUMER, idsc:AGGREGATE_BY_PROVIDER|Data will be part of another piece of data so that it is not distinguishable anymore.|These two aggregation actions are modelled as different class instances, but it is an examle of a transformation action that can be accommodated as transformation types that use a context-specific vocabulary.|

To address this, OpenREL introduces some recommended encoding patterns that are used by preference. Any ODRL-aligned pattern is acceptable, but we think that these specific patterms lead to greater flexinility and adaptibility for specific contexts.

## Design Patterns

### Assign Role Types to Duties

Duties are far more useful if it indicates the Party Collection or Party that is responsible for the Duty. OpenREL also introduces an additional property, and that is the ability to indicate a Role by way of a Role Type. Thesse Roles are aligned with Agent definitions that are common in the RDMI landscape, and are not necessarily apllicable in other contexts. The Role Type definitions are included in a Concept Scheme, and this allows the flexibility to define a context-specific Concept Scheme to address any differences without modifying Classes or Class Instances.

The applicatiuon of these options depend on the nature of the Policy that is being defined. In cases where the Policy subclass is equivalent to an Agreement (or a 'Contract') or an Assertion, being very specific is a necessity, and designating an Assignee as a specific Party is the best course of Action. For subclasses such as Offers or Licences, indicating the Party Collection is more appropriate, and standardising the Party Collection definitions using a Concept Scheme is good practice.

|Policy Subclass|Party Defined|Party Collection Defined|
|---------|---------|---------|
|Set|Not Applicable||
|Request|Assignee = IRI|Not Applicable|
|Offer|Assigner = IRI|Not Applicable|
|Agreement|Assignee = IRI, Assigner = IRI|Not Applicable|
|Ticket|Assignee = IRI, Assigner = IRI|Not Applicable|
|Privacy|Assignee = IRI, Assigner = IRI|Not Applicable|
|Assertion|Assignee = IRI|Not Applicable|
|Licence|Not Applicable|Role = Agent Type|
|Access Rules|Not Applicable|Role = Agent Type|
|Process Rules|Not Applicable|Role = Agent Type|
|Policy Collection|Inherited|Inherited|

