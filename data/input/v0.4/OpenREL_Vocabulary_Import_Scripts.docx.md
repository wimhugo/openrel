

| EOSC Beyond · WP14 · T14.4 · OpenAIRE / DANS OpenREL — Vocabulary Imports Suggested Python scripts for GeoNames, SPDX, and W3C DPV  |
| :---- |

## **Purpose and scope**

This document provides suggested Python scripts for downloading and converting three external vocabularies into the JSON lookup files required by the OpenREL Knowledge Base and Licence Wizard. These scripts are provided as a practical starting point rather than mandatory artefacts. If your existing pipeline or preferred tooling handles the same task differently, please use whatever works best for you.

| ℹ  All three scripts are optional helpers. The important output is the resulting JSON file in each case. The scripts can be modified, replaced, or run incrementally as needed. |
| :---- |

The three vocabularies covered are:

* GeoNames — country and geographic identifiers for the Spatial constraint (C13)

* SPDX — licence registry for the Adapt existing licence wizard mode

* W3C DPV v2.0 — Purpose and LegalBasis IRIs for constraints C01, C02, and C03

Each section below includes the source URL, the suggested script, the expected output structure, and notes on what to watch for.

| 1 | GeoNames — country identifiers |
| :---: | :---- |

| Purpose | Provides GeoNames URIs for the C13 Spatial constraint. The wizard country picker shows country names; the stored value is the GeoNames IRI. |
| :---- | :---- |
| **Source URL** | https://download.geonames.org/export/dump/countryInfo.txt |
| **Format** | Tab-separated text, approx. 250 rows, one per country. |
| **Output file** | openrel/lookup/country\_list.json |
| **Update frequency** | Rarely. GeoNames country IDs are stable. Re-run only if a new country entry or ID change is needed. |

| ✓  This script can be run without any API key or authentication. The file is publicly available. |
| :---- |

**Suggested script**

| import csv, json, urllib.request EU\_MEMBERS \= {     'AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE',     'GR','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT',     'RO','SK','SI','ES','SE' } url \= 'https://download.geonames.org/export/dump/countryInfo.txt' rows \= \[\] with urllib.request.urlopen(url) as r:     for line in r.read().decode('utf-8').splitlines():         if line.startswith('\#') or not line.strip():             continue         parts \= line.strip().split('\\t')         if len(parts) \< 17:             continue         iso2       \= parts\[0\].strip()         name       \= parts\[4\].strip()         geoname\_id \= parts\[16\].strip()         if not geoname\_id.isdigit():             continue         rows.append({             'label':        name,             'geonames\_uri': f'https://sws.geonames.org/{geoname\_id}/',             'iso2':         iso2,             'eu\_member':    iso2 in EU\_MEMBERS         }) \# Add EU aggregate entry rows.append({     'label':        'European Union',     'geonames\_uri': 'https://sws.geonames.org/6255148/',     'iso2':         'EU',     'eu\_member':    None }) rows.sort(key=lambda x: x\['label'\]) with open('country\_list.json', 'w', encoding='utf-8') as f:     json.dump(rows, f, ensure\_ascii=False, indent=2) print(f'{len(rows)} entries written to country\_list.json') |
| :---- |

**Expected output (sample entries)**

| \[   {     "label":        "Greece",     "geonames\_uri": "https://sws.geonames.org/390903/",     "iso2":         "GR",     "eu\_member":    true   },   {     "label":        "European Union",     "geonames\_uri": "https://sws.geonames.org/6255148/",     "iso2":         "EU",     "eu\_member":    null   } \] |
| :---- |

| ⚠  The EU aggregate entry (ID 6255148\) covers Europe as a continent in GeoNames, not strictly the EU political boundary. If a stricter EU-only URI is required in future, it should be declared explicitly in the OpenREL namespace. |
| :---- |

| 2 | SPDX — licence registry |
| :---: | :---- |

