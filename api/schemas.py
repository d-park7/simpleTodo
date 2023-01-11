from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class BaseTodo(BaseModel):
    todo: str
    

class Todo(BaseTodo):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True
    

class TodoCreate(BaseTodo):
    pass


class UserBase(BaseModel):
    username: str


class User(UserBase):
    id: int
    is_active: bool
    todos: list[Todo] = []
    
    class Config:
        orm_mode = True


class UserInDB(UserBase):
    password: str
    

class UserCreate(UserBase):
    password: str