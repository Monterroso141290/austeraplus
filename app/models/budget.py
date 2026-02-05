from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Budget(Base):
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="owned_budgets")

    members = relationship("BudgetMember", back_populates="budget", cascade="all, delete")

    expenses = relationship("Expense", back_populates="budget", cascade="all, delete")

    transactions = relationship(
    "Transaction",
    back_populates="budget",
    cascade="all, delete-orphan"
)