| Purpose | Provides the list of known licences for the Adapt existing licence wizard mode. The steward picks a licence by name; the wizard loads its pre-mapped OpenREL rules. |
| :---- | :---- |
| **Source URL** | https://raw.githubusercontent.com/spdx/license-list-data/main/json/licenses.json |
| **Format** | JSON. Approx. 700 licence entries. No conversion needed, only filtering. |
| **Output files** | openrel/lookup/spdx\_licences.json openrel/lookup/spdx\_openrel\_mapping.json |
| **Update frequency** | The SPDX list is updated approximately twice a year. The mapping file is updated manually when new licences are added to the OpenREL scope. |

|  |
| :---- |

**Suggested filtering script**

| import json, urllib.request url \= ('https://raw.githubusercontent.com/spdx/'        'license-list-data/main/json/licenses.json') with urllib.request.urlopen(url) as r:     data \= json.load(r) kept \= \[\] for lic in data\['licenses'\]:     if lic.get('isDeprecatedLicenseId', False):         continue     if not lic.get('reference'):         continue     kept.append({         'spdx\_id':      lic\['licenseId'\],         'name':         lic\['name'\],         'url':          lic\['reference'\],         'osi\_approved': lic.get('isOsiApproved', False),         'deprecated':   False     }) kept.sort(key=lambda x: x\['spdx\_id'\]) with open('spdx\_licences.json', 'w', encoding='utf-8') as f:     json.dump(kept, f, ensure\_ascii=False, indent=2) print(f'{len(kept)} licences written to spdx\_licences.json') |
| :---- |

**Expected output (sample entries)**

| \[   {     "spdx\_id":      "CC-BY-4.0",     "name":         "Creative Commons Attribution 4.0 International",     "url":          "https://spdx.org/licenses/CC-BY-4.0.html",     "osi\_approved": false,     "deprecated":   false   },   {     "spdx\_id":      "CC0-1.0",     "name":         "Creative Commons Zero v1.0 Universal",     "url":          "https://spdx.org/licenses/CC0-1.0.html",     "osi\_approved": true,     "deprecated":   false   } \] |
| :---- |

**Mapping file structure (provided separately by Melios)**

The spdx\_openrel\_mapping.json file maps each SPDX licence to its default OpenREL rules. This file is authored by the OpenREL team and committed to the KB without modification. Sample structure:

