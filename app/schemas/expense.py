from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# We will define the fields that a "expense" will always need to have

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: str

#This schema will be used when the user SENDS new data to the API to create an expense,
#so basically, the data from ExpenseBase (title, amount and category)
class ExpenseCreate(ExpenseBase):
    amount: float
    description: Optional[str] = None
    budget_id: int
    category_id: Optional[int] = None

class ExpenseResponse(ExpenseBase):
    id: int
    amount: float
    description: Optional[str]
    budget_id: int
    category_id: Optional[int]
    user_id: int
    created_at: datetime

class Expense(ExpenseBase):
    id: int 
    created_at: str | None

    class Config:
        from_attributes = True

#What the user will send when he or she is registering
class UserCreate(BaseModel):
    email: EmailStr
    password: str

#Wha we will give back to the user. (We will never give back the password to the user)
class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        #We will allow population from objects (ORM)
        orm_mode = True