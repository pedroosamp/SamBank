from fastapi import APIRouter, status
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
    db.add(user_model)
    db.commit()
