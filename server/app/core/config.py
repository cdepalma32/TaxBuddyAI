# server/app/core/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve .../server/.env from .../server/app/core/config.py
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)

AZURE_SQL_URL = os.getenv("AZURE_SQL_CONNECTION_STRING")

if not AZURE_SQL_URL:
    # helpful fail-fast message during dev
    raise RuntimeError(f"AZURE_SQL_CONNECTION_STRING not set. Checked: {ENV_PATH}")
