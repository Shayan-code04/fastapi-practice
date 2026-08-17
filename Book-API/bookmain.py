from fastapi import FastAPI
from router.book import router
app = FastAPI()
app.include_router(router)
