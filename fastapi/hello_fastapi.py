"""Hello FastAPI"""
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    """index"""
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("hello_fastapi:app", host="127.0.0.1", port=8000, reload=True)
