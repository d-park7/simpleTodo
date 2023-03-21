from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from ..database import get_db
from ..schemas import Todo


router = APIRouter()

@router.get("/todos/{todo_id}/todos/", response_model=Todo)
def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    return db.query(Todo).filter(Todo.id == todo_id).first()


@router.post("/todos/", response_model=Todo)
def create_todo(todo: Todo, db: Session = Depends(get_db)):
    todo = Todo(todo=todo.todo)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo