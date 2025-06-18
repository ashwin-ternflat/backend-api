from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from app.core.config import settings

client = AsyncIOMotorClient(settings.mongo_uri)
db = client[settings.mongo_db_name]

def get_user_collection() -> Collection:
    return db.get_collection("users")
