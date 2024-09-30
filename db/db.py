from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_HOST = 'localhost'
DB_NAME = 'book-store'
DB_USER = 'postgres'
DB_PASSWORD = '7504'

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')


Session = sessionmaker(bind=engine)


Base = declarative_base()