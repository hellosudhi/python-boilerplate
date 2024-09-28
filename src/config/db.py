import motor.motor_asyncio
from .config import DATABAS_URL
import logging

# Logging
logger = logging.getLogger(__name__)

# Intialize connections 
try:
  # Establishing the connection
  _client = motor.motor_asyncio.AsyncIOMotorClient(DATABAS_URL)
  db = _client.Cluster0
  logger.info("Mongo DB Connected")
except Exception as ex:
  logger.error(f"Error conneting to Mongo:{ex}")
  raise ConnectionError(f"Failed to connect: {ex}")

# Collections
user_collection = db.get_collection("users")



