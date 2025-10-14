# app/core/config.py
import os
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import quote_plus

ENV_PATH = Path(__file__).resolve().parents[2] / ".env"
load_dotenv(ENV_PATH)

# ==== JWT (used by core/security.py) ====
JWT_SECRET = os.getenv("JWT_SECRET", "devsecret_change_me")
ACCESS_TOKEN_MIN = int(os.getenv("ACCESS_TOKEN_MIN", "60"))

# ==== Primary: direct URL if provided (legacy or single-line style) ====
AZURE_SQL_URL = os.getenv("AZURE_SQL_URL") or os.getenv("AZURE_SQL_CONNECTION_STRING")

if not AZURE_SQL_URL:
    # ==== Fallback: build from individual pieces (recommended) ====
    SQL_SERVER  = os.getenv("SQL_SERVER")
    SQL_DB      = os.getenv("SQL_DB")
    SQL_UID     = os.getenv("SQL_UID")
    SQL_PWD     = os.getenv("SQL_PWD")
    SQL_DRIVER  = os.getenv("SQL_DRIVER", "ODBC Driver 17 for SQL Server")
    SQL_TIMEOUT = os.getenv("SQL_TIMEOUT", "30")

    missing = [k for k, v in {
        "SQL_SERVER": SQL_SERVER,
        "SQL_DB": SQL_DB,
        "SQL_UID": SQL_UID,
        "SQL_PWD": SQL_PWD,
    }.items() if not v]
    if missing:
        raise RuntimeError(
            f"Missing DB env vars: {missing}. "
            f"Provide AZURE_SQL_URL (or AZURE_SQL_CONNECTION_STRING) "
            f"OR set SQL_SERVER/SQL_DB/SQL_UID/SQL_PWD in {ENV_PATH}"
        )

    # Build an ODBC connect string and URL-encode it
    odbc = (
        f"DRIVER={{{SQL_DRIVER}}};"
        f"SERVER={SQL_SERVER},1433;"
        f"DATABASE={SQL_DB};"
        f"UID={SQL_UID};"
        f"PWD={SQL_PWD};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        f"Connection Timeout={SQL_TIMEOUT};"
    ).replace("{SQL_DRIVER}", SQL_DRIVER)

    AZURE_SQL_URL = "mssql+pyodbc:///?odbc_connect=" + quote_plus(odbc)
