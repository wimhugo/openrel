# Named Constraints

ODRL makes provision for the description of a *Constraint*, and such a Constraint can have a UID, which by implication allows them to become nodes in a graph that can be referenced by *Actions*.

This approach is useful, because some instances of Constraints (for example, that any number of Use-related subclasses are acceptable for non-commerical purposes) occur in many policies and licences, and one would like to avoid duplication and ensure consistent encoding of these Constraints. From this perspective, one should avoid the option that allows repetitive local definition of a Constraint wherever it is required.

The approach has its downsides, in that a policy or licence is not composed in a single location, but finds its rule content spread in a graph. If all policies and licences are contained in the same graph, this is OK, but if it is spread over many graphs, it becomes cumbersome to complile the machine-readable version of a policy or licence - even though it is technically possible.

We will follow a hybrid approach in OpenREL, by defining a set of '**Named Constraints**' - Constraints that can be referenced via IRI and extend the properties of the ODRL Constraint class. These Named Constraints assist with consistent implementation of encodings that are commonly used and/ or are complex to create.

