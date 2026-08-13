from datetime import date

from app.models import Expense
from app.services import ExpenseService


def test_expense_model():
    expense = Expense(
        description="Déjeuner",
        amount=45.0,
        category="Alimentation",
        expense_date=date.today()
    )

    assert expense.description == "Déjeuner"
    assert expense.amount == 45.0
    assert expense.category == "Alimentation"


def test_create_expense():
    service = ExpenseService()

    expense = Expense(
        description="Transport",
        amount=20.0,
        category="Transport",
        expense_date=date.today()
    )

    expense_id = service.create_expense(expense)

    assert expense_id is not None


def test_get_all_expenses():
    service = ExpenseService()

    expenses = service.get_all_expenses()

    assert isinstance(expenses, list)


def test_calculate_total():
    service = ExpenseService()

    total = service.calculate_total()

    assert isinstance(total, float)


def test_delete_expense():
    service = ExpenseService()

    expense = Expense(
        description="Test suppression",
        amount=10.0,
        category="Test",
        expense_date=date.today()
    )

    expense_id = service.create_expense(expense)

    result = service.delete_expense(expense_id)

    assert result is True