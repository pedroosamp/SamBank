from app.tests.utils import *
from app.core.auth import get_current_user
from app.core.dependencies import get_db
from app.main import app
from fastapi import status
from datetime import date

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_get_user():
    response = client.get("/users/me")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["first_name"] == "John"
    assert response.json()["last_name"] == "Doe"
    assert response.json()["birthday"] == "2000-01-01"
    assert response.json()["email"] == "test_email@email.com"
    assert response.json()["phone_number"] == "5512345678910"
    assert response.json()["national_id"] == "12345678910"
