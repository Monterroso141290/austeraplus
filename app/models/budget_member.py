from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base

class BudgetMember(Base):
    __tablename__ = "budget_members"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=False)

    role = Column(String, default="member")

    #Relationships
    user = relationship("User", back_populates="budget_members")
    budget = relationship("Budget", back_populates="members")