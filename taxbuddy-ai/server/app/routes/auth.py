from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.post("/login")
def login_user(credentials: dict):
    return {"token": "mock-token", "refresh": "mock-refresh-token"}

