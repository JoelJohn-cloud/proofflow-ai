"""Makes ONE call to your chosen LLM to confirm the key and model work.

Setup: copy .env.example to .env, fill LLM_PROVIDER, LLM_API_KEY, LLM_MODEL.
Run:   python scripts/check_model.py
"""
import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("LLM_PROVIDER", "groq").lower()
api_key = os.getenv("LLM_API_KEY", "")
model = os.getenv("LLM_MODEL", "")
prompt = "Reply with exactly: ProofFlow model check OK"

if not api_key or not model:
    sys.exit("Set LLM_API_KEY and LLM_MODEL in .env first (pick a model from your provider's current list).")

try:
    if provider == "groq":
        r = httpx.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {api_key}"},
            json={"model": model, "messages": [{"role": "user", "content": prompt}]},
            timeout=30,
        )
        r.raise_for_status()
        text = r.json()["choices"][0]["message"]["content"]
    elif provider == "gemini":
        r = httpx.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent",
            headers={"x-goog-api-key": api_key},
            json={"contents": [{"parts": [{"text": prompt}]}]},
            timeout=30,
        )
        r.raise_for_status()
        text = r.json()["candidates"][0]["content"]["parts"][0]["text"]
    else:
        sys.exit("LLM_PROVIDER must be 'groq' or 'gemini'.")
except httpx.HTTPStatusError as e:
    sys.exit(f"API error {e.response.status_code}: {e.response.text[:300]}")
except Exception as e:
    sys.exit(f"Call failed: {e}")

print(f"[{provider} / {model}] says: {text.strip()}")
