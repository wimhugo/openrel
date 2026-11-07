# Parameter Resolution and Validation

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

Parameter resolution obtains or validates values required for evaluation. A resolution service may return multiple outputs, including partial results.

`openrel:ParameterResolutionService` declares supported inputs and outputs through `openrel:inputParameter` and `openrel:outputParameter`. A contextual assertion may identify the service via `openrel:bindingSource`.

Each invocation can be recorded as an `openrel:ResolutionResult`, which identifies the invoked service through `openrel:resolutionService` and links resulting `openrel:ResolvedAssertion` instances through `openrel:hasResolvedAssertion`. A resolved assertion references its original claim with `openrel:resolvesAssertion`.

## Processing checklist

1. Verify that the service is authorised for the requested parameter and context.
2. Record the source claim and expected Parameter.
3. Invoke the service and capture its result separately.
4. Check datatype/class, multiplicity, provenance and other constraints.
5. Record partial or failed resolution explicitly; do not substitute a guessed value.
6. Pass validated results to policy evaluation, retaining the audit trail.

The specification recommends PROV-O for additional provenance. See Annex C for worked Turtle examples and SHACL requirements.
