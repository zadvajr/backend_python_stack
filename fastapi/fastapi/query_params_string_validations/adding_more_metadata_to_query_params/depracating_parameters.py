"""Deprecating Parameters"""
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(
        alias="item-query",
        title="Query Item",
        description="Query String for the Items to search in the database.",
        min_length=3,
        max_length=50,
        pattern="^fixedquery$",
        deprecated=True
    )] = None
):
    """Read items"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
