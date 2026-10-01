from fastapi import APIRouter, status, HTTPException
from app.modules.users.schemas import CreateUserRequest, UpdateUserRequest, UserPasswordVerification, UserResponse
from app.modules.users.models import Users
from app.core.dependencies import db_dependency
from app.core.auth import bcrypt_context, user_dependency

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Devolve o usuário logado
@router.get("/me", status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated.")
    return user

# Cria um usuário
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(db: db_dependency, user_request: CreateUserRequest):
    user_model = user_request.model_dump()
    user_model["hashed_password"] = bcrypt_context.hash(user_model["password"])
    del user_model["password"]
    user_model = Users(**user_model)

    if db.query(Users).filter(Users.email == user_model.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is already registered.")

    try:
        db.add(user_model)
        db.commit()
        db.refresh(user_model)
    except Exception:
        db.rollback()
        raise
    return user_model

# Deleta o usuário logado
@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(db: db_dependency, user: user_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    try:
        db.delete(user)
        db.commit()
    except Exception:
        db.rollback()
        raise

# Atualiza os dados do usuário logado
@router.put("/me", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(db: db_dependency, user: user_dependency, user_request: UpdateUserRequest):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    if db.query(Users).filter(Users.email == user_request.email, Users.id != user.id).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is already registered.")

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

# Atualizar a senha do usuário logado
@router.patch("/me/password", status_code=status.HTTP_204_NO_CONTENT)
async def update_user_password(db: db_dependency, user: user_dependency, verification: UserPasswordVerification):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated.")
    if not bcrypt_context.verify(verification.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials.")
    if verification.password == verification.new_password:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, detail="The new password must be different from the current password.")
    user.hashed_password = bcrypt_context.hash(verification.new_password)
    try:
        db.commit()
    except Exception:
        db.rollback()
        raise
