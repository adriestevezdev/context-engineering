from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.models.user import UserPlan


class UserBase(BaseModel):
    email: EmailStr
    name: str
    plan: UserPlan = UserPlan.FREE


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    name: str | None = None
    plan: UserPlan | None = None


class UserInDBBase(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    pass