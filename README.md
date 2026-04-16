# OpenREL
The **OpenREL** registry and knowledge base, serving as a redirection target for the **OpenREL** namespace and an API source.

## OpenREL profile package

This package extends ODRL with OpenREL policy subclasses and structural grouping resources.

### Main files
- `openrel-profile.ttl` — profile metadata
- `openrel-classes.ttl` — OpenREL classes
- `openrel-relationships.ttl` — OpenREL properties and relationships
- `openrel-vocabularies.ttl` — SKOS concept schemes and concept collections
- `openrel-shapes.ttl` — SHACL node/property shapes
- `openrel-all.ttl` — concatenated convenience file

### Added examples
- `openrel-example-graph.ttl` — compact Turtle example graph
- `openrel-example-graph.jsonld` — same example graph in JSON-LD
- `jsonld-templates/` — starter JSON-LD templates for the principal ODRL and OpenREL classes

### Notes
- OpenREL is modeled here as an ODRL profile extension.
- `odrl:obligation` is used for Duties attached directly to a Policy.
- `odrl:duty` is used for Duties attached to a Permission.
- `openrel:assigner` and `openrel:assignee` are extension properties that allow Party Collections to play those roles where needed.
