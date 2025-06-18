from fastapi import APIRouter, HTTPException
from typing import List
from app.models.user import User, UserOut
from app.services.user_service import create_user, get_user_by_email, fetch_all_users,update_user,delete_user
from app.models.user import UpdateUser

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

@router.put("/users/{email}", response_model=UserOut)
async def update_existing_user(email: str, user_update: UpdateUser):
    updated = await update_user(email, user_update.model_dump(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated

@router.delete("/users/{email}")
async def delete_existing_user(email: str):
    deleted = await delete_user(email)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return {"detail": "User deleted successfully"}
