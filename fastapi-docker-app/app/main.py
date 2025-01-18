from fastapi import FastAPI
from .database import init_db
from .routers import user

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(user.router, prefix="/api", tags=["users"])
