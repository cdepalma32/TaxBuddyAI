from fastapi import APIRouter, Depends
from pydantic import BaseModel    
from sqlalchemy.orm import Session
from sqlalchemy import text

from app.db.session import get_db
from app.routers.auth import get_current_user

router = APIRouter(prefix="/tax", tags=["tax"])

class TaxFormInput(BaseModel):
    income: float
    deductions: float

@router.post("/")
def get_tax_tip(
    data: TaxFormInput,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),   # ← JWT required
):
    prompt = f"Suggest a tax-saving tip for income: {data.income}, deductions: {data.deductions}"
    # call_openai(prompt)  # if you have it wired; else return a stub
    return {"tip": f"Consider maxing out pre-tax retirement contributions, {current_user['email']}."}
