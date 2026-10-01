# 🔱 Sanjeevani — LLM Jailbreak Challenge

> *"The true Vidya is never written on any parchment that a thief can reach."*

A **CTF (Capture the Flag)** challenge where participants must extract a hidden secret from an AI persona — **Shukracharya**, the stern guru of the Asuras who guards the Sanjeevani Vidya.

---

## 🎯 Challenge Overview

- **Difficulty:** Medium
- **Category:** LLM Jailbreaking / Prompt Injection
- **Format:** RAG-augmented chatbot with output-side flag filtering

The AI is instructed never to reveal a hidden `KCTF{...}` flag. Participants must use creative prompt engineering, context manipulation, or indirect extraction techniques to make it slip.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Local Ollama (no API key required) / Groq Cloud fallback |
| **Backend** | FastAPI + Uvicorn + httpx |
| **RAG** | Selective keyword-based retrieval (skips DB for generic queries) |
| **Optimization** | Fast-path caching (<1ms response for generic greetings) |
| **Frontend** | Vanilla HTML/CSS/JS · Inter font |
| **Deployment** | Render / Local / Docker |

---

## 🚀 Local Development (No API Key Required)

### 1. Clone & set up

```bash
git clone <repo-url>
cd sanjeevni
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure environment

```bash
cp .env.example .env
# Default uses local Ollama (http://localhost:11434/v1). No API key required!
```

### 3. Run

```bash
uvicorn main:app --reload --port 8000
```

Open [http://localhost:8000](http://localhost:8000)

---

## ☁️ Deploying to Render (Free Tier)

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Set **Build Command:** `pip install -r requirements.txt`
5. Set **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add **Environment Variable:** `GROQ_API_KEY` (optional for cloud Groq inference)
7. Deploy 🎉

---

## 🏗 Architecture

```
User Browser
     │
     ▼
FastAPI (main.py)
     │
     ├── GET /         → Serves index.html (chat UI)
     ├── POST /chat    → Handles conversation
     │       │
     │       ├── 1. Fast-Path: Generic greetings answered instantly (<1ms, No DB, No LLM)
     │       ├── 2. Smart Router: Skips DB retrieval for non-lore queries
     │       ├── 3. Keyword RAG: Fetches lore ONLY when query is lore-relevant
     │       ├── 4. Provider LLM: Ollama local (No API key) / Groq cloud / Fallback
     │       └── 5. Output Filter: Regex-blocks response if flag pattern is matched
     │
     └── GET /health   → Health check & provider status
```

---

## 🔐 Security Design

| Mechanism | Purpose |
|---|---|
| **System-prompt-only flag** | Flag is NOT in RAG documents — pure extraction attacks fail |
| **Decoy flag in RAG** | `KCTF{decoy_not_the_real_one}` traps hasty participants |
| **Output-side regex filter** | Even if the model is tricked, the flag is intercepted server-side |
| **In-character refusal** | Filter replacement stays in persona — doesn't reveal that filtering occurred |
| **Strict system prompt** | Hardened against roleplay overrides, authority claims, multi-turn trust attacks |

---

## 🧩 The Flag

```
KCTF{s4njeev4n1_vidy4_3b8428a850dd}
```

Set `SECRET_FLAG` as an environment variable on Render to avoid hardcoding it.

---

## 📚 Knowledge Base Sources

The RAG knowledge base contains lore adapted from:
- **Mahabharata Adi Parva** — Kacha, Devayani & Shukracharya narrative arc
- **Shukra Niti** — Ethics and philosophy of guarded knowledge
- Decoy documents to challenge participants who submit the first flag-shaped string they find
