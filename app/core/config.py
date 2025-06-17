from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "BackendAPI"
    mongo_uri: str
    mongo_db: str

    class Config:
        env_file = ".env"

settings = Settings()
