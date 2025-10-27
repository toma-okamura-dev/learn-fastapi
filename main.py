from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):  
    alexnet = "a"
    resnet = "b"
    lenet = "c"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    return {"model_name": model_name}
