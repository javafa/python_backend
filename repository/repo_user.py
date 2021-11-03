from sqlalchemy.sql.sqltypes import Integer
from repository import models
from sqlalchemy.orm import Session
from typing import List

# user ######################################################
def getUsers(page:int, page_size:int, db: Session):
    if page is None :
        page = 0
    else :
        page = page - 1
    
    table = models.User
    query = db.query(table)
    # query = query.filter(table.user_hash == user_hash) // 차 후 필터 적용 필요
    return query.limit(page_size).offset(page*page_size).all()

def getUser(userId:int, db: Session) :
    table = models.User
    query = db.query(table)
    query = query.filter(table.id == userId)
    return query.first()

def deleteUser(userId:int, db: Session):
    table = models.User
    user = db.query(table).filter(table.id == userId).first()
    if not user is None :
        db.delete(user)
        return True
    else :
        return False

def postUser(user:models.User, db: Session):
    db.add(user)
    db.flush()
    return user

def putUser(user:models.User, db: Session):
    table = models.User
    entity = db.query(table).filter(table.id == user.id).first()
    if not entity is None :
        entity.email = user.email
        entity.name = user.name
        entity.age = user.age
        entity.gender = user.gender
        entity.address = user.address
        entity.tel = user.tel
        return True
    else :
        return False
