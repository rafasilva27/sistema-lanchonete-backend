from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends

URL_DATABASE = 'postgresql://postgres:123@localhost:5432/Lanchonete'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Conectando com o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db # inicia a conexão
    finally:
        db.close() # encerra a conexão


db_dependency = Annotated[Session, Depends(get_db)]