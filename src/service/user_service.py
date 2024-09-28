from ..config.db import user_collection
from ..model import user_model as Model

class UserService :

  @staticmethod
  async def get_all_users():
    users = []
    async for user in user_collection.find():
      users.append(Model.UserInDB(**user))
    return  users