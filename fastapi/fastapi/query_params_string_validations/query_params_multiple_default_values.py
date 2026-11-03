"""Query Parameters with Multiple Values with Default Values"""
from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
    """Read Items"""
    query_items = {"q": q}
    return query_items
