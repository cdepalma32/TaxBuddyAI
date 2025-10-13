from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

# Request body model
class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_user(credentials: LoginInput):
    # TODO: verify user & issue real JWT
    return {
        "access_token": "mock-token",
        "token_type": "bearer",
        "refresh_token": "mock-refresh-token",
        "user": {"email": credentials.email}
    }

# Temporary dependency used by protected routes
def get_current_user():
    # TODO: decode/verify JWT from Authorization header
    return {"id": 1, "email": "demo@example.com"}
