# Contextual Assertions and Request Policies

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL separates reusable contextual claims from the request in which they are used.

| Class | Role |
|---|---|
| `openrel:AssertionPolicy` | Reusable assertion policy; a subclass of `odrl:Assertion` |
| `openrel:RequestPolicy` | Request incorporating assertion policies and request-specific context; subclass of `odrl:Request` |
| `openrel:AssertionCollection` | Collection of contextual claims |
| `openrel:ContextAssertion` | Claim associating a Parameter with a value or resolution source |
| `openrel:ResolvedAssertion` | Separate output claim produced by resolution |

## Key relationships

`openrel:hasAssertionPolicy` links a RequestPolicy to a reusable AssertionPolicy. `openrel:hasAssertionCollection` associates either policy type with an AssertionCollection, and `openrel:hasAssertion` links the collection to individual ContextAssertions.

A ContextAssertion identifies its Parameter with `openrel:assertedParameter`. A direct value uses `openrel:assertedValue`; a claim requiring resolution may use `openrel:bindingSource` to identify a `openrel:ParameterResolutionService`.

**Do not overwrite the original claim with the resolved result.** A `openrel:ResolvedAssertion` uses `openrel:resolvesAssertion` to refer to its source claim, preserving provenance and history. See specification Annex C.
