from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.budget import Budget
from app.models.budget_member import BudgetMember
from app.models.user import User
from app.dependencies import get_current_user

def verify_budget_access(
    budget_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    budget = db.query(Budget).filter(Budget.id == budget_id).first()

    if not budget:
        raise HTTPException(status_code=404, detail="Budget not found")

    #Owner check
    if budget.owner_id == curren_user.id:
        return budget

    #Membership check
    member = (
        db.query(BudgetMember)
        .filter(
            BudgetMember.budget_id == budget_id,
            BudgetMember.user_id == current_user.id,
        )
        .first()
    )

    if not member:
        raise HTTPException(status_code=403, detail="Access denied")

    return budget