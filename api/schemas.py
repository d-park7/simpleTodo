from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None


class TodoBase(BaseModel):
    description: str


class Todo(TodoBase):
    id: int
    user_id: int
    
    class Config:
        orm_mode = True

class TodoCreate(TodoBase):
    pass


class User(BaseModel):
    id: int
    email: str
    disabled: bool 
    todos: list[Todo] = []
    
    class Config:
        orm_mode = True

class UserInDB(User):
    hashed_password: str