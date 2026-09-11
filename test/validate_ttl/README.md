# OpenREL TTL File Validator

A command-line Python tool to validate .ttl (Turtle/RDF) files for the OpenREL ontology.

## Features

The validator performs the following checks on each .ttl file:

1. **Parse Validity**: Checks if the file can be parsed as valid Turtle/RDF syntax
2. **Unused Prefixes**: Identifies prefix declarations that are not used in the file
3. **Missing Comments**: Checks if each defined class and property has either:
   - `rdfs:comment` (RDF Schema comment)
   - `skos:definition` (SKOS definition - commonly used in OpenREL)

## Installation

Requires Python 3.6+ and the `rdflib` library:

```bash
pip install rdflib
```

## Usage

### Basic Usage

```bash
python validate_ttl.py
```

This will validate all .ttl files in the default directory `.openrel/vocabs/openrel`.

### Specify Directory

```bash
python validate_ttl.py -d /path/to/ttl/files
```

### Verbose Mode

Show detailed information about each issue:

```bash
python validate_ttl.py -v
```

### Strict Mode

Treat warnings as errors (exit with non-zero status if any warnings are found):

```bash
python validate_ttl.py -s
```

### Ignore Specific Prefixes

Ignore certain prefixes in the unused prefix check:

```bash
python validate_ttl.py --ignore-prefixes rdf rdfs owl
```

### Combine Options

```bash
python validate_ttl.py -d .openrel/vocabs/openrel -v -s --ignore-prefixes rdf rdfs
```

## Output

The tool produces a validation report with:

- Summary statistics (total files, valid files, files with warnings/errors)
- Detailed list of issues per file
- In verbose mode: full lists of unused prefixes and classes/properties without comments

### Exit Codes

- `0`: All files passed validation (no errors, and either no warnings or strict mode not enabled)
- `1`: Validation failed (files with errors, or warnings in strict mode)

## Examples

### Validate OpenREL vocabulary files

```bash
cd /path/to/openrel
python validate_ttl.py -d .openrel/vocabs/openrel -v
```

### Validate with strict checking

```bash
python validate_ttl.py -d .openrel/vocabs/openrel -s
```

### Validate and ignore common RDF prefixes

```bash
python validate_ttl.py -d .openrel/vocabs/openrel --ignore-prefixes rdf rdfs owl xsd
```

## Implementation Details

The validator:

1. Automatically handles the `openrel:` prefix which is often used but not defined in the files
2. Recognizes both `rdfs:comment` and `skos:definition` as valid documentation
3. Identifies classes and properties based on their RDF types:
   - Classes: `rdfs:Class`, `owl:Class`, `skos:Concept`, `skos:ConceptScheme`
   - Properties: `rdf:Property`, `owl:DatatypeProperty`, `owl:ObjectProperty`, `owl:AnnotationProperty`
4. Reports unused prefixes by checking if any URIs in the graph match the declared prefix URIs

## Notes

- The tool currently reports many parse errors in the OpenREL files because they contain syntax issues (missing periods, undefined prefixes like `dpv:`, `prov:`, `dcat-ap:`, etc.)
- These are actual issues in the TTL files that need to be fixed
- The unused prefix warnings can be suppressed using the `--ignore-prefixes` option if certain prefixes are intentionally declared for future use
