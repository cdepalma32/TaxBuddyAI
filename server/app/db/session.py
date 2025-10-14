from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from app.core.config import AZURE_SQL_URL

engine = create_engine(
    AZURE_SQL_URL, 
    pool_pre_ping=True, 
    pool_recycle=1800,
    pool_size=5,
    max_overflow=10,
    future=True)
    
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def ping_db():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
