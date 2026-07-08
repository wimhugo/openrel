
# 	Recording Changes to an Asset In Situ

Licences often require the end user to record any modifications as text within the asset without modifying the licence or removing earlier comments - very common in software licences, and good practice for all asset types.

There is a nuance here that is important: ODRL provides two Actions that are related and applicable: odrl:derive and odrl:modify. OpenREL has amended and clarified the distinction some more for a specific reason, and that concerns the relation between an asset and its persistent identifier. These depend on the intention of the asset owner or curator, as explained below. (2)

|Best Practice Case| Description| ODRL Interpretation| OpenREL Interpretation|
|:-----|:-----|:-----|:-----|
|Checksum|The asset is considered to be derived from the original if a modification results in a checksum change, even for very minor changes such as a correction of a typographical error.|odrl:modify|openrel:derive|
|Semantic Equivalence| The modified or derived asset is semantically equivalent to the original asset| odrl:derive |openrel:modify|
|Citation Equivalence| Any results based on the original asset remain achievable with the modified or derived asset. This is commonly the case for e.g. datasets where the metadata or semantic linking has been improved, or code that has been optimised or ported but respects the same input and output specifications| odrl:modify| openrel:modify|
|Role Equivalence| The PID resolves to a potentially very different asset over time, but the role of the asset remains the same - for example a data policy or a list of recommended sources of information|odrl:derive|openrel:derive or openrel:modify|

Any work that combines two or more assets will always be encoded as permission to derive a new asset, and will have a new persistent identifier as a matter of course.

## Sources

(1) [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)

(2) Hugo, W., Van de Sompel, H., & Hakala, J. (2025). The PID Landscape - a Technical View (1.1). Zenodo. [https://doi.org/10.5281/zenodo.14881287](https://doi.org/10.5281/zenodo.14881287) 

## Encoding Example


```
  [ a odrl:Permission ;
      odrl:action odrl:modify ;
      odrl:duty 
          [ a odrl:Duty ;
              odrl:action cc:Attribution ],
          [ a odrl:Duty ;
              odrl:action openrel:notify ;
                  odrl:constraint
                  [ a odrl:Constraint ;
                      odrl:leftOperand openrel:notificationType ;
                      odrl:operator odrl:eq ;
                      odrl:rightOperand openrel:record-in-asset 
                  ],
          ]   
  ],

  [ a odrl:Permission ;
      odrl:action odrl:derive ;
      odrl:duty [ a odrl:Duty ;
              odrl:action openrel:attribute ],
          [ a odrl:Duty ;
              odrl:action openrel:notify ;
                  odrl:constraint
                  [ a odrl:Constraint ;
                      odrl:leftOperand openrel:notificationType ;
                      odrl:operator odrl:eq ;
                      odrl:rightOperand openrel:record-in-asset 
                  ],
  ]
```


The example encodes the following human-readable statement: 

>"You are permitted to create modified or derived works from the asset, but in doing so, you must cite the original source, and record any changes you make in the derived or modified work or its metadata."

In practice, for datasets, this typically involves recording provenence in the asset metadata, and in source code, adding comments to the original licence and change statements to reflect modifications.

This example encodes the dutoes to attibute (cite) and to record changess. It utilises the following vocabulary concepts:

|Concept|Description|Source|
|:-------|:------|:-----|
|openrel:modiy|Action to modify an asset. |[OpenREL Actions](https://github.com/wimhugo/openrel/edit/main/.openrel/vocabs/openrel/actions.ttl)| 
|openrel:derive|Action to derive a new asset. |[OpenREL Actions](https://github.com/wimhugo/openrel/edit/main/.openrel/vocabs/openrel/actions.ttl)| 
|openrel:attribute| Creative Commons defines the action of attribution, as does ODRL. The OpenREL definition contains these and other relavant mappings, enabling crosswalks of the encoding. |[OpenREL Actions](https://github.com/wimhugo/openrel/edit/main/.openrel/vocabs/openrel/actions.ttl)|
|openrel:notificationType| OpenREL defines a Left Operand that can indicate one or more types of notification that is required. |OpenREL Left Operands|
|openrel:record-in-asset  |OpenREL provides a vocabulary for definition of a number of notification types and targets |[OpenREL Notification Types](https://github.com/wimhugo/openrel/blob/main/.openrel/vocabs/openrel/type_notification-purpose.ttl)|






