from fastapi import FastAPI
from app.core.config import settings
from app.api import user

app = FastAPI(title=settings.app_name)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Backend API is running"}
