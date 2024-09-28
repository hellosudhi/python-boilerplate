from fastapi import FastAPI
from src.controller import user_controller

app = FastAPI()


app.include_router(user_controller.router, prefix="/api", tags=["users"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
