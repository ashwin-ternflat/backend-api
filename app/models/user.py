from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    
    username: str
    email: EmailStr
    created_at: Optional[datetime] = None

class UserOut(BaseModel):
    id: str = Field(..., alias="_id")
    username: str
    email: EmailStr
    created_at: datetime

    class Config:
        populate_by_name = True
        from_attributes = True