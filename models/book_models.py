from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    isbn = Column(String)
    page_count = Column(String)
    image = Column(String)
    short_description = Column(String)
    long_description = Column(String)
class BookModel(BaseModel):
    id: int
    title: str
    isbn: str
    page_count: int
    image: str
    short_description: str
    long_description: str
    


  
