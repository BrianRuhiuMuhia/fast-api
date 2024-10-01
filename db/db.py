from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from env import settings

# DB_HOST = settings.DB_HOST
# DB_NAME = settings.DB_NAME
# DB_USER = settings.DB_USER
# DB_PASSWORD = settings.DB_USER
DB_HOST:str = 'localhost'
DB_NAME:str = 'book-store'
DB_USER:str = 'postgres'
DB_PASSWORD:int = "7504"

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')


Session = sessionmaker(bind=engine)


Base = declarative_base()