from pydantic import BaseModel
from enum import Enum
from decimal import Decimal
from datetime import datetime

class AccountType(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"

class AccountResponse(BaseModel):
    id: int
    name: str
    account_type: AccountType
    user_id: int
    currency: str
    balance: Decimal
    created_at: datetime


class CreateAccountRequest(BaseModel):
    name: str
    account_type: AccountType
