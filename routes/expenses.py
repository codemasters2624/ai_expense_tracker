from fastapi import APIRouter, HTTPException, Depends
from schemas import expenses_schema
from datetime import datetime

from db.models import Expense
from db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import and_

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.get("/all-expense")
def get_all_expenses(user_id: int, db: Session = Depends(get_db)):
    print(f"Fetching all expenses against {user_id}")
    expenses = db.query(Expense).filter(Expense.user_id == user_id).all()
    if not expenses:
        raise HTTPException(
            status_code=404, detail="No expenses found against provided user_id"
        )

    return {"message": "All expenses fetched successfully", "data": expenses}


@router.post("/add-expense")
def add_expense(
    expense: expenses_schema.CreateExpenseRequest, db: Session = Depends(get_db)
):

    current_date = datetime.today()
    print("Expense Obj passing", expense)
    new_expense = Expense(
        amount=expense.amount,
        desc=expense.desc,
        user_id=expense.user_id,
        expense_date=current_date
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return {"data": new_expense}


@router.delete("/delete-expense")
def delete_expense(user_id: int, expense_id: int, db: Session = Depends(get_db)):
    print(f"Deleting expense with id {expense_id} against user_id {user_id}")
    expense = (
        db.query(Expense)
        .filter(and_(Expense.id == expense_id, Expense.user_id == user_id))
        .first()
    )
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    db.delete(expense)
    db.commit()

    return {"msg": f"Expense deleted against ID: {expense_id}"}
