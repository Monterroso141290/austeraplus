from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.expense import Expense, ExpenseCreate
from app.crud.expense import ( get_expenses, create_expense, get_expense_by_id, delete_expense)

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

#Get all the /expenses
@router.get("/", response_model=list[Expense])
def read_expenses(db: Session = Depends(get_db)):
    return get_expenses(db)

#Postr the /expenses
@router.post("/", response_model=Expense)
def create_new_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense(db, expense)

#Get /expense/{id}
@router.get("/{expense_id}", response_model=Expense)
def read_expense(expense_id: int, db: Session = Depends(get_db)):
    db_expense = get_expense_by_id(db, expense_id)

    if not db_expense:
        raise HTTPException(status_code=404, detail="Get your ID right dawg")

    return db_expense

#Delete expenses by ID /expenses/{id}
@router.delete("/{expense_id}")
def remove_expense(expense_id: int, db: Session = Depends(get_db)):
    deleted = delete_expense(db, expense_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="You cannot delete what does not exists, man")

    return {"message": "Expense deleted successfully"}