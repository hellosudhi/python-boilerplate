from typing import List
from fastapi import APIRouter
from ..service.user_service import UserService
from ..model.user_model import UserResponse,UserModel

user_root = APIRouter()

# Fetch all user
@user_root.get("/user", response_model=List[UserResponse])
async def find_all_users():
  return  await UserService.get_all_users()
# Fetch UserById
@user_root.get("/user/{id}", response_model=UserResponse) 
async def find_user_by_id(id:str):
  return await UserService.get_user_by_id(id)
# create new user
@user_root.post("/create", response_model=UserResponse)
async def create_user(user_doc:UserModel):
  return await UserService.create_user(user_doc)