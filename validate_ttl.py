#!/usr/bin/env python3
"""
OpenREL TTL File Validator

A command-line tool to validate .ttl (Turtle/RDF) files by:
1. Parsing files and checking RDF validity
2. Checking for unused prefixes
3. Checking if each defined class and property has an rdfs:comment

Usage:
    python validate_ttl.py [--directory DIR] [--verbose] [--strict]

Options:
    --directory DIR, -d DIR   Directory containing .ttl files (default: .openrel/vocabs/openrel)
    --verbose, -v             Show detailed output
    --strict, -s              Treat warnings as errors
    --help, -h                Show this help message
"""

import argparse
import os
import sys
import re
from pathlib import Path
from collections import defaultdict

try:
    from rdflib import Graph, URIRef
    from rdflib.namespace import RDF, RDFS, OWL, SKOS
    RDF_LIB_AVAILABLE = True
except ImportError:
    RDF_LIB_AVAILABLE = False


# RDF types we consider as "defined classes"
CLASS_TYPES = {
    str(RDFS.Class),
    str(OWL.Class),
    str(SKOS.Concept),
    str(SKOS.ConceptScheme),
}

# RDF types we consider as "defined properties"
PROPERTY_TYPES = {
    str(RDF.Property),
    str(OWL.DatatypeProperty),
    str(OWL.ObjectProperty),
    str(OWL.AnnotationProperty),
}


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Validate .ttl files for OpenREL ontology",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python validate_ttl.py
    python validate_ttl.py -d .openrel/vocabs/openrel
    python validate_ttl.py -d ./my_ttl_files --verbose --strict
        """
    )
    parser.add_argument(
        "-d", "--directory",
        default=".openrel/vocabs/openrel",
        help="Directory containing .ttl files (default: .openrel/vocabs/openrel)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show detailed output"
    )
    parser.add_argument(
        "-s", "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )
    parser.add_argument(
        "--ignore-prefixes",
        nargs="*",
        default=[],
        help="Prefixes to ignore in unused prefix check (space-separated)"
    )
    return parser.parse_args()


def find_ttl_files(directory):
    """Find all .ttl files in the specified directory."""
    path = Path(directory)
    if not path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        sys.exit(1)
    
    ttl_files = list(path.glob("*.ttl"))
    if not ttl_files:
        print(f"Warning: No .ttl files found in '{directory}'")
    
    return sorted(ttl_files)


def fix_openrel_prefix(content):
    """
    Fix the openrel: prefix issue in TTL files.
    Many files use openrel: but don't define it. It should map to the base URI.
    """
    # Check if openrel: is used but not defined
    if 'openrel:' not in content:
        return content
    
    if '@prefix openrel:' in content:
        return content
    
    # Find the base URI
    base_uri = None
    for line in content.split('\n'):
        line_stripped = line.strip()
        if line_stripped.startswith('@base'):
            # Extract the URI from @base <uri> .
            match = re.search(r'@base\s+<([^>]+)>', line_stripped)
            if match:
                base_uri = match.group(1)
                break
        elif line_stripped.startswith('@prefix :'):
            # Extract from @prefix : <uri> .
            match = re.search(r'@prefix\s+:\s+<([^>]+)>', line_stripped)
            if match:
                base_uri = match.group(1)
                break
    
    if not base_uri:
        return content
    
    # Find where to insert the prefix
    lines = content.split('\n')
    insert_pos = 0
    for i, line in enumerate(lines):
        if line.strip().startswith('@base') or line.strip().startswith('@prefix'):
            insert_pos = i + 1
    
    # Insert the openrel prefix
    lines.insert(insert_pos, f"@prefix openrel: <{base_uri}> .")
    return '\n'.join(lines)


def parse_ttl_file(filepath):
    """Parse a TTL file and return the RDF graph."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fix common issues
        content = fix_openrel_prefix(content)
        
        graph = Graph()
        graph.parse(data=content, format="turtle")
        return graph, None
    except Exception as e:
        return None, str(e)


def extract_prefixes_from_text(filepath):
    """Extract all @prefix declarations from a TTL file."""
    prefixes = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('@prefix'):
                    # Parse @prefix directive
                    # Format: @prefix name: <uri> .
                    match = re.match(r'@prefix\s+(\S+)\s+<([^>]+)>', line)
                    if match:
                        prefix_name = match.group(1).rstrip(':')
                        prefix_uri = match.group(2)
                        prefixes[prefix_name] = prefix_uri
    except Exception as e:
        pass
    return prefixes


