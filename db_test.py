from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import get_db
from models import User

app = FastAPI()


@app.get("/test-db")
def test_database(db: Session = Depends(get_db)):
    return {
        "message": "Database session received successfully"
    }


@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return users



@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email=user.email,
        hashed_password=user.hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user