from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, nullable=False)

    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=False)

    budget = relationship("Budget")
    expenses = relationship("Expense", back_populates="category")