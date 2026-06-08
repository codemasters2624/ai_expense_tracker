from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    name: str

class CreateUserResponse(BaseModel):
    name: str
    user_id: int