from typing import List

from .database import get_connection
from .models import Expense


class ExpenseRepository:

    def create(self, expense: Expense) -> int:
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                INSERT INTO expenses
                (description, amount, category, expense_date)
                VALUES (%s, %s, %s, %s)
            """

            values = (
                expense.description,
                expense.amount,
                expense.category,
                expense.expense_date
            )

            cursor.execute(query, values)
            connection.commit()

            return cursor.lastrowid

        finally:
            cursor.close()
            connection.close()

    def find_all(self) -> List[Expense]:
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                SELECT id, description, amount, category, expense_date
                FROM expenses
                ORDER BY expense_date DESC
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            return [
                Expense(
                    id=row[0],
                    description=row[1],
                    amount=float(row[2]),
                    category=row[3],
                    expense_date=row[4]
                )
                for row in rows
            ]

        finally:
            cursor.close()
            connection.close()

    def delete(self, expense_id: int) -> bool:
        connection = get_connection()
        cursor = connection.cursor()

        try:
            query = """
                DELETE FROM expenses
                WHERE id = %s
            """

            cursor.execute(query, (expense_id,))

            deleted = cursor.rowcount > 0

            connection.commit()

            return deleted

        finally:
            cursor.close()
            connection.close()