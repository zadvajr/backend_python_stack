"""Predefined path parameters"""
from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    """Model Class"""
    ALEXNET = "alexnet"
    RESNET = "resnet"
    LENET = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """get model names"""
    if model_name is ModelName.ALEXNET:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name is ModelName.LENET:
        return {"model_name": model_name, "message": "LeCNN all the images!"}
    return {"model_name": model_name, "message": "Have some residuals!"}
