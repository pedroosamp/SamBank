from pydantic import BaseModel
from enum import Enum

class AccountType(str, Enum):
    CHECKING = "checking"
    SAVINGS = "savings"

class CreateAccount(BaseModel):
    name: str
    account_type: AccountType
