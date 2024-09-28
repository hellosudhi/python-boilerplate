# src/model/models.py
from pydantic import BaseModel,Field,EmailStr
from bson import ObjectId
from typing import Optional

# Custom class to handle Mongodb Objectid validaton
class PyObjectId(ObjectId):
 @classmethod
 def __get_validators__(cls):
  yield cls.validate
 
 @classmethod
 def validate(cls,v):
  if not ObjectId.is_valid(v):
   raise ValueError("Invalid ObjectId")
  return ObjectId(v)

# User Model
class UserModel(BaseModel):
 username: str = Field(...,min_length=6,max_length=30)
 email: EmailStr
 password: str = Field(...,min_length=8)

# Inherit from UserModel
class UserInDB(UserModel):
  id:PyObjectId = Field(default_factory=PyObjectId,alias="_id")

class UserUpdateModel(BaseModel):
 username: Optional[str] = Field(None,min_length=6,max_length=30)
 email: Optional[EmailStr] = None
 
# User output model (excludes password)
class UserResponse(BaseModel):
    id: PyObjectId = Field(alias="_id")
    username: str
    email: EmailStr

    class Config:
        allow_population_by_field_name = True