def get_used_prefixes(graph, declared_prefixes):
    """
    Find which declared prefixes are actually used in the graph.
    Returns a set of prefix names that are used.
    """
    used = set()
    
    # Get all URIs used in the graph
    all_uris = set()
    for triple in graph:
        for term in triple:
            if hasattr(term, '__str__'):
                uri_str = str(term)
                if uri_str.startswith('http'):
                    all_uris.add(uri_str)
    
    # Check which declared prefixes match any used URI
    for prefix_name, prefix_uri in declared_prefixes.items():
        # Normalize the prefix URI
        if not prefix_uri.endswith('/') and not prefix_uri.endswith('#'):
            prefix_uri_with_slash = prefix_uri + '/'
            prefix_uri_with_hash = prefix_uri + '#'
        else:
            prefix_uri_with_slash = prefix_uri
            prefix_uri_with_hash = prefix_uri
        
        for uri in all_uris:
            if (uri.startswith(prefix_uri) or 
                uri.startswith(prefix_uri_with_hash) or 
                uri.startswith(prefix_uri_with_slash)):
                used.add(prefix_name)
                break
    
    return used


def get_defined_classes_and_properties(graph):
    """
    Extract all defined classes and properties from the graph.
    Returns two dictionaries:
    - classes: {uri: label}
    - properties: {uri: label}
    """
    classes = {}
    properties = {}
    
    # Helper to get label
    def get_label(subject):
        for label_obj in graph.objects(subject, RDFS.label):
            return str(label_obj)
        for label_obj in graph.objects(subject, SKOS.prefLabel):
            return str(label_obj)
        return None
    
    # Find all subjects that have rdf:type statements
    for subject in graph.subjects(RDF.type, None):
        types = list(graph.objects(subject, RDF.type))
        for obj in types:
            obj_str = str(obj)
            
            # Check if it's a class
            if obj_str in CLASS_TYPES:
                label = get_label(subject)
                classes[str(subject)] = label or str(subject)
                break
            
            # Check if it's a property
            if obj_str in PROPERTY_TYPES:
                label = get_label(subject)
                properties[str(subject)] = label or str(subject)
                break
    
    # Also check for skos:Concept which are often used as classes
    for subject in graph.subjects(RDF.type, SKOS.Concept):
        if str(subject) not in classes:
            label = get_label(subject)
            classes[str(subject)] = label or str(subject)
    
    for subject in graph.subjects(RDF.type, SKOS.ConceptScheme):
        if str(subject) not in classes:
            label = get_label(subject)
            classes[str(subject)] = label or str(subject)
    
    # Check for owl:Class
    for subject in graph.subjects(RDF.type, OWL.Class):
        if str(subject) not in classes:
            label = get_label(subject)
            classes[str(subject)] = label or str(subject)
    
    # Check for rdf:Property
    for subject in graph.subjects(RDF.type, RDF.Property):
        if str(subject) not in properties:
            label = get_label(subject)
            properties[str(subject)] = label or str(subject)
    
    return classes, properties


def check_rdfs_comments(graph, classes, properties):
    """
    Check if each defined class and property has an rdfs:comment or skos:definition.
    Returns a dictionary with missing comments.
    """
    missing_comments = {
        'classes': [],
        'properties': []
    }
    
    # Check classes
    for uri, label in classes.items():
        has_comment = False
        for comment in graph.objects(URIRef(uri), RDFS.comment):
            has_comment = True
            break
        # Also check skos:definition as it's commonly used
        if not has_comment:
            for comment in graph.objects(URIRef(uri), SKOS.definition):
                has_comment = True
                break
        
        if not has_comment:
            missing_comments['classes'].append({
                'uri': uri,
                'label': label
            })
    
    # Check properties
    for uri, label in properties.items():
        has_comment = False
        for comment in graph.objects(URIRef(uri), RDFS.comment):
            has_comment = True
            break
        # Also check skos:definition as it's commonly used
        if not has_comment:
            for comment in graph.objects(URIRef(uri), SKOS.definition):
                has_comment = True
                break
        
        if not has_comment:
            missing_comments['properties'].append({
                'uri': uri,
                'label': label
            })
    
    return missing_comments


