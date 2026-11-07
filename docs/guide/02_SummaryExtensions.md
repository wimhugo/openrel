# Summary of Main Extensions and Additions

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL is an ODRL-aligned vocabulary and evaluation framework. Its principal additions are grouped below.

| Area | Key terms | Purpose |
|---|---|---|
| Policies | `openrel:Licence`, `openrel:AccessRules`, `openrel:ProcessRules`, `openrel:PolicyCollection` | Distinguish types of applicable policy and group multiple policies |
| Duties | `openrel:PreDuty`, `openrel:PostDuty` | Distinguish duties required before and after an action |
| Constraints | `openrel:NamedConstraint` | Give reusable constraints stable identifiers |
| Evaluation | `openrel:EvaluationScheme`, `openrel:EvaluationDetail`, `openrel:EvaluationMapping` | Record comparison evidence and policy-level outcomes |
| Parameters | `openrel:Parameter`, `openrel:ParameterResolutionService` | Describe values and their resolution requirements |
| Context | `openrel:AssertionPolicy`, `openrel:RequestPolicy`, `openrel:AssertionCollection`, `openrel:ContextAssertion`, `openrel:ResolvedAssertion`, `openrel:ResolutionResult` | Represent and resolve contextual claims |
| Controlled vocabularies | SKOS concept schemes for access, status, validity, assertions, outcomes, constraints, binding sources and other types | Supply controlled values and interoperable references |

The OpenREL namespace is `http://www.w3id.org/ns/openrel/0/`. New metadata properties and classes must not be mistaken for native ODRL properties or automatically assumed to be permitted ODRL Profile extensions.

OpenREL distinguishes a **resource-level mapping** (for example, relationships between Actions) from a **policy-level decision**. A decision requires applicable prohibitions, permissions, duties, constraints, and parameter resolution to be considered together.
