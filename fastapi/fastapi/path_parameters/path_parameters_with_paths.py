"""Path parameters containing paths"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """read file path"""
    return {"file_path": file_path}
