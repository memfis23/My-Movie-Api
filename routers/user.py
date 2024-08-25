from fastapi import APIRouter
from pydantic import BaseModel
from utils.jwt_manajer import create_token
from fastapi.responses import JSONResponse
from schemas.user import User

user_router = APIRouter()

@user_router.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token:str = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)