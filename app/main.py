from fastapi import FastAPI
app=FastAPI()
from router.book_router import bookRouter
app.include_router(bookRouter)
    