from app.core.database import db
from app.models.user import User
from datetime import datetime
from app.core.database import get_user_collection
from datetime import datetime, timezone
from pymongo import ReturnDocument

async def create_user(user: User):
    user_dict = user.model_dump()

    user_dict["created_at"] = datetime.now(timezone.utc).isoformat()
    result = await db["users"].insert_one(user_dict)
    user_dict["_id"] = str(result.inserted_id)
    return user_dict

async def get_user_by_email(email: str):
    data = await db["users"].find_one({"email": email})
    return User(**data) if data else None

async def fetch_all_users():
    user_collection = get_user_collection()
    users = []
    async for user in user_collection.find({}):
        user["_id"] = str(user["_id"])
        users.append(user)
    return users

async def update_user(email: str, update_data: dict):
    updated_user = await db["users"].find_one_and_update(
        {"email": email},
        {"$set": update_data},
        return_document=ReturnDocument.AFTER
    )
    if updated_user:
        updated_user["_id"] = str(updated_user["_id"])
    return updated_user

async def delete_user(email: str):
    result = await db["users"].delete_one({"email": email})
    return result.deleted_count > 0
