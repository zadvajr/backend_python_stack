"""Request body"""
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    """Item Model Class"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    """create item"""
    return item
