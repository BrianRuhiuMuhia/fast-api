from fastapi import APIRouter,status
from models.models import Book
from db.db import Session
userRouter=APIRouter()
@userRouter.get("/books")
async  def get_books():
    session=Session()
    books = session.query(Book).all()
    return {"books":books}
    
