from repository import repo_user
from repository.database import sessionScope
from fastapi.encoders import jsonable_encoder

from controller.base import ResponseBase
from controller.request import User

def getUsers(page:int=0, page_size:int=25):
    response = ResponseBase
    with sessionScope() as db:
        userList = repo_user.getUsers(page, page_size, db)
        if not userList is None:
            response["data"] = jsonable_encoder(userList)
        else :
            response["message"] = "data not exists"
    return response

def getUser(userId:int):
    response = ResponseBase
    with sessionScope() as db:
        user = repo_user.getUser(userId, db)
        if not user is None:
            response["data"] = jsonable_encoder(user)
        else :
            response["message"] = "data not exists"
    return response

def postUser(user:User):
    response = ResponseBase
    with sessionScope() as db:
        result = repo_user.postUser(user.toModel(), db)
        if result :
            response["data"] = jsonable_encoder(user)
        else :
            response["message"] = "could not post"
    return response

def deleteUser(userId:int):
    response = ResponseBase
    with sessionScope() as db:
        result = repo_user.deleteUser(userId, db)
        if result :
            response["data"] = None
        else :
            response["message"] = "could not delete"
    return response

def putUser(user:User):
    response = ResponseBase
    with sessionScope() as db:
        result = repo_user.putUser(user.toModel(), db)
        if result :
            response["data"] = jsonable_encoder(user)
        else :
            response["message"] = "could not update"
    return response