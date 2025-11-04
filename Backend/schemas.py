from pydantic import BaseModel
from datetime import datetime

#importing basemodel done------------------------------

class UserIntBase(BaseModel):
    username: str
    full_name: str
    email: str
    contact: str

class CreateUserInt(UserIntBase):
    password: str

class UserIntOut(UserIntBase):
    user_id: int

    class Config:
        orm_mode=True

class UserExtBase(BaseModel):
    username: str
    full_name: str
    email: str
    contact: str

class CreateUserExt(UserExtBase):
    password: str

class UserExtOut(UserExtBase):
    user_id: int

    class Config:
        orm_mode=True

class ContentBase(BaseModel):
    user_id: int
    content: str

class MakeContent(ContentBase):
    pass

class ContentOut(ContentBase):
    content_id:int
    date_time: datetime

    class Config:
        orm_mode=True

class CommentBase(BaseModel):
    user_id: int
    comment: str

class MakeComment(CommentBase):
    pass

class CommentOut(CommentBase):
    comment_id:int
    date_time: datetime

    class Config:
        orm_mode=True

class LikeBase(BaseModel):
    user_id: int
    content_id: int

class MakeLike(LikeBase):
    pass

class LikeOut(LikeBase):
    like_id:int
    date_time: datetime

    class Config:
        orm_mode=True
