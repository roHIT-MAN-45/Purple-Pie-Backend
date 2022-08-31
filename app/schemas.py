from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic.types import conint

# Create User Schema
class UserCreate(BaseModel):
    name : str
    phone : str
    email : EmailStr
    password : str

class UserResponse(UserCreate):
    id : int
    created_at : datetime

    class Config :
        orm_mode = True

# Authentication
class LoginUser(BaseModel):
    email : EmailStr
    password : str

# Access token
class Token(BaseModel):
    user_id : Optional[str] = None
    name : str
    token : str
    token_type : str

# Schema for token data
class TokenData(BaseModel):
    id : Optional[str] = None

# Menu Item Post Schema
class MenuItem(BaseModel):
    name : str
    description : str
    category : str
    itemType : str
    price : int
    calories : int
    isFavourite : bool = False # Optional field
    image : str

# Menu Items Response Schema
class MenuItemResponse(MenuItem):
    id : int

    class Config:
        orm_mode = True