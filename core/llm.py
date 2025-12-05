import os
import requests
from dotenv import load_dotenv

# -------------------------------------------------
# Load .env from project root (one level above /core)
# -------------------------------------------------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(PROJECT_ROOT, ".env")
load_dotenv(DOTENV_PATH)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(f"Missing GROQ_API_KEY in .env file at: {DOTENV_PATH}")

API_URL = "https://api.groq.com/openai/v1/chat/completions"
DEFAULT_MODEL = "llama-3.1-8b-instant"


def ask_llm(prompt: str, model: str = DEFAULT_MODEL) -> str:
    """
    Call Groq's chat completion API with a simple text prompt.
    Returns the model's reply as a string.
    On error, returns a short human-readable message instead of raw JSON.
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 1024,
    }

    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=30)

        # If Groq returns an error (rate limit, bad model, etc.)
        if resp.status_code != 200:
            # Keep it short so UI doesn't show massive JSON
            return f"⚠️ LLM Error {resp.status_code}: {resp.text[:200]}"

        data = resp.json()
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        # Any network/other error
        return f"⚠️ LLM Request Failed: {str(e)[:200]}"

