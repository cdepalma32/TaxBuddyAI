# Server/app/main.py  - application root
from fastapi import FastAPI
from contextlib import asynccontextmanager
# Import path for ping_db after moving to db/session.py
from app.db.session import ping_db
from app.routers.tax import router as tax_router
from app.routers.auth import router as auth_router

# Infra checks / startup logic
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

# Feature composition
app.include_router(auth_router)
app.include_router(tax_router)

from fastapi.openapi.utils import get_openapi  # <-- add import

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        routes=app.routes,
        description="TaxBuddy AI API",
    )
    openapi_schema.setdefault("components", {}).setdefault("securitySchemes", {})
    openapi_schema["components"]["securitySchemes"]["bearerAuth"] = {
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "JWT",
    }
    # Require bearer by default for all routes (you can still override per-route)
    openapi_schema["security"] = [{"bearerAuth": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

#health + debug
@app.get("/")
def home():
    return {"status": "ok", "routes": ["/auth/login", "/tax/check", "/docs"]}
