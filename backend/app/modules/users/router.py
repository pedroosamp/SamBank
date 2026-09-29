from fastapi import APIRouter, status, HTTPException
from app.modules.users.schemas import UserRequest
from app.modules.users.models import Users
from app.core.dependencies import db_dependency

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_users(db: db_dependency):
    users = db.query(Users).all()
    return users

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: UserRequest):
    user_model = Users(**user_request.model_dump())
    try:
        db.add(user_model)
        db.commit()
    except Exception:
        db.rollback()
        raise

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, user_id: int):
    user_model = db.query(Users).filter(Users.id == user_id).first()
    if not user_model:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    try:
        db.delete(user_model)
        db.commit()
    except Exception:
        db.rollback()
        raise
