"""Request body + Path Parameters"""
from pydantic import BaseModel
from fastapi import FastAPI

class Item(BaseModel):
    """Item class model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """update item"""
    return {"item_id": item_id, **item.model_dump()}
