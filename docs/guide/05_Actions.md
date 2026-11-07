# Actions and Semantic Mappings

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

ODRL Actions describe what is to be performed on an Asset. OpenREL supplies additional Action individuals and semantic mappings to external vocabularies where necessary.

Prefer a general Action refined by constraints where the variation is a condition rather than a genuinely different operation. For example, notification requirements can often be expressed through a notification Action together with constraints describing the kind of notification and its target.

## Comparison and interpretation

A mapping or assertion about two Actions can help determine whether they overlap, contradict one another, or have a more specific relationship. Such relationships must be interpreted in the context of the rule roles (`odrl:Permission`, `odrl:Prohibition`, `odrl:Duty`), the relevant Asset, and constraints.

Use `openrel:EvaluationMapping` for recorded pairwise evidence. The assertion type and provenance should be preserved; inferred semantic similarity is not equivalent to an asserted permission.

Do not use deprecated `openrel:contradictsAction` in new examples. See [Evaluation](13_Evaluation.md).