| \[   {     "spdx\_id":                    "CC-BY-4.0",     "openrel\_default\_permissions":  \["A01","A02","A03","A04","A05"\],     "openrel\_default\_prohibitions": \[\],     "openrel\_default\_obligations":  \["A10"\],     "openrel\_default\_constraints":  { "A10": \["C23"\] }   },   {     "spdx\_id":                    "CC0-1.0",     "openrel\_default\_permissions":  \["A01","A02","A03","A04","A05"\],     "openrel\_default\_prohibitions": \[\],     "openrel\_default\_obligations":  \[\],     "openrel\_default\_constraints":  {}   }   // ... initial delivery covers 12 priority licences \] |
| :---- |

| 3 | W3C DPV — Data Privacy Vocabulary |
| :---: | :---- |

| Purpose | Provides the IRIs for Purpose and LegalBasis terms used in OpenREL constraints C01 (Academic Research), C02 (Non-Commercial), and C03 (Consent). These IRIs appear in the ODRL JSON-LD output and must be correct and resolvable. |
| :---- | :---- |
| **Source URL** | https://w3id.org/dpv/dpv.jsonld  (JSON-LD) or https://w3id.org/dpv/dpv.ttl  (Turtle) |
| **Version** | DPV v2.0. The version must be pinned in the KB. DPV is under active development and IRIs can change between major versions. |
| **Output file** | openrel/lookup/dpv\_terms.json |
| **Update frequency** | Only when OpenREL adds new constraints referencing DPV terms, or when DPV releases a breaking change. |

| ⚠  Before committing dpv\_terms.json, check existing OpenREL policy files for which DPV namespace is in use. v1.0 used https://www.w3.org/ns/dpv\# while v2.0 uses https://w3id.org/dpv\# — these are not interchangeable. |
| :---- |

**Version check — run this first**

| \# Check which DPV namespace is currently in use in the KB import os, re policies\_dir \= 'openrel/policies' v1\_pattern   \= re.compile(r'www\\.w3\\.org/ns/dpv') v2\_pattern   \= re.compile(r'w3id\\.org/dpv') v1\_files, v2\_files \= \[\], \[\] for root, \_, files in os.walk(policies\_dir):     for fname in files:         if not fname.endswith('.json'): continue         path \= os.path.join(root, fname)         text \= open(path).read()         if v1\_pattern.search(text): v1\_files.append(path)         elif v2\_pattern.search(text): v2\_files.append(path) print(f'Files using v1.0 namespace: {len(v1\_files)}') for f in v1\_files: print('  ', f) print(f'Files using v2.0 namespace: {len(v2\_files)}') |
| :---- |

**Suggested extraction script**

| import json, urllib.request url \= 'https://w3id.org/dpv/dpv.jsonld' with urllib.request.urlopen(url) as r:     data \= json.load(r) PURPOSE\_IRIS \= \[     'https://w3id.org/dpv\#AcademicResearch',     'https://w3id.org/dpv\#NonCommercialPurpose',     'https://w3id.org/dpv\#ResearchAndDevelopment',     'https://w3id.org/dpv\#ScientificResearch', \] LEGALBASIS\_IRIS \= \[     'https://w3id.org/dpv\#Consent',     'https://w3id.org/dpv\#LegitimateInterest',     'https://w3id.org/dpv\#LegalObligation', \] OPENREL\_MAP \= {     'https://w3id.org/dpv\#AcademicResearch':    'C01',     'https://w3id.org/dpv\#NonCommercialPurpose': 'C02',     'https://w3id.org/dpv\#Consent':             'C03', } output \= {     'dpv\_version': '2.0',     'source':      'https://w3id.org/dpv/dpv.jsonld',     'purposes':    \[\],     'legal\_bases': \[\] } for entry in data.get('@graph', \[\]):     iri   \= entry.get('@id', '')     label \= entry.get('rdfs:label', {}).get('@value', iri.split('\#')\[-1\])     rec   \= {         'iri':                iri,         'label':              label,         'openrel\_constraint': OPENREL\_MAP.get(iri)     }     if iri in PURPOSE\_IRIS:   output\['purposes'\].append(rec)     elif iri in LEGALBASIS\_IRIS: output\['legal\_bases'\].append(rec) with open('dpv\_terms.json', 'w', encoding='utf-8') as f:     json.dump(output, f, ensure\_ascii=False, indent=2) print('dpv\_terms.json written') print(f"  {len(output\['purposes'\])} purpose terms") print(f"  {len(output\['legal\_bases'\])} legal basis terms") |
| :---- |

**Expected output**

| {   "dpv\_version": "2.0",   "source": "https://w3id.org/dpv/dpv.jsonld",   "purposes": \[     {       "iri":                "https://w3id.org/dpv\#AcademicResearch",       "label":              "Academic Research",       "openrel\_constraint": "C01"     },     {       "iri":                "https://w3id.org/dpv\#NonCommercialPurpose",       "label":              "Non-Commercial Purpose",       "openrel\_constraint": "C02"     }   \],   "legal\_bases": \[     {       "iri":                "https://w3id.org/dpv\#Consent",       "label":              "Consent",       "openrel\_constraint": "C03"     }   \] } |
| :---- |

## **Summary — recommended order of execution**

The three scripts are independent and can be run in any order. The suggested sequence below minimises dependency on external services and puts the most stable source first.

| \# | Script | Output file | Manual follow-up |
| :---- | :---- | :---- | :---- |
| **1** | GeoNames download and convert | openrel/lookup/country\_list.json | EU entry included. No manual follow-up. |
| **2** | SPDX filtering | openrel/lookup/spdx\_licences.json | Receive and commit spdx\_openrel\_mapping.json from Melios. |
| **3** | DPV version check \+ extraction | openrel/lookup/dpv\_terms.json | Verify IRI namespace version before committing. Update any v1.0 policy files if needed. |

| ✓  None of these scripts modifies the existing KB structure. They produce new standalone JSON files that are committed as lookup resources. The KB pipeline and the wizard read from these files at load time. |
| :---- |

| Document status: Working draft — suggested scripts for discussion with Wim Hugo (KNAW-DANS) Project: EOSC Beyond · WP14, T14.4 · Grant 101131875 Prepared by: Melios Katsamakis (OpenAIRE)  ·  June 2026 |
| :---- |

