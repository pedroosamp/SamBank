from pydantic import BaseModel

class UserRequest(BaseModel):
    id: int
    first_name: str
    last_name: str
    birthday: str
    phone_number: str
    email: str
    hashed_password: str
    national_id: str
