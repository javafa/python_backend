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
async def postUser(item:User):
    return user.postUser(item)

@router.put("/user")
async def putUser(item:User):
    return user.putUser(item)
