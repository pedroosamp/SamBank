from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    phone_number: str
    email: str
    password: str
    national_id: str

class UpdateUserRequest(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    phone_number: str
    email: str
    national_id: str
