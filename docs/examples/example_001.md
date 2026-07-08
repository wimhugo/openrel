# 	Non-Commercial Use

This is a common use case, and in some cases, permits the recovery of e.g. distribution costs.

## Sources

[Creative Commons Attribution-NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/)

## Encoding Example


`  [ a odrl:Permission ;`
`      odrl:action openrel:costRecovery `
`        [ a odrl:Constraint ;`
`            odrl:leftOperand openrel:leftOperand.revenuSource ;`
`            odrl:operator odrl:eq ;`
`            odrl:rightOperand trsp:distributionFee ; `
`        ],`            
`  ] ;`


The example encodes the following human-readable statement: 

>"You are permitted to recover costs of making derived works available to third parties, but in doing so, you must only charge a distribution fee and not recover any other costs." 

This example encodes the permission to recover dustribution costs. It utilises the following vocabulary concepts:

|Concept|Description|Source|
|:-------|:------|:-----|
|openrel:costRecovery|Action to recover costs invilved in creating and distributing a derbibved asset. Options for types of cost revocery is based on 'Revenue Source Types' associated with RDMI, as defined by [TRSP](https://github.com/wimhugo/kb-attributes-eden-fidelis-trsp/blob/main/.configs/vocabs/attr/revenue-source-type.ttl)|[OpenREL Actions](https://github.com/wimhugo/openrel/edit/main/.openrel/vocabs/openrel/actions.ttl)| 
