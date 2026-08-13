from fastapi import FastAPI ,Depends
from routers import items
app = FastAPI()
def check_user():
    return "valid user"
@app.get("/")



def root(user=Depends(check_user)):
    return {"message": user}




app.include_router(
    items.router,
    prefix="/items",
)


