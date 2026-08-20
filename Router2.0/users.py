from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import crud
from database import get_db
from schemas import UserCreate, UserResponse


router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(
        db,
        user.email,
        user.password
    )


@router.get("/users", response_model=UserResponse)
def get_user(email: str, db: Session = Depends(get_db)):
    return crud.get_user_by_email(db, email)