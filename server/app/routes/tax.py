# server/app/routes/tax.py
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db import get_db
from app.routes.auth import get_current_user
from app.services.llm import call_openai

router = APIRouter(prefix="/tax", tags=["tax"])

# ---------- Schemas ----------
class TaxFormInput(BaseModel):
    income: float
    deductions: float

class CheckResponse(BaseModel):            # <-- NEW: response model for /tax/check
    status: str
    ok: int

# ---------- Routes ----------
@router.post("/")
def get_tax_tip(
    data: TaxFormInput,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Protected endpoint:
    - Requires a valid JWT via get_current_user (auth.py).
    - Calls LLM to generate a tip (stub/real).
    - (Later) Persist request/response to Azure SQL.
    """
    prompt = f"Suggest a tax-saving tip for income: {data.income}, deductions: {data.deductions}"
    response = call_openai(prompt)
    return {"tip": response}

@router.get("/check", response_model=CheckResponse)    # <-- NEW: docs schema
def check_connection(db: Session = Depends(get_db)):
    try:
        row = db.execute(text("SELECT 1 AS ok")).fetchone()
        # ensure integers for schema
        ok_value = int(row.ok) if row and row.ok is not None else 0
        return {"status": "connected", "ok": ok_value}
    except Exception as e:
        # keep helpful error detail while developing
        print("DB CHECK ERROR:", repr(e))
        return JSONResponse(
            status_code=500,
            content={"detail": "DB error", "error": str(e)},
        )
