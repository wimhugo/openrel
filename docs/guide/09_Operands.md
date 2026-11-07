# Operands and Constraint Expressions

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

An ODRL constraint combines a left operand, operator and right operand.

| Element | Role |
|---|---|
| `odrl:leftOperand` | Identifies the measured or evaluated characteristic |
| `odrl:operator` | Specifies the comparison operation |
| `odrl:rightOperand` | Provides the comparison value when directly expressible |

A right operand may be a literal or resource as allowed by the expression. OpenREL additionally supports parameters for values that require binding or resolution. The Parameter is a distinct OpenREL class, not an ODRL RightOperand subclass.

When an expression cannot be evaluated because required values are missing, preserve that unresolved state; do not interpret it as a successful comparison.
