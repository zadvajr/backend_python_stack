"""Path Parameters and Numeric Validations"""
from typing import Annotated
from fastapi import FastAPI, Query, Path

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the Item to get")],
    q: Annotated[str | None, Query(alias="item-query")] = None
):
    """Read Items"""
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
