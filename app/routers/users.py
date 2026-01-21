# APIRouter for user related endpoints and Depends for dependencies injections
from fastapi import APIRouter, Depends
from app.core.deps import get_current_user
from app.models.user import User

#Standard router configuration
router = APIRouter(prefix="/users", tags=["Users"])

#FASTAPI will see Depends(get_current_user) and will call it and execute it. If it fails, it will stop. If it returns, the route executes
@router.get("/me")
def read_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
    }