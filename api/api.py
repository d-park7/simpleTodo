from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas, auth
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency that creates a new SessionLocal that will be used in a single request
# will automatically close once request is finished
# https://fastapi.tiangolo.com/tutorial/sql-databases/#create-a-dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)): 
    user_form = auth.get_user(db, form_data.username)
    if not user_form:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    user = schemas.UserInDB(id=user_form.id, username=user_form.username, password=user_form.password)
    hased_password = form_data.password
    if not hased_password == user.password:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_user)):
    return current_user

@app.get("/users/{username}", response_model=schemas.User)
def get_user(username: str, db: Session = Depends(get_db)):  
    db_user = crud.get_user(db, username=username)
    if username is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user 

@app.post("/todos/", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, todo=todo)

@app.post("/users/{user_id}/todos/", response_model=schemas.Todo)
def create_todo_for_user(user_id: int, todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo_for_user(db=db, todo=todo, user_id=user_id)

@app.get("/todos/{todo_id}", response_model=schemas.Todo)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db, todo_id=todo_id)
    if todo_id is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# TODO: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/?h=oauth2passwordrequestform#oauth2passwordrequestform