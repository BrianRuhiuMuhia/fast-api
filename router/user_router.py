from fastapi import APIRouter,status,Request,Response
userRouter=APIRouter()
from models.user_models import User
from db.db import Session
from .auth_router import registered_user_session
@userRouter.get("/users")
async def get_all_users(request:Request,response:Response):
    session=Session()
    session_id = request.cookies.get("session_id")
    if session_id in registered_user_session:
         users=session.query(User).all()
         return users
    else:
        return {"message":"You are not logged in"}
@userRouter.get("/users/{id}")
async def get_single_user(id,request:Request,response:Response):
    session=Session()   
    user=session.query(User).filter(User.id==id).first()
    if user != None:
          session_id = request.cookies.get("session_id")
          if session_id in registered_user_session:
                return user
          else:
              return {"message":"log in to access route"}
    else:
        return {"message":"user not found"}
