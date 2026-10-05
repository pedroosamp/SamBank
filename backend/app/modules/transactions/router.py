from fastapi import APIRouter, status, HTTPException
from app.core.dependencies import db_dependency
from app.core.auth import user_dependency
from app.modules.transactions.models import Transactions


router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/me/{transaction_number}")
async def get_transaction(user: user_dependency, db: db_dependency, transaction_number: str):
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated.")
    transaction = db.query(Transactions).filter(Transactions.transaction_number == transaction_number)
    if not transaction:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Transaction not found.")
