from app.core.database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)

    phone_number = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    national_id = Column(String, unique=True, nullable=False)

    # Relationships
    accounts = relationship("Accounts", back_populates="user", cascade="all, delete-orphan")
