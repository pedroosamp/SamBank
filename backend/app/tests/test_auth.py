from app.tests.utils import *
from app.core.auth import authenticate_user, create_access_token, SECRET_KEY, ALGORITHM, get_current_user
from datetime import timedelta
from jose import jwt
from fastapi import HTTPException, status
import pytest
import asyncio

def test_authenticate_user(test_user):
    db = TestingSessionLocal()
    authenticated_user = authenticate_user(test_user.email, "test_password", db)
    assert authenticated_user.email == test_user.email

    non_existent_user = authenticate_user("wrong_user@email.com", "test_password", db)
    assert non_existent_user is False

    wrong_password_user = authenticate_user(test_user.email, "1234", db)
    assert wrong_password_user is False

    db.close()

def test_create_access_token():
    email = "test_user@email.com"
    user_id = 1
    expires_delta = timedelta(days=1)

    token = create_access_token(email, user_id, expires_delta)
    decoded_token = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM], options={"verify_signature": False})
    assert decoded_token["sub"] == "test_user@email.com"
    assert decoded_token["id"] == 1

@pytest.mark.asyncio
async def test_get_current_user_valid_token():
    encode = {"sub": "test_email@email.com", "id": 1}
    token = jwt.encode(encode, key=SECRET_KEY, algorithm=ALGORITHM)
    user = await get_current_user(token=token)
    assert user == {"email": "test_email@email.com", "id": 1}

@pytest.mark.asyncio
async def test_get_current_user_missing_payload():
    encode = {"id": 1}
    token = jwt.encode(encode, key=SECRET_KEY, algorithm=ALGORITHM)

    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(token=token)
    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == 'Could not validate user.'
