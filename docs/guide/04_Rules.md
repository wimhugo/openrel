# Rules and Duties

> OpenREL user guidance | Aligned with OpenREL Specification V0.5.2 | CC BY 4.0

> This is implementation guidance. The specification and published RDF/SHACL definitions take precedence if any discrepancy is found.

ODRL defines `odrl:Permission`, `odrl:Prohibition` and `odrl:Duty`. OpenREL retains these foundational rule semantics.

OpenREL further distinguishes:

- `openrel:PreDuty` — a duty that must be fulfilled before the associated action is executed, subject to the applicable policy conditions.
- `openrel:PostDuty` — a duty fulfilled after execution of the associated action. Failure to fulfil it may constitute a policy violation, but does not by itself prevent initial execution.

The distinction is important when computing `PERMIT`, `CONDITIONAL`, or `DENY`: an unsatisfied pre-duty can prevent immediate authorisation, while a post-duty can remain an obligation following an authorised action.

Do not infer that all duties are preconditions. Nor should a post-duty be ignored simply because it does not block the initial action. See [Evaluation](13_Evaluation.md).
