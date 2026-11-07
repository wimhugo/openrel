# Why OpenREL? Rationale and Context

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL extends the W3C ODRL Information Model for the expression and evaluation of rights, access conditions, process requirements, and obligations relevant to research assets. A dataset can be subject to several independent sources of requirements: its licence, conditions imposed by a repository or rights holder, and technical process rules applied by a platform.

ODRL provides the policy/rule/action/constraint foundation. OpenREL adds specialised policy classes, reusable named constraints, parameterised expressions, contextual assertions, and auditable evaluation records. Existing vocabularies such as DPV, CC, DUO and Data Spaces vocabularies remain relevant as external semantic sources. OpenREL should reuse their identifiers and meanings where appropriate rather than asserting that they are interchangeable.

## Typical workflow

1. Identify the Asset and relevant policies.
2. Assemble the applicable policies in an `openrel:PolicyCollection`.
3. Express the requested operation and contextual claims in an `openrel:RequestPolicy`, optionally referencing reusable `openrel:AssertionPolicy` resources.
4. Resolve any parameters and validate evidence.
5. Evaluate the combined policies, recording the decision, rationale and provenance.

**Important:** A semantic mapping between two actions is evidence for evaluation, not a policy-level authorisation.
