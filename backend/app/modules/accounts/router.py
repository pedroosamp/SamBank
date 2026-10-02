from fastapi import APIRouter, status, HTTPException
from app.core.dependencies import db_dependency
from app.core.auth import user_dependency
from app.modules.accounts.models import Accounts
from app.modules.accounts.schemas import AccountResponse

router = APIRouter(
    prefix="/accounts",
    tags=["accounts"]
)

# Devolve todas as contas do usuário
@router.get("/me", status_code=status.HTTP_200_OK)
async def get_all_user_accounts(user: user_dependency, db: db_dependency):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated.")
    accounts = db.query(Accounts).filter(Accounts.user_id == user.get("id")).all()
    return accounts
