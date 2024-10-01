from fastapi import APIRouter,Request,Response
from models.user_models import User,UserModel,UserSession
from db.db import Session
import bcrypt,secrets
authRouter=APIRouter()
registered_user_session={}
class UserSession:
    def __init__(self, user):
        self.user = user
@authRouter.post("/register")
async def register_func(user:UserModel,response:Response,request:Request):
    try:
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), salt)
        user.password=hashed_password.decode("utf-8")
        user_db=User(**user.dict())
        session=Session()
        session.add(user_db)
        session.commit()
        return {"message":"user registered"}
    except Exception as e:
        print(e)
        return {"message":"error registering user"}
@authRouter.post("/login")
@authRouter.post("/login")
async def login_func(user: UserModel, response: Response, request: Request):
    session = Session()
    try:
        user_db = session.query(User).filter_by(email=user.email).first()
        if user_db is not None:
            if user_db.name != user.name:
                return {"message": "invalid username or password"}
            hashed_password = user_db.password.encode("utf-8")
            if bcrypt.checkpw(user.password.encode("utf-8"), hashed_password):
                session_id = secrets.token_urlsafe(16)
                registered_user_session[session_id] = UserSession(user)
                response.set_cookie("session_id", session_id)
                return {"message": "successful login"}
            else:
                return {"message": "invalid username or password"}
        else:
            return {"message": "user not found"}
    except Exception as e:
        print(e)
        return {"message": "error logging in"}
        

@authRouter.post("/logout")
async def logout(request: Request,response:Response):
    session_id = request.cookies.get("session_id")
    if session_id in registered_user_session:
        del registered_user_session[session_id]
    response.delete_cookie("session_id")
    return {"message":"successsful logout"}