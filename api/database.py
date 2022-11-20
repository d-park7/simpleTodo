from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Too lazy to hide this
POSTGRES_URL = "postgresql://david:admin@localhost:5432/todo"

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

if __name__ == "__main__":
    try:
        engine.connect()
        print("worked")
    except SQLAlchemyError as err:
        print(err.__cause__)
