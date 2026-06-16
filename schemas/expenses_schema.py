from pydantic import BaseModel

class CreateGetExpensesRequest(BaseModel):
    user_id: int