# Customising OpenREL

>Wim Hugo, DANS/ EUDAT | 
>Melios Katsamakis, OpenAIRE | 
>Prodromos Tsiavos, OpenAIRE | 
>09-07-2026 | 
>[CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

## Context

Vocabularies that can be used to encode rights-, access-, sensitive data-related policies and licences (e.g. ODRL, DPV, IDSC, DALICC, and ccREL) often entrench context-specific considerations into RDF Classes. Some examples are:

|Vocabulary|IRI|Description|Issue|
| -------- | -------- | -------- | -------- |
|ODRL| odrl:textToSpeech|To have a text Asset read out loud.|ODRL is relatively free of context-specific class definitions, with one or two exxceptions - such as this one. One can generalise the action of 'Text-to-Speech' as odrl:transform with a constraint, because if it is permitted, it need not be mentioned - all uses are implied if not explicitly prohibited or constrained. A more flexible and extensible encoding would add a left Operand (Transformation Type) and limit or allow the types of transformation with a cepomncept scheme of which 'Text-To-Speech' is one member.|
