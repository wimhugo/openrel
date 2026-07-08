# Named Constraints

ODRL makes provision for the description of a constraint, and such a constraint can have a UID, which by implication allows such constraints to become nodes in a graph that can be referenced by Actions.

This approach is useful, because some instances of constraints (for example, that any number of use-related subclasses are acceptable for non-commerical purposes) occur in many policies and licences, and one would like to avoid duplication and ensure consistent encoding of such constraints. From this perspective, one should avoid the option that allows repetitive local definition of a constraint whereever it is required.

The approach has its downsides, in that a policy or licence is not composed in a single location, but finds its rule content spread in a graph. If all policies and licences are contained in the same graph, this is OK, but if it is spread over many graphs, it becomes cumvbersome to complile the machine-readable version of a policy - even though it is technically possible.

We will follow a hybrid approach in OpenREL, by defining a set of 'Named Constraints' - constraints that can be referenced via IRI and extend the properties of the ODRL COnstraint class. These named constraints assist with consistent implementation of constraints that are commonly used and/ or are complex to encode.

