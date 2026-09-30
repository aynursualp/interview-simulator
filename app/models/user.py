from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import List

class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    email: str
    password_hash: str
    registration_date: datetime

    sessions: List["Session"] = Relationship(back_populates="user")