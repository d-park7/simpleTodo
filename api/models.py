from sqlalchemy import Column, String, Integer, Boolean, ForeignKey

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    password = Column(String)
    disabled = Column(Boolean)
    
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    todo = Column(String, index=True)

class Owns(Base):
    __tablename__ = "owns"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))