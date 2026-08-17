from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Book(BaseModel):
    title: str
    author: str
    price: float


books = {
    1: {
        "title": "Atomic Habits",
        "author": "James Clear",
        "price": 500
    },
    2: {
        "title": "Clean Code",
        "author": "Robert Martin",
        "price": 700
    }
}


@router.get("/books")
def get_books():
    return books


@router.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return books[book_id]


@router.post("/books", status_code=201)
def create_book(book: Book):
    new_id = max(books.keys()) + 1

    books[new_id] = book.model_dump()

    return books[new_id]


@router.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    books[book_id] = book.model_dump()

    return books[book_id]


@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    del books[book_id]
    