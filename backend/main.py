from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI(title="My Spend O'ra 2025")

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
