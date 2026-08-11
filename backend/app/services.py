from typing import List

from .models import Expense
from .repositories import ExpenseRepository


class ExpenseService:

    def __init__(self):
        self.repository = ExpenseRepository()

    def create_expense(self, expense: Expense) -> int:
        return self.repository.create(expense)

    def get_all_expenses(self) -> List[Expense]:
        return self.repository.find_all()

    def delete_expense(self, expense_id: int) -> bool:
        return self.repository.delete(expense_id)

    def calculate_total(self) -> float:
        expenses = self.repository.find_all()

        return sum(expense.amount for expense in expenses)