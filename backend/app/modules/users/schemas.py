from pydantic import BaseModel, EmailStr, Field
from datetime import date

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    birthday: date
    phone_number: str
    email: EmailStr
    national_id: str

class CreateUserRequest(BaseModel):
    first_name: str = Field(min_length=4, max_length=100)
    last_name: str = Field(min_length=4, max_length=100)
    birthday: date
    phone_number: str = Field(min_length=4, max_length=15)
    email: EmailStr
    password: str
    national_id: str = Field(min_length=9, max_length=16)

class UpdateUserRequest(BaseModel):
    first_name: str = Field(min_length=4, max_length=100)
    last_name: str = Field(min_length=4, max_length=100)
    birthday: date
    phone_number: str = Field(min_length=4, max_length=15)
    email: EmailStr
    national_id: str = Field(min_length=9, max_length=16)

class UserPasswordVerification(BaseModel):
    password: str
    new_password: str
