from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Item(BaseModel):
    name : str
    price: float
    avaliable:bool= True
    description:Optional[str]=None


@app.get("/")
def home():
    return {"message": "FastAPI is working"}



@app.get("/items")
def get_item(skip:int=0, limit:int =10):
    return { 
        "skip":skip,
        "limit":limit
           }

@app.post("/items")
def create_item(item: Item):
    return item     