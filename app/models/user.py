from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.common.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)  # Auto-generated UUID
    email = Column(String, unique=True, nullable=True)
    name = Column(String, nullable=True)
    microsoft_id = Column(String, unique=True, nullable=False)  # Microsoft ID column
