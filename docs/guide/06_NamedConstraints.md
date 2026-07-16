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

We will follow a hybrid approach in OpenREL, by defining a set of '**Named Constraints**' - Constraints that can be referenced via IRI and extend the properties of the ODRL Constraint class. These Named Constraints assist with consistent implementation of encodings that are commonly used and/ or are complex to create, and can be easily referenced in Logical Constraints.

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

## Scenarios

Scnearios are used to describe contextual information about the Asset or Asset Collection, the Party or Party Collection, the Assigner, or the Assignee. The primary use of Scenarios is to capture, in human-readable form, any conditions, limitations, duties, or contextual information that may influence the composition of or compliance with a Policy (Policy, Licence, Access Rules, Process Rules, Assertion, Offer, Agreement, Privacy, ...). The encoded language of these Policies are not easily interpreted by end users, and Scenarios are used to bridge this gap. Scenarios are defined in OpenREL as a hierarchy of instances in a [Concept Scheme](../../.openrel/vocabs/openrel/type_scenario.ttl) (vocabulary). 

Some examples will be useful: 

- An end user may be affiliated with a Research Performing Organisation (university, research institute, commercial research organisation) and sometimes apply derived results for commercial gain. This end-user context can be defines as one or more Scenario statements (instances) that are mapped to Named Constraints to indicate how such a Scenario is encoded in practice.
- Assets created by a project may have to be published as Open or Managed Access because it is funded publicly by the Horizon Europe project and does not contain any sensitive information.

To map Scenarios to Named Constraints, we add a property as follows:

|Property| IRI| Description|
|:-------|:-------|:-------|
|Scenario|openrel:scenario|A value from a vocabulary (Concept Scheme) that defines the applicable scenario(s) for the Named Constraint.|

## Named Constraint Types

The Named Constraint Types that can be used for categorisation are defined in a [Concept Scheme](https://github.com/wimhugo/openrel/blob/main/.openrel/vocabs/openrel/type_constraint.ttl), and summarised below. Each of these constraint types, in turn, can make use of a default (example) vocabulary to further qualify the constraint. This aspect delivers significant flexibility and customisability, since implementors of OpenREL are free to subsititute or expand these vocabularies.

The vocabularies are significant interoperability resources, since many of the concepts defined in them are mapped to or originally defined in vocabularies that are focused on the same topic, such as DPV, IDSC, DUO, and the like.

|Concept| IRI| Description|Example Vocabulary|
|:-------|:-------|:-------|:---------|
|Role|openrel:role|Named Constraint defined on the basis of an Agent Role|[Agent Types](../../.openrel/vocabs/openrel/type_agent.ttl)|
|Usage|openrel:usage|Constraint defined on the basis of usage characteristics.|[Usage Types](../../.openrel/vocabs/openrel/type_usage.ttl)|
|Access|openrel:access|Constraint defined on the basis of allowable access types.|[Access Types](../../.openrel/vocabs/openrel/type_access.ttl)|
|Purpose|openrel:purpose|Purpose-based Constraints may apply to any Action.| [Purpose Types](../../.openrel/vocabs/openrel/type_purpose.ttl)|
|Notification|openrel:notification|Constraint defined for elaboration of notification duties.|[Notification Target Types](../../.openrel/vocabs/openrel/type_notification-target.ttl)|
|Consent|openrel:consent|Constraint defined for definition of consent-related duties.|[Consent Types](../../.openrel/vocabs/openrel/type_consent.ttl)|
|Context|openrel:context|Constraint defined for definition of agent-related context.|[Context Types](../../.openrel/vocabs/openrel/type_context.ttl)|
|Technical and Organisation Measures|openrel:tom|Constraint defined for technical, organisational, legal, and physical measures required to safeguard (usually sensitive) data.|[TOM Types](../../.openrel/vocabs/openrel/type_tom.ttl)|






