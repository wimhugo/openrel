# Named Constraints

ODRL makes provision for the description of a *Constraint*, and such a Constraint can have a UID, which by implication allows them to become nodes in a graph that can be referenced by *Actions*.

This approach is useful, because some instances of Constraints (for example, that any number of Use-related subclasses are acceptable for non-commerical purposes) occur in many policies and licences, and one would like to avoid duplication and ensure consistent encoding of these Constraints. From this perspective, one should avoid the option that allows repetitive local definition of a Constraint wherever it is required.

Moreover, referenceable and reusable constraints are far simpler to incorporate into Logical Constraints - those that have to be satisfied together, or in sequence, and so on.

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

The extension of properties is simple: providing a name and a description for the constraint is the most important extension. These can easily be provided by existing and well-known properties.

|Property| IRI| Description|
|:-------|:-------|:-------|
|Constraint Name (Title)|rdfs:label|A suitable short label or title for the named constraint|
|Constraint Definition|skos:definition|A definition of the purpose and usage of the constraint|

There is a new property that is udeful in some constraint definitions, and that is the ability to designate a target (IRL) for the fulfillment of the constraint. A very good example of this is offered by a variety of notification-related constraints, where the IRL can be utilised to identify the endpoint where notifications must be made. Similarly, a constraint may require adherence to a profile of measures, and these measures may be documented as a machine-readable resource at an external endpoint. To accommodate this, we define an additional (new) property for Named Constraints:

|Property| IRI| Description|
|:-------|:-------|:-------|
|Applicable Endpoint|openrel:applicableEndpoint|An endpoint that is used to fulfill the criteria of or inform the adherence to the named constraint.|







