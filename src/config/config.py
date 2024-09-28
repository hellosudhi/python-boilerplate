import os
from dotenv import load_dotenv

ENV = os.getenv("APP_ENV","development")

if ENV == "production":
  load_dotenv(".env.production")
else:
  load_dotenv(".env.local")

DEBUG = os.getenv("DEBUG","False") == "True"

DATABAS_URL = os.getenv("DATABASE_URL")