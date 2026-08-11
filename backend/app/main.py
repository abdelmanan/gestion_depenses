from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .models import Expense
from .services import ExpenseService


app = FastAPI(
    title="Expense Tracker API",
    description="API simple de gestion des dépenses",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


service = ExpenseService()


@app.get("/")
def home():
    return {
        "message": "Expense Tracker API is running"
    }


@app.post("/expenses", status_code=201)
def create_expense(expense: Expense):

    expense_id = service.create_expense(expense)

    return {
        "id": expense_id,
        "message": "Expense created successfully"
    }


@app.get("/expenses")
def get_expenses():

    return service.get_all_expenses()


@app.get("/expenses/total")
def get_total():

    total = service.calculate_total()

    return {
        "total": total
    }


@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):

    deleted = service.delete_expense(expense_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {
        "message": "Expense deleted successfully"
    }