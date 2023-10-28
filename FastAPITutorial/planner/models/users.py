from pydantic import BaseModel, EmailStr
from typing import Optional, List
from models.events import Event


class User(BaseModel):
    """
    email: 사용자 이메일
    password: 사용자 패스워드
    events: 해당 사용자가 생성한 이벤트, 처음에는 비어있음
    """
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "username": "strong!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }
