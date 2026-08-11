from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class item(BaseModel):
    name : str
    price: float



@app.get("/")
def home():
    return{"message":"hello world"}


@app.get("/item/{item_id}")
def get_item(item_id:id):
    return{"item_id":item_id}

@app.post("/item")
def create_item(item: item):
    return item     