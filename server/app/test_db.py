from sqlalchemy import create_engine, text
from app.core.config import AZURE_SQL_URL

engine = create_engine(AZURE_SQL_URL)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        print("✅ Connection successful:", result.fetchone())
except Exception as e:
    print("❌ Connection failed:", e)
