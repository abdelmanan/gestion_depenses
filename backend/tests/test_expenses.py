from datetime import date

import pytest

from app.models import Expense
from app.services import ExpenseManager


def test_create_expense():
    expense = Expense(
        description="Déjeuner",
        amount=45.0,
        category="Alimentation",
        expense_date=date.today()
    )

    assert expense.description == "Déjeuner"
    assert expense.amount == 45.0
    assert expense.category == "Alimentation"


def test_add_expense():
    manager = ExpenseManager()

    expense = Expense(
        description="Transport",
        amount=20.0,
        category="Transport",
        expense_date=date.today()
    )

    manager.add_expense(expense)

    expenses = manager.get_expenses()

    assert len(expenses) == 1
    assert expenses[0].description == "Transport"


def test_total_expenses():
    manager = ExpenseManager()

    manager.add_expense(
        Expense(
            "Déjeuner",
            45.0,
            "Alimentation",
            date.today()
        )
    )

    manager.add_expense(
        Expense(
            "Transport",
            20.0,
            "Transport",
            date.today()
        )
    )

    assert manager.get_total() == 65.0


def test_delete_expense():
    manager = ExpenseManager()

    manager.add_expense(
        Expense(
            "Déjeuner",
            45.0,
            "Alimentation",
            date.today()
        )
    )

    manager.delete_expense(0)

    assert len(manager.get_expenses()) == 0


def test_delete_invalid_expense():
    manager = ExpenseManager()

    with pytest.raises(IndexError):
        manager.delete_expense(0)