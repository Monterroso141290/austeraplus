from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str
    description: Optional[str] = None
    budget_id: Optional[int] = None


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseRead(ExpenseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # REQUIRED for SQLAlchemy
