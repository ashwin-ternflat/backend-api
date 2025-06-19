import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Your App"
    mongo_uri: str = os.getenv("MONGO_URI", "mongodb://localhost:27017/backend_api_db")
    mongo_db_name: str 
    class Config:
        env_file = ".env"

settings = Settings()
