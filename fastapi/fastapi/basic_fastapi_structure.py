from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """root function"""
    return {"message": "Hello World"}