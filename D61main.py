from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float


items = {
    1: {
        "name": "Laptop",
        "price": 50000
    },
    2: {
        "name": "Phone",
        "price": 20000
    }
}


@app.get("/items", response_model=list[Item])
def get_items():
    return list(items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):

    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    return items[item_id]


@app.post(
    "/items",
    response_model=Item,
    status_code=status.HTTP_201_CREATED
)
def create_item(item: Item):

    new_id = max(items.keys()) + 1

    items[new_id] = item.model_dump()

    return items[new_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):

    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    items[item_id] = item.model_dump()

    return items[item_id]


@app.delete("/items/{item_id}")
def delete_item(item_id: int):

    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )

    del items[item_id]

    return {
        "message": "Item deleted successfully"
    }