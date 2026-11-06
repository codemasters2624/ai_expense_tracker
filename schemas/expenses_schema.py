from pydantic import BaseModel

class GetExpensesRequest(BaseModel):
    user_id: int

class CreateExpenseRequest(BaseModel):
    amount: int
    desc: str
    user_id: int