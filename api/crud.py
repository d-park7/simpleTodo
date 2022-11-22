from sqlalchemy.orm import Session

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    password = user.password
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_todo_by_id(db: Session, todo_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    todo = models.Todo(todo=todo.todo)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

def create_todo_for_user(db: Session, todo: schemas.TodoCreate, user_id: int):
    todo = models.Owns(id=todo.id, user_id=user_id)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo