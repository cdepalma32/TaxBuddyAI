from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from passlib.hash import bcrypt

from app.db.session import get_db
from app.core.security import create_access_token, verify_token

router = APIRouter(prefix="/auth", tags=["auth"])

# This creates the Swagger "Authorize" button
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(body: LoginInput, db: Session = Depends(get_db)):
    # fetch user by email using raw SQL
    row = db.execute(
        text("SELECT TOP (1) id, email, [password], [role] FROM [dbo].[users] WHERE email = :email"),
        {"email": body.email}
    ).fetchone()

    if not row:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not bcrypt.verify(body.password, row.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token(sub=row.email)
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {"id": row.id, "email": row.email, "role": row.role},
    }

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    # OPTIONAL: ensure the user still exists (simple check)
    row = db.execute(
        text("SELECT TOP (1) id, email, [role] FROM [dbo].[users] WHERE email = :email"),
        {"email": email}
    ).fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    # return a lightweight user dict
    return {"id": row.id, "email": row.email, "role": row.role}
