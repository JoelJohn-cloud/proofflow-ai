# ProofFlow AI

> An autonomous agent that investigates invoices against purchase orders and delivery receipts, finds discrepancies, looks for the evidence that explains them, and reports what is verified and what is not.

Built for **Homingo Hack Days 2026** (build phase: 21 Nov – 6 Dec 2026), AI Agents track.

ProofFlow reports discrepancies and evidence. It never says "fraud" and never approves a payment; a human reviews every finding.

## How it works
1. Upload a purchase order, invoice and delivery receipt.
2. An LLM extracts fields into a validated JSON schema.
3. Documents are matched by PO number, supplier and date.
4. Python (`Decimal`) checks quantity, price, totals, tax and duplicates. The LLM never does arithmetic.
5. A LangGraph agent investigates each finding with tools (e.g. search for a PO amendment) and updates its conclusion.
6. A report lists findings as *verified*, *anomaly*, *missing info* or *assumption*, each linked to its source.
7. A human approves or dismisses.

## AI tools, models and libraries
| Type | Name | Used for |
|------|------|----------|
| Model | Groq or Gemini API (set `LLM_MODEL` in `.env`) | Field extraction and investigation reasoning |
| Agent framework | LangGraph | Controlled multi-step investigation workflow |
| Library | pdfplumber / PyMuPDF | PDF text extraction |
| Library | Pydantic | Validating extracted JSON |
| Library | FastAPI | Backend API |
| Library | Python `Decimal` | Exact financial arithmetic |
| Editor | VS Code | Development |
| AI assistant | Claude | Planning and code assistance (all AI-written code is reviewed by the team) |

## Quick start
```bash
git clone https://github.com/<username>/proofflow-ai.git
cd proofflow-ai
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                  # add your API key and model name
python scripts/check_model.py                         # one successful model call
pytest                                                # runs the tests
uvicorn app.main:app --reload --app-dir backend       # http://localhost:8000/health
docker compose up -d db                               # optional: Postgres
```

## Project docs
- [Project brief](docs/PROJECT_BRIEF.md): who it's for, the one task, "finished", first-weekend target, team
- [Architecture](docs/architecture.md)

## Status
- [ ] Dashboard checked (hackathon.homingo.co.in/me)
- [x] Repo and README
- [ ] Model call works (`scripts/check_model.py`)
- [ ] First end-to-end path
- [ ] Evaluation results (none yet; numbers will come only from our own dataset)

## Data
Only synthetic documents are used. No real financial data, no API keys in the repo.
