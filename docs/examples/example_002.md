
# 	Recording Changes to an Asset In Situ

Licences often require the end user to record any modifications as text within the asset without modifying the licence or removing earlier comments - very common in software licences, and good practice for all asset types.

There is a nuance here that is important: ODRL provides two Actions that are related and applicable: odrl:derive and odrl:modify. OpenREL has amended and clarified the distinction some more for a specific reason, and that concerns the relation between an asset and its persistent identifier. These depend on the intention of the asset woner or curator, as explained below. (2)

|Best Practice Case| Description| ODRL Interpretation| OpenREL Interpretation|
|:-----|:-----|:-----|:-----|
|Checksum|The asset is considered to be derived from the original if a modification results in a checksum change, even for very minor changes such as a correction of a typographical error.|odrl:modify|openrel:derive|

## Sources

1. [Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)

## Encoding Example


```
  [ a odrl:Permission ;
      odrl:action openrel:costRecovery 
        [ a odrl:Constraint ;
            odrl:leftOperand openrel:revenueSource ;
            odrl:operator odrl:eq ;`
            odrl:rightOperand trsp:distributionFee ;
        ],           
  ] ;
```


The example encodes the following human-readable statement: 

>"You are permitted to recover costs of making derived works available to third parties, but in doing so, you must only charge a distribution fee and not recover any other costs." 

This example encodes the permission to recover dustribution costs. It utilises the following vocabulary concepts:

|Concept|Description|Source|
|:-------|:------|:-----|
|openrel:costRecovery|Action to recover costs invilved in creating and distributing a derived asset. |[OpenREL Actions](https://github.com/wimhugo/openrel/edit/main/.openrel/vocabs/openrel/actions.ttl)| 
|openrel:revenueSource| OpenREL defines a Left Operand that can indicate one or more types of revenue source. |OpenREL Left Operands|
|trsp:distributionFee | Options for types of cost recovery (Right Operand) is based on 'Revenue Source Types' associated with RDMI, as defined by [TRSP](https://github.com/wimhugo/kb-attributes-eden-fidelis-trsp)|[TRSP Revenue Sources](https://github.com/wimhugo/kb-attributes-eden-fidelis-trsp/blob/main/.configs/vocabs/attr/revenue-source-type.ttl)|






