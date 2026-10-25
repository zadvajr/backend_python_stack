"""Importance of order in creating path operations"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")
async def read_user_me():
    """return current user"""
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """return id of current user"""
    return {"user_id": user_id}
