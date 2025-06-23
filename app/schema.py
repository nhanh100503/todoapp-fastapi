from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    
    class config:
        from_attributes: True
        
class TaskUpdate(BaseModel):
    name: str
    
    class config:
        from_attributes: True
        
class TaskResponse(BaseModel):
    id: UUID
    name: str
    create_at: datetime
    is_completed: bool
    
    class config:
        from_attributes: True