# ProofFlow AI – Project Brief

## Who it's for
Accounts-payable teams at small and mid-size companies who compare invoices, POs and delivery receipts by hand.

## The one task it does
Given a PO, invoice and delivery receipt, find discrepancies and investigate them with evidence, so a human can decide quickly.

## What "finished" looks like
- [ ] Upload 3 PDFs and get structured extraction
- [ ] Documents matched; unmatched ones flagged, not guessed
- [ ] Quantity, price, total, tax and duplicate checks done in Python `Decimal`
- [ ] Agent uses tools (amendment search, receipt search, re-validate) and updates findings
- [ ] Report separates verified / anomaly / missing info / assumption, every item traceable to a source
- [ ] Human can approve or dismiss and add notes; nothing is auto-approved
- [ ] Evaluated on our own synthetic dataset with a written method (no invented numbers)

## First-weekend target (by Sun 22 Nov)
One rough end-to-end path with **synthetic JSON input** (no PDFs yet):
`PO + invoice + receipt JSON → quantity check → agent searches for a PO amendment → printed report`

Example case: PO 80 units, invoice 100 units, receipt 80 units, no amendment found. The report must say the 20-unit gap is verified, the cause is unverified, and an amendment was searched for and not found.

## Team and ownership
| Name | Owns |
|------|------|
| Joel | Agent and tools (LangGraph) |
| <Member 2> | Extraction and matching |
| <Member 3> | Validation engine, tests, evaluation |
| <Member 4> | Frontend, reports, README and demo |

**Daily check-in:** <time> (fill in)
