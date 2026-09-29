from fastapi import FastAPI
from app.modules.users.router import router as users_router
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)

@app.get("/")
async def index():
    return {"detail": "index"}
