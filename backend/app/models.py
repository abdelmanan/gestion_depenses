from datetime import date

from pydantic import BaseModel, Field


class Expense(BaseModel):
    id: int | None = None
    description: str = Field(min_length=1, max_length=255)
    amount: float = Field(gt=0)
    category: str = Field(min_length=1, max_length=100)
    expense_date: date