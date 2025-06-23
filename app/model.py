import uuid
from sqlalchemy import TIMESTAMP, Boolean, Column, String, text
from app.database import Base
from sqlalchemy.dialects.postgresql import UUID  # nếu bạn dùng PostgreSQL


class BaseModel:
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, nullable=False, default=uuid.uuid4)
    
class Task(Base, BaseModel):
    __tablename__= "task"
    
    name = Column(String, nullable=False)
    create_at = Column(TIMESTAMP(timezone=True),
                       nullable=False, server_default=text('now()'))
    is_completed = Column(Boolean, default=False)