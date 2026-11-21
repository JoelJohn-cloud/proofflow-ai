# Architecture

```
React UI ─► FastAPI ─► Extraction (pdfplumber/OCR + LLM → JSON)
                 │          ▼
                 │      Matching ─► Validation engine (Decimal)
                 │                        ▼
                 ├────────────► LangGraph agent ◄─► Tools (SQL lookups,
                 │                        ▼          re-validate, find docs)
                 ▼                  Report builder
             PostgreSQL ◄──────── audit trail + human review
```

Rules: arithmetic only in `validation/`; the agent's tools return database facts only; "not found" is a valid result; humans make the final call.
