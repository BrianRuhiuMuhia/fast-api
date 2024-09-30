from fastapi import FastAPI
app=FastAPI()
from router.book_router import bookRouter
from router.user_router import userRouter
app.include_router(bookRouter)
app.include_router(userRouter)
    