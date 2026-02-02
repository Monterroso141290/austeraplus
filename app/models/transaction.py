from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    amount = Column(Float, nullable = False)
    description = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_by_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    budget = relationship("Budget", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")
    created_by = relationship("User")