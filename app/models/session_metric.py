from sqlmodel import Field, SQLModel, Relationship
from datetime import datetime
from sqlalchemy import Column, JSON

class SessionMetric(SQLModel, table=True):
    session_metric_id: int | None = Field(default=None, primary_key=True)
    session_id: int | None = Field(default=None, foreign_key="session.session_id")
    record_time: datetime
    metric_type: str
    metric_value: float
    
    detail: dict | None = Field(default=None, sa_column=Column(JSON))

    session: "Session" = Relationship(back_populates="session_metric")

    