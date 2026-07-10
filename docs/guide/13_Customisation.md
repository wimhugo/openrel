# Customising OpenREL

>Wim Hugo, DANS/ EUDAT | 
>Melios Katsamakis, OpenAIRE | 
>Prodromos Tsiavos, OpenAIRE | 
>09-07-2026 | 
>[CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

## Context

Vocabularies that can be used to encode rights-, access-, sensitive data-related policies and licences (e.g. ODRL, DPV, IDSC, DALICC, and ccREL) often entrench context-specific considerations into RDF Classes. The implication is that if a new context is identified or is different from what is encodable already, classes have to be added to the vocabulary to accomodate the new context, spawning a new version and for stable vocabualries, a potentially lengthy review and release process. Some examples are:

|Vocabulary|IRI|Description|Issue|
| -------- | -------- | -------- | -------- |
|ODRL| odrl:textToSpeech|To have a text Asset read out loud.|ODRL is relatively free of context-specific class definitions, with one or two exxceptions - such as this one. It is just one of many possible transformations of content and should be made more flexible, since each context may want to encode a different set of applicable transformations|
[ccREL|cc:CommercialUse| |This is just one of many potential ways in which revenue can be generated from disseminated, derived or modified Assets - it is, for example, also possible to have non-commercial revenue by recovering dissemination and packaging costs.|

