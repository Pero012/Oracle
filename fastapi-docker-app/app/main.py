from fastapi import FastAPI
from app.database import init_db
from app.routers import user

app = FastAPI()

# Inicijaliziraj bazu podataka
init_db()

# Uključi rute iz modula user
app.include_router(user.router, prefix="/api", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
