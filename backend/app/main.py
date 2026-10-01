from fastapi import FastAPI
from app.modules.users.router import router as users_router
from app.core.auth import router as auth_router
from app.core.database import Base, engine

app = FastAPI()

app.include_router(users_router)
app.include_router(auth_router)

@app.get("/")
async def index():
    return {"detail": "index"}
