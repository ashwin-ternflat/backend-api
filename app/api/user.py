from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.services.user_service import create_user, get_user_by_email

router = APIRouter() 

@router.post("/users", response_model=User)
async def register_user(user: User):
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(user)
