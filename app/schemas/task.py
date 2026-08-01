from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import PriorityLevel

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: PriorityLevel = PriorityLevel.medium
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
    priority: Optional[PriorityLevel] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed : bool
    priority: PriorityLevel
    due_date: Optional[datetime]
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True
        