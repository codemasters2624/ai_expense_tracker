from fastapi import APIRouter, HTTPException, Depends
from schemas import expenses_schema 

from db.models import Expense
from db.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.get('/all-expense')
def get_all_expenses(user_id: expenses_schema.CreateGetExpensesRequest, db: Session=Depends(get_db)):
    print(f"Fetching all expenses against {user_id}")
    expenses = (db.query(Expense).filter(Expense.user_id == user_id))
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found against provided user_id")
    
    return {"message": "All expenses fetched successfully", "data": expenses}
    