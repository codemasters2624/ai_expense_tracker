from fastapi import APIRouter, HTTPException, Depends
from schemas import users_schema

from sqlalchemy.orm import Session
from db.database import get_db
from db.models import User

router= APIRouter()

@router.get("/get-all-users")
def users(db: Session=Depends(get_db)):
    users_list = db.query(User).all()

    if not users_list:
        return {"message": "No users registered", "data": []}
    else:
        return {"data": users_list}
    pass

@router.post("/add-user")
def create_user(user: users_schema.CreateUserRequest, db=Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"data": new_user}
    # User
    

@router.get("/get-user/{user_id}")
def update_user(user_id: int, db: Session = Depends(get_db)):
    user = (
                db.query(User)
                .filter(User.id == user_id)
                .first()
                )
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {"user_details": user}