from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.core.database import Base
from app.modules.users.models import Users
from fastapi.testclient import TestClient
from app.core.auth import bcrypt_context
from app.main import app
from datetime import date
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"first_name": "John", "last_name": "Doe", "email": "test_email@email.com",
            "birthday": date.fromisoformat("2000-01-01"), "phone_number": "5512345678910", "national_id": "12345678910"}

client = TestClient(app)

@pytest.fixture
def test_user():
    user = Users(
        first_name="John",
        last_name="Doe",
        birthday=date.fromisoformat("2000-01-01"),
        phone_number="5512345678910",
        email="test_email@email.com",
        hashed_password=bcrypt_context.hash("test_password"),
        national_id="12345678910",
    )
    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with db.connection() as connection:
        connection.execute(text("DELETE FROM users;"))
        connection.commit()
