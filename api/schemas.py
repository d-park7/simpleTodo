from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class Todo(BaseModel):
    id: int
    todo: str
    
    class Config:
        orm_mode = True

# not sure why they do this in the docs
# ig mostly for keeping the same convention
# of separating the base from the methods?
class TodoCreate(Todo):
    pass

class Owns(BaseModel):
    id: int
    user_id: int

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True

class UserInDB(User):
    password: str
    
class UserCreate(User):
    password: str
 