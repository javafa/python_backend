from pydantic import BaseModel, Field
from typing import Optional

from repository import models

class User(BaseModel):
    id : int                = Field(None, description="POST 에는 사용하지 않는다")
    email : str             = Field(min_length=5, max_length=255, description="이메일")
    name : str              = Field(min_length=2, max_length=5, description="이름 5자 이하")
    age : Optional[int]     = Field(None, gt=0, lt=150, description="나이")
    gender : Optional[str]  = Field(None, min_length=1, max_length=1, description="성별 M/F")
    address : Optional[str] = Field(None, min_length=5, max_length=200, description="주소")
    tel : Optional[str]     = Field(None, min_length=7, max_length=11, description="전화번호 : - 를 빼고 입력")

    def toModel(self) :
        model = models.User()
        model.id = self.id
        model.email = self.email
        model.name = self.name
        model.age = self.age
        model.gender = self.gender
        model.address = self.address
        model.tel = self.tel
        return model

