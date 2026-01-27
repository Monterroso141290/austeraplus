from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable = False)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    budget_id = Column(Integer, ForeignKey("budgets.id"))
    category_id = Column(Integer, ForeignKey("categories.id"))
    created_by = Column(Integer, ForeignKey("users.id"))

    budget = relationship("Budget", back_populates="transactions")