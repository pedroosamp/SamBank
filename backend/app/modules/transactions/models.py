from uuid import uuid4
from app.core.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric, DateTime
from datetime import datetime, timezone

class Transactions(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    transaction_number = Column(String, nullable=False, index=True, unique=True, default=lambda: str(uuid4()))
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Numeric(18, 2), nullable=False)
    currency = Column(String(3), nullable=False)
    description = Column(String)
    status = Column(String, nullable=False)
    created_at = Column(Date, default=timezone.utc, nullable=False)
    completed_at = Column(DateTime, nullable=False)
