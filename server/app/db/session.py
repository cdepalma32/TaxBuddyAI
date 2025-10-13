# server/app/db.py
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import AZURE_SQL_URL


# Create the SQLAlchemy engine using the URL from config.py
# pool_pre_ping helps avoid stale connections (useful locally and on Azure)
engine = create_engine(
    AZURE_SQL_URL,
    echo=False,
    pool_pre_ping=True,
)

# Session factory
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional: quick connectivity check used on startup
def ping_db():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
