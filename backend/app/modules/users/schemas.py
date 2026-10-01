from pydantic import BaseModel

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    birthday: str
    phone_number: str
    email: str
    national_id: str

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

class PasswordVerification(BaseModel):
    password: str
    new_password: str
