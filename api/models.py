from sqlalchemy import Column, String, Integer, Boolean, ForeignKey 
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    email = Column(String, index=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
    
    todos = relationship("Todo", back_populates="user")
    
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    description = Column(String, index=True)
    
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="todos")