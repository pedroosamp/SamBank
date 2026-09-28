from app.core.database import Base
from sqlalchemy import Column, Integer, String

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(String)

    phone_number = Column(String)
    email = Column(String)
    hashed_password = Column(String)

    national_id = Column(String)
