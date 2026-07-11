# Constraints and Named Constraints

>Wim Hugo, DANS/ EUDAT | 
>Melios Katsamakis, OpenAIRE | 
>Prodromos Tsiavos, OpenAIRE | 
>09-07-2026 | 
>[CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

## Context 

ODRL makes provision for the description of a *Constraint*, and such a Constraint can have a UID, which by implication allows them to become nodes in a graph that can be referenced by *Actions* in *Rules*.

This approach is useful, because some instances of Constraints (for example, that any number of Use-related subclasses are acceptable for non-commerical purposes) occur in many policies and licences, and one would like to avoid duplication and ensure consistent encoding of these Constraints. From this perspective, one should avoid the option that allows repetitive local definition of a Constraint wherever it is required.

Moreover, referenceable and reusable constraints are far simpler to incorporate into *Logical Constraints* - those that have to be satisfied together, or in sequence, and so on.

The approach has its downsides, in that a policy or licence is not composed in a single location, but finds its rule content spread in a graph. If all policies and licences are contained in the same graph, this is OK, but if it is spread over many graphs, it becomes cumbersome to complile the machine-readable version of a policy or licence - even though it is technically possible.

We will follow a hybrid approach in OpenREL, by defining a set of '**Named Constraints**' - Constraints that can be referenced via IRI and extend the properties of the ODRL Constraint class. These Named Constraints assist with consistent implementation of encodings that are commonly used and/ or are complex to create, and can be easily referenced as Logical Constraints.

## Class Definitions

The ODRL Constraint Class is defined as follows:

```
:Constraint
	a rdfs:Class, owl:Class, skos:Concept ;
	rdfs:isDefinedBy odrl: ;
	rdfs:label "Constraint"@en ;
	skos:definition "A boolean expression that refines the semantics of an Action and Party/Asset Collection or declare the conditions applicable to a Rule."@en .
```

The OpenREL NamedConstraint Class extends this :

```
openrel:NamedConstraint
	a rdfs:Class, owl:Class, skos:Concept ;
  	rdfs:subClassOf odrl:Constraint ;
  	rdfs:isDefinedBy openrel: ;
	rdfs:label "Named Constraint"@en ;
  	skos:definition "A subclass that extends the properties of the ODRL Constraint Class."@en ;
	skos:note "ODRL: A boolean expression that refines the semantics of an Action and Party/Asset Collection or declare the conditions applicable to a Rule."@en .
```

## Properties

The extension of properties is simple: providing a name and a description for the constraint are the most important extensions. These can easily be provided by existing and well-known properties.

|Property| IRI| Description|
|:-------|:-------|:-------|
|Constraint Name (Title)|rdfs:label|A suitable short label or title for the named constraint|
|Constraint Definition|skos:definition|A definition of the purpose and usage of the constraint|

There is a new property that is useful for some constraint definitions, and that is the ability to designate a target (IRL) for the fulfillment of the constraint. A very good example of this is offered by a variety of notification-related constraints, where the IRL can be utilised to identify the endpoint where notifications must be made. Similarly, a constraint may require adherence to a profile of measures, and these measures may be documented as a machine-readable resource at an external endpoint. To accommodate this, we define an additional (new) property for Named Constraints:

|Property| IRI| Description|
|:-------|:-------|:-------|
|Applicable Endpoint|openrel:applicableEndpoint|An endpoint that is used to fulfill the criteria of or inform the adherence to the named constraint.|

ODRL defines a target (odrl:target), but this property is semantically different - it is intended to define the target of the policy.

Named Constraints (and Constraints) can also be categorised in terms of the intent of the Constraint. This is useful for grouping Named Constraints for the purposes of understanding the scope of available instances. Since the category has no impact on the properties of the Named Constraint, OpenREL implements these categories as a Concept Scheme coupled to a property of Named Constraints: openrel:constraintType.

|Property| IRI| Description|
|:-------|:-------|:-------|
|Constraint Category|openrel:constraintType|A value from a vocabulary (Concept Scheme) that defines the named constraint category.|

## Named Constraint Types

The Named Constraint Types that can be used for categorisation are defined in a [Concept Scheme](https://github.com/wimhugo/openrel/blob/main/.openrel/vocabs/openrel/type_constraint.ttl), and summarised below.

|Concept| IRI| Description|Example Vocabulary|
|:-------|:-------|:-------|:---------|
|Role|openrel:role|Named Constraint defined on the basis of an Agent Role|[Agent Types](../../.openrel/vocabs/openrel/type_agent.ttl)|
|Usage|openrel:usage|Constraint defined on the basis of usage characteristics.|[Usage Types](../../.openrel/vocabs/openrel/type_usage.ttl)|
|Access|openrel:access|Constraint defined on the basis of allowable access types.|[Access Types](../../.openrel/vocabs/openrel/type_access.ttl)|
|Purpose|openrel:purpose|Purpose-based Constraints may apply to any Action.| [Purpose Types](../../.openrel/vocabs/openrel/type_purpose.ttl)|
|Notification|openrel:notification|Constraint defined for elaboration of notification duties.|[Notification Target Types](../../.openrel/vocabs/openrel/type_notification-target.ttl)|
|Consent|openrel:consent|Constraint defined for definition of consent-related duties.|[Consent Types](../../.openrel/vocabs/openrel/type_consent.ttl)|
|Context|openrel:context|Constraint defined for definition of agent-related context.|[Context Types](../../.openrel/vocabs/openrel/type_context.ttl)|
|Technical and Organisation Measures|openrel:tom|onstraint defined for definition of technical, organisational, legal, and physical measures required to safeguard sensitive data.|[TOM Types](../../.openrel/vocabs/openrel/type_tom.ttl)|






