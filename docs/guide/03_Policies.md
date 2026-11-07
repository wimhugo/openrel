# Policies and Policy Collections

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

ODRL policies contain permissions, prohibitions and duties. OpenREL adds policy specialisations according to their purpose, not as replacements for the ODRL policy lifecycle types (`odrl:Request`, `odrl:Offer`, `odrl:Agreement`, etc.).

| Class | Intended use |
|---|---|
| `openrel:Licence` | Rights and obligations associated with a licence |
| `openrel:AccessRules` | Access conditions imposed by rights holders, subjects, repositories or institutions |
| `openrel:ProcessRules` | Operational requirements imposed by software platforms or dissemination workflows |
| `openrel:PolicyCollection` | A referenceable grouping of two or more policies for combined evaluation or recordkeeping |

## Policy collection

Use `openrel:hasPolicy` to identify constituent `odrl:Policy` instances. The collection has **at least two** policies, enforced by the OpenREL SHACL model. It is not simply another way to express `odrl:inheritFrom`, and grouping does not mean that all permissions are automatically combined or inherited.

```turtle
@prefix openrel: <http://www.w3id.org/ns/openrel/0/> .
@prefix odrl: <http://www.w3.org/ns/odrl/2/> .
@prefix ex: <https://example.org/> .

ex:applicablePolicies a openrel:PolicyCollection ;
    openrel:hasPolicy ex:datasetLicence, ex:repositoryAccessRules .

ex:datasetLicence a openrel:Licence .
ex:repositoryAccessRules a openrel:AccessRules .
```

This example demonstrates composition, not a successful evaluation. An evaluator must still consider the applicable rules and context.

## Requests and assertions

`openrel:RequestPolicy` extends `odrl:Request` with request-specific contextual assertions and references to reusable `openrel:AssertionPolicy` instances. Contextual claims are not themselves proof of compliance. See [Contextual Assertions](16_ContextualAssertions.md) and [Parameter Resolution](17_ParameterResolution.md).
