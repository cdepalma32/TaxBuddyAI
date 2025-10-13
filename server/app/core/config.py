# server/app/core/config.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve .../server/.env from .../server/app/core/config.py
ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)

# Read either new or old name (new preferred)
AZURE_SQL_URL = os.getenv("AZURE_SQL_URL") or os.getenv("AZURE_SQL_CONNECTION_STRING")
if not AZURE_SQL_URL:
    raise RuntimeError(f"AZURE_SQL_URL / AZURE_SQL_CONNECTION_STRING not set. Checked: {ENV_PATH}")

# # Optional: centralize JWT envs (used by core/security.py)
# JWT_SECRET = os.getenv("JWT_SECRET", "devsecret_change_me")
# ACCESS_TOKEN_MIN = int(os.getenv("ACCESS_TOKEN_MIN", "60"))