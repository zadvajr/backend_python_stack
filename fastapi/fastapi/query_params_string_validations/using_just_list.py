"""You can define multiple values and default values with just list and not list[str]"""
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list, Query()] = []):
    """Read Items"""
    query_items = {"q": q}
    return query_items
