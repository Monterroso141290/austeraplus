from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class BudgetMember(Base):
    __tablename__ = "budget_members"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    budget_id = Column(Integer, ForeignKey("budgets.id"), nullable=False)

    # 🔗 RELATIONSHIPS
    user = relationship(
        "User",
        back_populates="budget_memberships"
    )

    budget = relationship(
        "Budget",
        back_populates="members"
    )
