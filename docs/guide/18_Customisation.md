# Customising OpenREL

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

OpenREL is designed to be extended through controlled vocabularies, registries and ODRL-compatible profile extensions. Prefer reuse of existing ODRL Actions and constraints combined with context-specific SKOS concepts over creating a new Action for every minor variation.

## Recommended approach

1. Reuse the OpenREL namespace and published identifiers without redefining their meaning.
2. Extend a concept scheme for local classifications, with clear definitions and provenance.
3. Add local NamedConstraint or Parameter individuals when a reusable expression is needed.
4. Add new classes/properties only where a genuine structural gap exists, and check ODRL Profile conformance.
5. Define SHACL constraints and validate examples before publication.
6. Keep external vocabulary mappings separate from policy evaluation outcomes.

New OpenREL terms follow the specification's RDF/SKOS documentation pattern, including labels, definitions, notes and appropriate domain/range declarations. Deprecations should be reflected in both ontology and documentation; do not introduce `openrel:dutySlot` or `openrel:contradictsAction` in new encodings.
