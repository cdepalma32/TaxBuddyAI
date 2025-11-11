from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.routers.auth import get_current_user

router = APIRouter(prefix="/tax", tags=["tax"])

class TaxInput(BaseModel):
    income: float
    deductions: float

def compute_tip(income: float, deductions: float) -> str:
    if income - deductions > 50000:
        return "Consider itemizing and maxing pre-tax retirement."
    return "Consider maxing out pre-tax retirement contributions."

@router.post("/")
def create_tax_entry(
    body: TaxInput,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    tip = compute_tip(body.income, body.deductions)
    result = db.execute(
        text("""
            INSERT INTO dbo.tax_queries (user_id, income, deductions, tip)
            OUTPUT INSERTED.id
            VALUES (:uid, :income, :deductions, :tip)
        """),
        {"uid": user["id"], "income": body.income, "deductions": body.deductions, "tip": tip}
    )
    inserted_id = result.fetchone()[0]
    db.commit()
    return {"tip": tip, "saved": True, "id": inserted_id}

@router.get("/{id}")
def get_tax_entry(
    id: int,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    row = db.execute(
        text("""
          SELECT TOP (1) id, user_id, income, deductions, tip, created_at
          FROM dbo.tax_queries
          WHERE id = :id AND user_id = :uid
        """),
        {"id": id, "uid": user["id"]}
    ).fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Entry not found")

    return {
        "id": row.id,
        "income": float(row.income),
        "deductions": float(row.deductions),
        "tip": row.tip,
        "created_at": row.created_at.isoformat() if row.created_at else None,
    }
