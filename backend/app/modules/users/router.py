from fastapi import APIRouter, status, HTTPException
from app.modules.users.schemas import CreateUserRequest, UpdateUserRequest, PasswordVerification, UserResponse
from app.modules.users.models import Users
from app.core.dependencies import db_dependency
from app.core.auth import bcrypt_context, user_dependency

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Devolve o usuário logado
@router.get("/", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated.")
    return user

# Cria um usuário
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, user_request: CreateUserRequest):
    user_model = user_request.model_dump()
    user_model["hashed_password"] = bcrypt_context.hash(user_model["password"])
    del user_model["password"]
    user_model = Users(**user_model)

    try:
        db.add(user_model)
        db.commit()
    except Exception:
        db.rollback()
        raise

# Deleta o usuário logado
@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")
    try:
        db.delete(user)
        db.commit()
    except Exception:
        db.rollback()
        raise

# Atualiza os dados do usuário logado
@router.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db: db_dependency, user: user_dependency, user_request: UpdateUserRequest):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authorized")

    user.first_name = user_request.first_name
    user.last_name = user_request.last_name
    user.birthday = user_request.birthday
    user.phone_number = user_request.phone_number
    user.national_id = user_request.national_id
    user.email = user_request.email

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise
