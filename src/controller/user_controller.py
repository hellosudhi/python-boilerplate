from typing import List
from fastapi import APIRouter
from ..service.user_service import UserService
from ..model.user_model import UserInDB
router = APIRouter()


@router.get("/user", response_model=List[UserInDB])
async def find_all_users():
  return  await UserService.get_all_users()