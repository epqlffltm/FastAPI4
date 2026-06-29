#user/interface/controllers/user_controller.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/user")

class CreateUserBody(BaseModel):
    name: str
    email: str
    password: str
    
@router.post("")
def create_user(user:CreateUserBody):
    return user
    
@router.post("", status_code=201)
def create_user():
    return "user created"
