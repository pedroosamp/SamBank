from app.tests.utils import *
from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.modules.accounts.models import Accounts
from app.modules.users.models import Users
from app.main import app
from fastapi import status
from datetime import date

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_get_user(test_user):
    response = client.get("/users/me")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["first_name"] == "John"
    assert response.json()["last_name"] == "Doe"
    assert response.json()["birthday"] == "2000-01-01"
    assert response.json()["email"] == "test_email@email.com"
    assert response.json()["phone_number"] == "5512345678910"
    assert response.json()["national_id"] == "12345678910"

def test_create_user(test_user):
    db = TestingSessionLocal()
    response = client.post("/users", json={
        "first_name": "Test", "last_name": "User", "email": "test_creation@email.com",
        "birthday": "1900-09-09", "phone_number": "12312312312",
        "national_id": "12312312311", "password": "passwordtest123",
    })
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["first_name"] == "Test"
    assert response.json()["last_name"] == "User"
    assert response.json()["birthday"] == "1900-09-09"
    assert response.json()["email"] == "test_creation@email.com"
    assert response.json()["phone_number"] == "12312312312"
    assert response.json()["national_id"] == "12312312311"

    user = db.query(Users).filter(Users.email == "test_creation@email.com").first()
    accounts = db.query(Accounts).filter(Accounts.user_id == user.id).all()
    assert len(accounts) == 2
    assert {account.account_type for account in accounts} == {"checking", "savings"}

def test_create_user_email_exists(test_user):
    response = client.post("/users", json={
        "first_name": "Test", "last_name": "User", "email": "test_email@email.com",
        "birthday": "1900-09-09", "phone_number": "12312312312",
        "national_id": "12312312311", "password": "passwordtest123",
    })
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Email is already registered."}

def test_create_user_national_id_exists(test_user):
    response = client.post("/users", json={
        "first_name": "Test", "last_name": "User", "email": "test_creation@email.com",
        "birthday": "1900-09-09", "phone_number": "12312312312",
        "national_id": "12345678910", "password": "passwordtest123",
    })
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "National ID is already registered."}

def test_create_user_phone_number_exists(test_user):
    response = client.post("/users", json={
        "first_name": "Test", "last_name": "User", "email": "test_creation@email.com",
        "birthday": "1900-09-09", "phone_number": "5512345678910",
        "national_id": "12312312311", "password": "passwordtest123",
    })
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Phone number is already registered."}

def test_delete_user(test_user):
    response = client.delete("/users/me")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    db = TestingSessionLocal()
    model = db.query(Users).filter(Users.id == 1).first()
    assert model is None

def test_update_user(test_user):
    response = client.put("/users/me", json={
        "first_name": "Updated", "last_name": "User", "email": "updated_email@email.com",
        "birthday": "2010-05-12", "phone_number": "5511333333333",
        "national_id": "99999999999",
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert test_user.first_name == "Updated"
    assert test_user.last_name == "User"
    assert test_user.email == "updated_email@email.com"
    assert test_user.birthday == date.fromisoformat("2010-05-12")
    assert test_user.phone_number == "5511333333333"
    assert test_user.national_id == "99999999999"

def test_update_user_email_exists(test_user, test_second_user):
    response = client.put("/users/me", json={
        "first_name": "Updated", "last_name": "User", "email": "test_email2@email.com",
        "birthday": "2010-05-12", "phone_number": "5511333333333",
        "national_id": "99999999999",
    })
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Email is already registered."}

def test_update_user_national_id_exists(test_user, test_second_user):
    response = client.put("/users/me", json={
        "first_name": "Updated", "last_name": "User", "email": "updated_email@email.com",
        "birthday": "2010-05-12", "phone_number": "5511333333333",
        "national_id": "23456789102",
    })
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "National ID is already registered."}

def test_update_user_phone_number_exists(test_user, test_second_user):
    response = client.put("/users/me", json={
        "first_name": "Updated", "last_name": "User", "email": "updated_email@email.com",
        "birthday": "2010-05-12", "phone_number": "5534567890123",
        "national_id": "99999999999",
    })
    assert response.status_code == status.HTTP_409_CONFLICT
    assert response.json() == {"detail": "Phone number is already registered."}

def test_update_user_password(test_user):
    response = client.patch("/users/me/password", json={
        "password": "test_password",
        "new_password": "updated_password",
    })
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert bcrypt_context.verify("updated_password", test_user.hashed_password) is True
