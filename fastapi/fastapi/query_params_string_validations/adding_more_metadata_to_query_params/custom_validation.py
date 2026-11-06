"""Custom Validation"""
import random
from typing import Annotated

from pydantic import AfterValidator
from fastapi import FastAPI

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}

def check_valid_id(item_id: str):
    """Checks Valid ID"""
    if not item_id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format it must start with "isbn-" or "imdb-"')
    return item_id

@app.get("/items/")
async def read_items(item_id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    """Read Items"""
    if item_id:
        item = data.get(item_id)
    else:
        item_id, item = random.choice(list(data.items()))
    return {"id": item_id, "name": item}
