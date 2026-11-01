"""Verify the Composio SDK is installed and, if an API key is set, can reach the API."""
import os

from dotenv import load_dotenv
from composio import Composio

load_dotenv()

if not os.getenv("COMPOSIO_API_KEY"):
    print("Composio SDK installed. Set COMPOSIO_API_KEY in .env to test the connection.")
    raise SystemExit(0)

composio = Composio()
toolkits = composio.toolkits.get()
print(f"Connected to Composio. {len(toolkits)} toolkits available, e.g.:")
for tk in toolkits[:10]:
    print(" -", getattr(tk, "slug", tk))
