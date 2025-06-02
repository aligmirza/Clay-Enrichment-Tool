# 🔌 Clay Python API

This project lets you call modular Python scripts dynamically from Clay.com using an HTTP POST API.

## 🧰 How it works

- Drop any Python snippet in `/logic/` with a `run(data)` function.
- POST to `/run` with a JSON payload like:

```json
{
  "logic": "add",
  "data": { "a": 5, "b": 3 }
}
```

## 🔐 Secured with API Key

Set `X-API-Key` in your headers. Keys are stored in `.env`.

## 🚀 Deploy on Render, Railway, etc.

Start command: `python api_server.py`
