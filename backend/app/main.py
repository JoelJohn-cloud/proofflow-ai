"""FastAPI entry point. Other modules (api, extraction, ...) plug in here later."""
from fastapi import FastAPI

app = FastAPI(title="ProofFlow AI")


@app.get("/health")
def health() -> dict:
    """Simple check that the server is running."""
    return {"status": "ok"}
