from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import AZURE_SQL_URL

# Create the SQLAlchemy engine using the URL from config.py
engine = create_engine(AZURE_SQL_URL)

# Set up the session factory to manage DB sesssions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


