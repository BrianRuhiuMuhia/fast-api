from fastapi import FastAPI
app=FastAPI()
from router.router import userRouter
app.include_router(userRouter)
    