from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()


def create_todo(db: Session, todo: schemas.TodoCreate):
    todo = models.Todo(todo=todo.todo)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Todo).offset(skip).limit(limit).all()


def create_todo_for_user(db: Session, todo: schemas.TodoCreate, user_id: int):
    todo = models.Owns(id=todo.id, user_id=user_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo