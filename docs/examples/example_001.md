# 	Non-Commercial Use Permitting Distribution Cost Recovery

This is a common use case, and in some cases, permits the recovery of e.g. distribution costs.

## Sources

[Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)

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







