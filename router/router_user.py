from fastapi import APIRouter, Query
from controller import user
from controller.request import User

router = APIRouter()

@router.get("/list")
async def get_user_list(page: int = Query(None, gt=0)):
    return user.getUsers(page)

@router.get("/{userId}")
async def get_user(userId:int):
    return user.getUser(userId)

@router.delete("/{userId}")
async def delete_user(userId:int):
    return user.deleteUser(userId)

@router.post("")
async def post_user(item:User):
    return user.postUser(item)

@router.put("")
async def put_user(item:User):
    return user.putUser(item)
