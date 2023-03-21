from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str

    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str
    JWT_PRIVATE_KEY: str
    
    class Config:
        env_file = 'api/.env'
        
settings = Settings()