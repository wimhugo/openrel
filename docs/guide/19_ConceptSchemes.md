# Concept Schemes and Registries

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL uses SKOS concept schemes for controlled values, including policy status, access, validity, constraint categories, assertion derivation, evaluation outcomes, parameter binding sources and subject rights.

A **concept scheme** is a controlled classification; a **registry** is a collection of referenceable individuals (for example, named constraints, parameters or Actions). These may overlap in their RDF representation but have different intended uses.

Use the exact IRI from the specification or published Turtle file. Do not derive an IRI from a display label. For example, `openrel:typeStatus`, `openrel:typeEvaluationOutcome`, `openrel:PolicyScheme`, `openrel:EvaluationScheme` and `openrel:constraintScheme` have distinct purposes and should not be conflated.

Where external concepts are mapped, record whether the mapping is exact, broader/narrower, or merely related. Such mappings are not automatically executable policy decisions.
