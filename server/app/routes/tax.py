from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.services.llm import call_openai
from app.db import SessionLocal
from app.routes.auth import get_current_user  # or wherever your auth dep lives

router = APIRouter()

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic input model
class TaxFormInput(BaseModel):
    income: float
    deductions: float

# AI-generated tax tip (auth + LLM integration)
@router.post("/")
def get_tax_tip(
    data: TaxFormInput,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    prompt = f"Suggest a tax-saving tip for income: {data.income}, deductions: {data.deductions}"
    response = call_openai(prompt)

    # (Optional) Save to DB here using SQLAlchemy models

    return {"tip": response}

# Health check
@router.get("/check")
def check_connection(db: Session = Depends(get_db)):
    result = db.execute("SELECT 1").fetchone()
    return {"status": "connected", "result": result}

