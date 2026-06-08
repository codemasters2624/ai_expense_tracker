from fastapi import APIRouter
from schemas import users_schema
from storage import storage

router= APIRouter()

@router.get("/get-users")
def users():
    return {"UsersList": storage.users_list}

@router.post("/add-user")
def create_user(user: users_schema.CreateUserRequest):
    storage.users_id
    new_user = {"name": user.name, "id": storage.users_id}
    storage.users_id += 1
    storage.users_list.append(new_user)
    return {"user": new_user}