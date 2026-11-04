"""Adding alias to query parameter"""
from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(item_query: Annotated[str | None, Query(alias="item-query")] = None):
    """Read Items"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if item_query:
        results.update({"item-query": item_query})
    return results
