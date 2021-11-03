from fastapi import APIRouter, Query
from controller import user
from controller.request import User

router = APIRouter()

@router.get("/users")
async def userList(page: int = Query(None, gt=0)):
    return user.getUsers(page)

@router.get("/user/{userId}")
async def getUser(userId:int):
    return user.getUser(userId)

@router.delete("/user/{userId}")
async def deleteUser(userId:int):
    return user.deleteUser(userId)

@router.post("/user")
async def postUser(user:User):
    return user.postUser(user)

@router.put("/user")
async def putUser(user:User):
    return user.putUser(user)