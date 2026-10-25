"""Query parameters: when you declare other function parameters -
 that are not part of path parameter, they are automatically interpreted as query parameters
 """
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 100):
    """read item"""
    return fake_items_db[skip:limit]
