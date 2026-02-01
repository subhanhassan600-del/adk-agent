# ADK Project

This repository contains a small FastAPI-based server used to experiment with an LLM generation API running locally (via Ollama or a similar service). The README explains how to start the server, how to call the model endpoint, and troubleshooting steps for common issues (for example, JSON decode errors when the response is not valid JSON).

## Quick Start

- Create and activate the virtual environment (if not already active):

```bash
python3 -m venv adk-env
source adk-env/bin/activate
pip install -r requirements.txt  # if present
```

- Start the FastAPI server (from repository root):

```bash
uvicorn main:app --reload
```

The server will start on http://127.0.0.1:8000 by default. Some local integrations (like Ollama) may listen on other ports (e.g. `11434`) — check `ollama_api.py` or any test scripts for the exact URL used.

## What this project does

- `main.py`: FastAPI app that exposes routes for generating text using a local LLM API.
- `ollama_api.py`: Helper module that communicates with the local model service (example: Ollama). It wraps HTTP calls and should handle request/response formatting.

The typical flow:

1. A client (browser, curl) sends a POST request to the FastAPI endpoint.
2. The FastAPI handler forwards the request to the local LLM service via `ollama_api.py`.
3. The LLM service returns a response (often JSON). The handler validates and returns that to the original client.

## Next steps / Improvements

- Add a `requirements.txt` or `pyproject.toml` with pinned dependencies.
- Improve error handling in `ollama_api.py` to normalize responses (NDJSON, streaming, or single JSON).
- Add unit tests to validate parsing logic and endpoint behavior.

If you'd like, I can also: run the test script, inspect `ollama_api.py` to harden parsing, or add a `requirements.txt` for this environment.

