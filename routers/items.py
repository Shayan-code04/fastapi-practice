from fastapi import APIRouter
router=APIRouter()
items = {
    1: {
        "name": "monitor",
        "price": 50000
    },
    2: {
        "name": "nothingIp2",
        "price": 20000
    }
}


@router.get("/")
def get_items():
    return items


@router.get("/{item_id}")
def get_item(item_id: int):
    return items[item_id]
