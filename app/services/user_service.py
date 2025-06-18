from app.core.database import db
from app.models.user import User
from datetime import datetime
from app.core.database import get_user_collection
from datetime import datetime, timezone


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
