from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter()

class TaxFormInput(BaseModel):
    income: float
    deductions: float

@router.post("/")
def get_tax_tip(data: TaxFormInput):
    # placeholder LLM response
    return {"tip": f"Try adjusting deductions from ${data.deductions} on ${data.income} income."}
