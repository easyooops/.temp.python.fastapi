from typing import List

from pydantic import BaseModel
from app import schemas

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    items: List[schemas.Item] = []

    class Config:
        orm_mode = True