def validate_file(filepath, ignore_prefixes=None):
    """
    Validate a single TTL file.
    Returns a dictionary with validation results.
    """
    if ignore_prefixes is None:
        ignore_prefixes = []
    
    results = {
        'file': str(filepath),
        'valid': True,
        'errors': [],
        'warnings': [],
        'prefixes_declared': [],
        'prefixes_unused': [],
        'classes_without_comment': [],
        'properties_without_comment': [],
    }
    
    # Step 1: Parse and check validity
    graph, parse_error = parse_ttl_file(filepath)
    if parse_error:
        results['valid'] = False
        results['errors'].append(f"Parse error: {parse_error}")
        return results
    
    # Step 2: Check for unused prefixes
    declared_prefixes = extract_prefixes_from_text(filepath)
    results['prefixes_declared'] = sorted(declared_prefixes.keys())
    
    used_prefixes = get_used_prefixes(graph, declared_prefixes)
    unused_prefixes = [p for p in declared_prefixes.keys() 
                      if p not in used_prefixes and p not in ignore_prefixes and p != '']
    results['prefixes_unused'] = sorted(unused_prefixes)
    
    if unused_prefixes:
        results['warnings'].append(
            f"Unused prefixes: {', '.join(unused_prefixes)}"
        )
    
    # Step 3: Check for rdfs:comment on classes and properties
    classes, properties = get_defined_classes_and_properties(graph)
    missing_comments = check_rdfs_comments(graph, classes, properties)
    
    results['classes_without_comment'] = missing_comments['classes']
    results['properties_without_comment'] = missing_comments['properties']
    
    if missing_comments['classes']:
        class_labels = [c['label'] for c in missing_comments['classes']]
        results['warnings'].append(
            f"Classes without rdfs:comment or skos:definition: {', '.join(sorted(class_labels))}"
        )
    
    if missing_comments['properties']:
        prop_labels = [p['label'] for p in missing_comments['properties']]
        results['warnings'].append(
            f"Properties without rdfs:comment or skos:definition: {', '.join(sorted(prop_labels))}"
        )
    
    return results


def print_results(results, verbose=False, strict=False):
    """Print validation results."""
    total_files = len(results)
    valid_files = sum(1 for r in results if r['valid'])
    files_with_warnings = sum(1 for r in results if r['warnings'])
    files_with_errors = sum(1 for r in results if r['errors'])
    
    print("=" * 80)
    print("OpenREL TTL Validation Report")
    print("=" * 80)
    print(f"Files scanned: {total_files}")
    print(f"Valid files: {valid_files}")
    print(f"Files with warnings: {files_with_warnings}")
    print(f"Files with errors: {files_with_errors}")
    print("=" * 80)
    
    for result in results:
        print(f"\nFile: {result['file']}")
        
        if result['errors']:
            print("  ERRORS:")
            for error in result['errors']:
                print(f"    - {error}")
        
        if result['warnings']:
            print("  WARNINGS:")
            for warning in result['warnings']:
                print(f"    - {warning}")
        
        if verbose:
            if result['prefixes_unused']:
                print(f"  Unused prefixes: {', '.join(result['prefixes_unused'])}")
            
            if result['classes_without_comment']:
                print(f"  Classes without comment:")
                for cls in result['classes_without_comment']:
                    print(f"    - {cls['label']} ({cls['uri']})")
            
            if result['properties_without_comment']:
                print(f"  Properties without comment:")
                for prop in result['properties_without_comment']:
                    print(f"    - {prop['label']} ({prop['uri']})")
        
        if not result['errors'] and not result['warnings']:
            print("  OK")
    
    print("\n" + "=" * 80)
    
    # Summary statistics
    total_unused_prefixes = sum(len(r['prefixes_unused']) for r in results)
    total_classes_missing = sum(len(r['classes_without_comment']) for r in results)
    total_props_missing = sum(len(r['properties_without_comment']) for r in results)
    
    print(f"Total unused prefixes across all files: {total_unused_prefixes}")
    print(f"Total classes without comments: {total_classes_missing}")
    print(f"Total properties without comments: {total_props_missing}")
    print("=" * 80)
    
    # Return exit code
    if files_with_errors > 0:
        return 1
    if strict and files_with_warnings > 0:
        return 1
    return 0


def main():
    """Main entry point."""
    args = parse_arguments()
    
    if not RDF_LIB_AVAILABLE:
        print("Error: rdflib is required. Please install it with: pip install rdflib")
        sys.exit(1)
    
    # Find TTL files
    ttl_files = find_ttl_files(args.directory)
    
    if not ttl_files:
        print(f"No .ttl files found in '{args.directory}'")
        sys.exit(0)
    
    print(f"Found {len(ttl_files)} .ttl files in '{args.directory}'")
    print()
    
    # Validate each file
    results = []
    for filepath in ttl_files:
        try:
            result = validate_file(filepath, ignore_prefixes=args.ignore_prefixes)
            results.append(result)
        except Exception as e:
            results.append({
                'file': str(filepath),
                'valid': False,
                'errors': [f"Unexpected error: {str(e)}"],
                'warnings': []
            })
    
    # Print results
    exit_code = print_results(results, verbose=args.verbose, strict=args.strict)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
