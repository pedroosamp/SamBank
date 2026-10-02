from fastapi import APIRouter, status, HTTPException
from app.core.dependencies import db_dependency
from app.core.auth import user_dependency
from app.modules.accounts.models import Accounts
from app.modules.accounts.schemas import CreateAccountRequest, AccountResponse

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

# Cria uma nova conta bancária
@router.post("/me", status_code=status.HTTP_201_CREATED, response_model=AccountResponse)
async def create_user_account(user: user_dependency, db: db_dependency, accounts_request: CreateAccountRequest):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated.")
    account_model = accounts_request.model_dump()
    account_model["user_id"] = user.get("id")
    account_model["currency"] = "BRL"
    account_model["balance"] = 0
    account_model = Accounts(**account_model)

    try:
        db.add(account_model)
        db.commit()
        db.refresh(account_model)
    except Exception:
        db.rollback()
        raise
    return account_model
