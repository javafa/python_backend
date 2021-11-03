from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    id : int                = Filed(None)
    email : str             = Field(min_length=5, max_length=255, description="이메일")
    name : str              = Field(min_length=2, max_length=5, description="이름 5자 이하")
    age : Optional[int]     = Field(None, gt=0, lt=150, description="나이")
    gender : Optional[str]  = Field(None, min_length=1, max_length=1, description="성별 M/F")
    address : Optional[str] = Field(None, min_length=5, max_length=200, description="주소")
    tel : Optional[str]     = Field(None, min_length=7, max_length=11, description="전화번호 : - 를 빼고 입력")
