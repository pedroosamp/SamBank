import random
from app.core.database import Base
from sqlalchemy import String, Column, Integer, Numeric, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

class Accounts(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    account_number = Column(String, index=True, default=lambda: str(random.randint(100000000000, 999999999999)))
    name = Column(String, nullable=False)
    account_type = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    balance = Column(Numeric, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # Relationships
    user = relationship("Users", back_populates="accounts")
