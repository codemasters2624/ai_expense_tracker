from pydantic import BaseModel, EmailStr

class CreateUserRequest(BaseModel):
    name: str
    email: EmailStr

class CreateUserResponse(BaseModel):
    name: str
    user_id: int