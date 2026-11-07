# Parameter Binding and Binding Sources

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

Parameter binding identifies the source or context from which a parameter value is expected. The **binding source vocabulary** classifies this context; it is not itself a service invocation.

The OpenREL specification describes the `openrel:ParameterBindingSource` concept scheme. Typical source categories include policy-supplied values, requestor or party context, subject context, repository/platform context, runtime context, events and external references. Consult the current scheme for the authoritative IRIs.

Distinguish:

- A Parameter and its expected value constraints.
- The parameter's binding-source classification (the kind of source expected).
- A `openrel:ContextAssertion` stating or referring to a value.
- A `openrel:ParameterResolutionService` used to obtain or validate the value.
- A `openrel:ResolutionResult` documenting the actual resolution invocation.

Do not treat an unverified context claim as an authenticated fact. See specification A.7.4 and Annex C.
