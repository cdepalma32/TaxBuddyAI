from fastapi import FastAPI
from app.routes import auth, tax

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(tax.router, prefix="/tax")
