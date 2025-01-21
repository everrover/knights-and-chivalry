from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def create_item(item: Union[str, int, float]):
    return {"item": item}

@app.get("/hello")
async def hello():
    return {"message": "Hello World"}