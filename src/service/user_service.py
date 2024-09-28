
from ..config.db import user_collection
from ..model import user_model as Model
from bson import ObjectId

class UserService :

  @staticmethod
  async def get_all_users():
    users = []
    async for user in user_collection.find():
      users.append(Model.UserInDB(**user))
    return  users
  
  @staticmethod
  async def get_user_by_id(id:str) -> Model.UserInDB:
    return await user_collection.find_one({"_id":ObjectId(id)})
  
  @staticmethod
  async def create_user(user:Model.UserModel) ->  Model.UserInDB:
    return await user_collection.insert_one(user)
  
  @staticmethod
  async def get_user_by_id_and_update(id:str,user_doc:Model.UserModel) -> Model.UserInDB:
    _userValue = {key: value for key,value in user_doc.dict() if value is not None}
    result =  await user_collection.find_one_and_update({"_id": ObjectId(id)}, {
      "$set": _userValue
    })
    print("user service")
    print(result)
    return result;

  @staticmethod
  async def get_user_by_id_and_remove(id:str):
    return await user_collection.find_one_and_delete({"_id": ObjectId(id)})