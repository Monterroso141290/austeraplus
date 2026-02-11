from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    # 🔑 FOREIGN KEYS (THIS IS THE FIX)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    # 🔗 RELATIONSHIPS
    category = relationship("Category", back_populates="expenses")
    budget = relationship("Budget", back_populates="expenses")
