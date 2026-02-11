from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)

    budget_id = Column(Integer, ForeignKey("budgets.id"))
    budget = relationship("Budget", back_populates="expenses")

    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    budget_id = Column(Integer, nullable=True)
    category_id = Column(Integer, nullable=True)
    user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
