# Constraints and Named Constraints

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

An ODRL Constraint refines a Rule or other applicable expression. `openrel:NamedConstraint` is a specialised, IRI-identifiable constraint intended for reuse across policies.

Named Constraints are particularly useful where the same conditional expression occurs repeatedly, where constraints are combined logically, or where a registry is maintained. The operator is expressed using **`odrl:operator`**, not `odrl:operand`.

## Practical guidance

1. Reuse an existing NamedConstraint IRI if its semantics match the requirement.
2. Preserve its label, definition and associated classification vocabulary.
3. Check the applicable left operand, operator, right operand and any parameter binding.
4. Validate the expression against the relevant OpenREL shapes.
5. Do not assume that a NamedConstraint alone determines the outcome of a policy evaluation.

`openrel:typeConstraint` is the classification concept scheme. The current specification also describes purpose, access, usage, consent, subject rights, agent types, notification and other schemes. These are controlled values, not substitutes for the ODRL constraint expression.

See [Logical Constraints](07_LogicalConstraints.md), [Left Operands](08_LeftOperands.md) and [Parameters](10_RightOperands.md).
