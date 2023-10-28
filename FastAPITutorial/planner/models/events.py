from sqlmodel import JSON, SQLModel, Field, Column
from typing import Optional, List


class Event(SQLModel, table=True):
    """
    id: 자동 생성 되는 고유 식별자
    title: 이벤트 타이틀
    image: 이벤트 이미지 배너의 링크
    description: 이벤트 설명
    tags: 그룹화를 위한 이벤트 태그
    location: 이벤트 위치
    """

    id: int = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": ("We will be discussing the contents of the \
                FastAPI book in this event. Ensure to com with your own copy \
                to win gifts!"),
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }


class EventUpdate(SQLModel):
    title: Optional[str] = ""
    image: Optional[str] = ""
    description: Optional[str] = ""
    tags: Optional[List[str]] = []
    location: Optional[str] = ""

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": ("We will be discussing the contents of the \
                                FastAPI  book in this event. Ensure to come \
                                with your own copy to win gifts!"),
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet",
            }
        }
