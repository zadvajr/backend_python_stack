"""Path parameters with types"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(item_id: int):
    """defines path with types"""
    return {"item_id": item_id}
