from fastapi import APIRouter,status
from models.models import Book
from models.models import BookModel
from db.db import Session
bookRouter=APIRouter()
@bookRouter.get("/books")
async  def get_books():
    session=Session()
    books = session.query(Book).all()
    return {"books":books}
    
@bookRouter.get("/books/{id}")
async def get_single_book(id):
    session=Session()
    book = session.query(Book).filter(Book.id == id).first()
    if book!=None:
        return [book]
    else:
        return {"message":"book not found"}
@bookRouter.post("/books")
async def add_book(book:BookModel):
    session = Session()
    db_book = Book(**book.dict())  # Convert Pydantic model to SQLAlchemy model
    session.add(db_book)
    session.commit()
    return {"message":"book added"}
@bookRouter.delete("/books/{id}")
async def delete_book(id):
    session=Session()
    book = session.query(Book).filter(Book.id == id).first()
    if book:
        session.delete(book)
        session.commit()
        return {"message": "Book deleted"}
    else:
        return {"message": "Book not found"}
@bookRouter.patch("/books/{id}")
async def update_book(id,book:BookModel):
    session=Session()
    book_update = session.query(Book).filter(Book.id == id).first()
    if book_update:
        book_update=book
        session.commit()
        return {"message":f"book with id {id} updated"}
    else:
        return {"message":"book not found"}
