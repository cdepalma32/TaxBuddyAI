# server/app/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import ping_db
from .routes.tax import router as tax_router
from .routes.auth import router as auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- startup ---
    try:
        ping_db()
    except Exception as e:
        print(f"DB ping failed on startup: {e}")

    # (optional) list registered routes for debugging
    for r in app.router.routes:
        try:
            print("ROUTE:", r.path)
        except Exception:
            pass

    yield  # hand off to the app

    # --- shutdown ---
    # nothing to clean up yet (SQLAlchemy engine handles its own pools)

app = FastAPI(title="TaxBuddy AI API", version="0.1.0", lifespan=lifespan)

app.include_router(auth_router)
app.include_router(tax_router)

@app.get("/")
def home():
    return {"status": "ok", "routes": ["/auth/login", "/tax/check", "/docs"]}
