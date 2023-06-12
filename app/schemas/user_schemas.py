from pydantic import BaseModel, EmailStr
from typing import Optional, List
from ..utils.enums import Roles
from datetime import datetime


# user schemas
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    role: Roles

    class Config:
        orm_mode = True


class CreateUser(BaseUser):
    password: str


class UpdateUser(BaseUser):
    password: Optional[str]


class LoginUser(BaseModel):
    username: str
    password: str


class LoginResponse(BaseUser):
    access_token: str

    class Config:
        orm_mode = True


class CreateUserResponse(BaseUser):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class UserDetails(BaseUser):
    id: int
    is_active: bool
    addresses: List
    orders: List
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class TokenData(BaseModel):
    id: Optional[str] = None