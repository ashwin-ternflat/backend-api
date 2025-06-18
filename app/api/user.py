from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User, UserOut
from app.services.user_service import create_user, get_user_by_email, fetch_all_users

router = APIRouter()

@router.post("/users", response_model=User)
async def register_user(user: User):
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await create_user(user)

@router.get("/users", response_model=List[UserOut])
async def get_all_users():
    users = await fetch_all_users()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users
