import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__ + "/..")))

from app.db import engine

try:
    with engine.connect() as connection:
        print("✅ Connected to Azure SQL Database!")
except Exception as e:
    print("❌ Connection failed:", e)
