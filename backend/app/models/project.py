from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="projects")
    claude_docs = relationship("ClaudeDoc", back_populates="project", cascade="all, delete-orphan")
    initial_docs = relationship("InitialDoc", back_populates="project", cascade="all, delete-orphan")
    prp_docs = relationship("PRPDoc", back_populates="project", cascade="all, delete-orphan")