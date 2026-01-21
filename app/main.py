from fastapi import FastAPI
from app.database import engine, Base
from app.models.expense import Expense
from app.routers import expenses, auth

app = FastAPI(title ="AusteraPlus API")

Base.metadata.create_all(bind=engine)

app.include_router(expenses.router)
app.include_router(auth.router)

@app.get("/")

def root():
    return {"message": "AusteraPlus is running"}