from fastapi import FastAPI
app=FastAPI()
from router.book_router import bookRouter
from router.user_router import userRouter
from router.auth_router import authRouter
app.include_router(bookRouter)
app.include_router(userRouter)
app.include_router(authRouter)
    