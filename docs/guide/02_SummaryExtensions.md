# Summary of Main Extensions and Additions

OpenREL is intended as an extension for existing vocabularies that address aspects of rights management already, primarily ODRL and ccREL, but there are several others that are in scope and have been incorporated or linked where applicable.

## Extension Types

These extensions fall into the following categories:

- **Subclasses of Existing Classes**: These are typically used when an existing class, for example the 'Policy' class defined by ODRL, requires further definition (a subclass with a narrower definition) and/ or specific property additions that apply only to the subclass. A good example of this is the Policy Class, to which OpenREL ads the explicit subclass 'Licence' to account for a policy that has a legal text and applies in a given jurisdiction.
- **New Concept Schemes**: These are typically vocabularies that are specific to the research output and repository management landscape, and may not apply more generally to generic content for which a policy or licence can be formulated. These Concept Schemes are used extensively to qualify, for example, Right Operands in Constraint encodings. This approach allows simpler extension of scope, since it often avoids definition of new subclasses when a new constraint is identified. As an example, notifications are modelled in OpenREL as a generic Left Operand (requiring notification), with the Right Operand(s) defining the type of notification and the notification targets - this model is more extensible than having specific Left Operand classes for each type of notification.
- **Mappings**: In some cases, OpenREL concepts or classes mirror those defined elsewhere, but there are multiple vocabularies that use semantically matching or similar concepts and classes. To enable interoperability between encodings, and the ability to assess and process encodings that are not using OpenREL, these mappings are required. It is also required to re-enable the DALICC encpodings of popular licences, which relied extensively on a DALICC vocabulary that is no longer supported. OpenREL provides mappings and crosswalks for these licences.
- **Properties**: A number of new properties have been defined that were not part of the existing vocabularies available to the community.

## Scope of Vocabulary

The vocabularies that are referenced and reused in OpenREL are summarised in the tables below.

### RDF-Related

These vocabularies are foundational to RDF encodings and are used whenever appropriate.

|Label|Prefix|Source|
|:--------|:--------|:--------|
|RDF| rdf: |<http://www.w3.org/1999/02/22-rdf-syntax-ns#> |
|SKOS| skos: |<http://www.w3.org/2004/02/skos/core#> |
|OWL| owl: |<http://www.w3.org/2002/07/owl#> |
|XSD| xsd: |<http://www.w3.org/2001/XMLSchema#> |

### General Content

These vocabularies are used to describe very general classes and concepts.

|Label|Prefix|Source|
|:--------|:--------|:--------|
|SCHEMA |schema: |<http://schema.org/> |
|FOAF |foaf: |<http://xmlns.com/foaf/0.1/> |
|VCARD |vcard: |<http://www.w3.org/2006/vcard/ns#> |











