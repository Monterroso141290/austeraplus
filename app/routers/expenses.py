from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_current_user
from app.models.user import User
from app.models.expense import Expense as ExpenseModel
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
def create_new_expense(expense: ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_expense = ExpenseModel(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        budget_id=expense.budget_id,
        category_id=expense.category_id,
        user_id=current_user.id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

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