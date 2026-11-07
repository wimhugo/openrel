# Logical Constraints

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

ODRL supports logical combinations of constraints. Use the operators and expression forms defined by ODRL and the applicable OpenREL profile, rather than inventing a parallel Boolean syntax.

A logical constraint may reference reusable `openrel:NamedConstraint` individuals. When evaluating the result, preserve the structure of the logical expression: a conjunction cannot be reduced to one successful child expression, and an unresolved parameter must not silently be treated as satisfied.

For an implementation, record which subexpression succeeded, failed, or remained unresolved. Consult the specification for exact supported operators and the SHACL constraints for the selected profile.
