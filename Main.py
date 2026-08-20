import sys
sys.path.append("Router2.0")

from fastapi import FastAPI

import users
import jobs


app = FastAPI()

app.include_router(users.router)
app.include_router(jobs.router)