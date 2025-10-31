from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session
from sqlalchemy import text
from passlib.hash import bcrypt

from app.db.session import get_db
from app.core.security import create_access_token, verify_token

router = APIRouter(prefix="/auth", tags=["auth"])

# For Swagger “Authorize” button and OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ---------- MODELS ----------
class SignupInput(BaseModel):
    email: EmailStr
    password: str
    role: str = "user"


class LoginInput(BaseModel):
    email: str
    password: str


# ---------- ROUTES ----------
@router.post("/signup", status_code=201)
def signup_user(body: SignupInput, db: Session = Depends(get_db)):
    """Create a new user with a hashed password (passlib bcrypt)."""
    existing = db.execute(
        text("SELECT 1 FROM dbo.users WHERE email = :email"),
        {"email": body.email}
    ).fetchone()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = bcrypt.hash(body.password)

    db.execute(
        text("""
            INSERT INTO dbo.users (email, [password], [role], created_at)
            VALUES (:email, :pw, :role, SYSUTCDATETIME())
        """),
        {"email": body.email, "pw": hashed_pw, "role": body.role}
    )
    db.commit()

    return {"message": "User created successfully"}


@router.post("/login")
def login_user(body: LoginInput, db: Session = Depends(get_db)):
    """Authenticate user and return JWT token."""
    row = db.execute(
        text("""
            SELECT TOP (1) id, email, [password], [role]
            FROM [dbo].[users]
            WHERE email = :email
        """),
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


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    """Validate and decode JWT to retrieve current user."""
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token payload")

    row = db.execute(
        text("""
            SELECT TOP (1) id, email, [role]
            FROM [dbo].[users]
            WHERE email = :email
        """),
        {"email": email}
    ).fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": row.id, "email": row.email, "role": row.role}
