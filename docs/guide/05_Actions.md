# Actions

>Wim Hugo, DANS/ EUDAT | 

>Melios Katsamakis, OpenAIRE | 

>Prodromos Tsiavos, OpenAIRE | 

>09-07-2026 | [CC BY 4.0](https://spdx.org/licenses/CC-BY-4.0.html)
---

[RDF Turtle Representation](https://github.com/wimhugo/openrel/blob/main/.openrel/vocabs/openrel/actions.ttl)

## Summary

ODRL defines a wide variety of Actions classes and subclasses, and these are also widely duplicated in other vocabularies (ccREL [^1], DUO [^2], DPV [^3], IDSC [^4], and so on).

OpenREL has defined a number of additional Actions to assist especially with encoding of Rules related to subject and curator rights, as well as ethical and legal concerns applicable to the research data (output) management landscape. OpenREL has also redefined the Actions previously included into d  the DALICC [^5] vocabulary, allowing DALICC-encoded licences to be cross-walked to OpenREL encodings.

## Extension Types

OpenREL has made extension to existing ODRL Action classes, specifically in respect of mappings from ccREL, DALICC, IDSC, DUO, and DPV. In cases where DALICC defined a new action (one that cannot be mapped to an existing ODRL Action), OpenREL redefined the DALICC Action and included it into the vocabulary.

There are three motivations for these extensions:
- It allows any API development to present a full complement of Actions from all relevant sources, assisting with creation of new policies, matching and comparing existing ones, and helping users with understanding the scope of available Actions.
- It allows crosswalks from Policies that may have been encoded using a different vocabulary to a common one for purposes of reuse and comparison.
- DALICC introduced an additional property to Actions, and that entails *contradiction* between two actions - a necessary extension to assist a *Reasoner*.

## Design Approach: Action or Constraint?

There is a common tendency to define Actions that are quite specific, for example dalicc:modificationNotice and dalicc:attributionNotice both describe actions that require a notice to be provided, and a separate action is defined for each type of notice.

OpenREL generalises these Actions to one that can be tailored for a specific purpose using Left and Right Operands expressed in a Constraint. For example, OpenREL defines an Action (openrel:Notify) which can be refined by way of one or more constraints to indicate all of the duties that require notification - to an external or internal log, to a usage event log, to a clearinghouse, an attribution note, or any other target for such notification. This arrangement allows simpler extension by defining new concepts (vocabulary) rather than defining new classes. 



[^1]: https://creativecommons.org/ns#
[^2]: https://github.com/EBISPOT/DUO 
[^3]: https://w3id.org/dpv
[^4]: https://w3id.org/idsa/core/
[^5]: https://dalicc.net/ns#
