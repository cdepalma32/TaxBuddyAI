from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.post("/login")
def login_user(credentials: dict):
    return {"token": "mock-token", "refresh": "mock-refresh-token"}

# Add this for now—can improve later
def get_current_user():
    # This should eventually verify user/session/token
    return {"user": "mock-user"}
