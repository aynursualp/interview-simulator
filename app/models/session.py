from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from typing import List

class Session(SQLModel, table=True):
    session_id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="user.user_id")
    start_date: datetime
    end_date: datetime | None = None
    interview_type: str
    target_role: str
    score: float | None = None

    user: "User" = Relationship(back_populates="sessions")
    session_metrics: List["SessionMetric"] = Relationship(back_populates="session")