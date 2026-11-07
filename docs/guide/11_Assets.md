# Assets and Asset Collections

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

ODRL `odrl:Asset` identifies the resource to which a Rule applies. Asset collections and relationships must be represented using the applicable ODRL mechanisms and the published profile, not by inventing an OpenREL AssetCollection class.

Distinguish a collection of Assets from `openrel:PolicyCollection`: the latter groups **policies**, not data resources. A policy collection may be relevant to an Asset or Asset Collection, but this does not imply that every policy has identical scope.

When evaluating a request, determine the actual target Asset and any relevant collection membership before selecting the applicable policies.
