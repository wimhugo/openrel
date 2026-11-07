# Parameters and Right Operands

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL supports dynamic values without encoding a placeholder string such as `[END_DATE]` as though it were a real `xsd:dateTime`.

`openrel:Parameter` describes an expected value, including its permitted RDF datatype or class and multiplicity. A Parameter is **not** a subclass of an ODRL Right Operand. `openrel:ParameterResolutionService` represents a service able to resolve or validate parameter values.

The specification describes `openrel:operandParameter` as the link between a Left Operand and its Parameter definition. The binding context is classified through the parameter binding source vocabulary.

## Typical process

1. Identify the Left Operand and required comparison.
2. Define or reuse a Parameter with its value requirements.
3. Identify where the value should come from.
4. Supply a direct assertion or invoke an authorised resolution service.
5. Validate the resulting value before using it in policy evaluation.

See [Parameter Binding](14_ParameterBinding.md), [Contextual Assertions](16_ContextualAssertions.md) and [Parameter Resolution](17_ParameterResolution.md).
