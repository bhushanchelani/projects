# projects

## Composio

[Composio](https://github.com/ComposioHQ/composio) Python SDK (`composio==0.30.0`) is set up here. It connects AI agents to outside apps such as Gmail, Google Sheets and Slack.

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # then paste your COMPOSIO_API_KEY
python composio_check.py
```

Get an API key at https://platform.composio.dev. Never commit `.env`.
