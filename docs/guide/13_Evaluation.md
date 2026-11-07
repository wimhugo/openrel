# Policy Comparison and Evaluation

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL separates **pairwise semantic evidence** from **policy-level decisions**.

| Component | Role |
|---|---|
| `openrel:EvaluationMapping` | Records a comparison between identified resources (such as Actions or Constraints), including its outcome and provenance |
| `openrel:EvaluationDetail` | Records evaluation information associated with policy-level comparison |
| `openrel:EvaluationScheme` | Describes an evaluation scheme used to organise or interpret evaluation |
| `openrel:PolicyCollection` | Identifies the two or more policies under consideration |

## Policy-level outcomes

- **PERMIT:** applicable prohibitions have been accounted for and required preconditions, including pre-duties, are satisfied.
- **CONDITIONAL:** no applicable prohibition prevents the operation, but some required preconditions or pre-duties remain to be satisfied.
- **DENY:** an applicable prohibition prevents the operation or a mandatory condition cannot be satisfied.

These are policy-level outcomes; do not confuse them with pairwise resource relationships such as `allows`, `contradicts` or `overlaps`. The concept scheme is `openrel:typeEvaluationOutcome`.

## Evidence and provenance

Evaluation records should identify both compared resources, their evaluation class, outcome, assertion derivation type, rationale and provenance where available. Distinguish assertions made by a human, semantic assertions and corpus-derived observations. Use current terms `openrel:assertionHuman` and `openrel:assertionSemantic`; do not use `humanAssertion`, `semanticAssertion`, or deprecated `openrel:contradictsAction`.

A mapping between Actions cannot alone establish permission to access an Asset. The evaluator must also consider applicable rule roles, constraints, parameters and duties. See specification A.4 and Annex B.
