from fastapi import APIRouter,status
userRouter=APIRouter()
from models.user_models import User,UserModel
from db.db import Session
@userRouter.get("/users")
async def get_all_users():
    session=Session()
    users=session.query(User).all()
    return users
@userRouter.get("/users/{id}")
async def get_single_user(id):
    session=Session()   
    user=session.query(User).filter(User.id==id).first()
    if user != None:
        return user
    else:
        return {"message":"user not found"}
@userRouter.delete("/users/{id}")
async def delete_user(id):
    session=Session()
    user = session.query(User).filter(User.id == id).first()
    if user != None:
        session.delete(user)
        session.commit()
        return {"message":"user deleted successfully"}
    else:
        return {"message":"user not found"}
@userRouter.put("/users/{id}")
async def update_user(id, user:UserModel):
    session=Session()
    user_to_update = session.query(User).filter(User.id == id).first()
    if user_to_update!=None:
        user_to_update=user
        return user
    else:
        return {"message":"user not found"}
    