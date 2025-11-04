from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import foreign

from .database import Base

#importing done---------------------------------

class User_int(Base):
    __tablename__="user_int"

    user_id=Column(Integer, primary_key=True, index=True, nullable=False)
    username=Column(String, unique=True,  nullable=False)
    password=Column(String, nullable=False)
    full_name=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    contact=Column(String, unique=True)

class User_ext(Base):
    __tablename__="user_ext"
    user_id=Column(Integer, primary_key=True, index=True, nullable=False)
    username=Column(String, unique=True, nullable=False)
    password=Column(String, nullable=False)
    full_name=Column(String, nullable=False)
    email=Column(String, unique=True, nullable=False)
    contact=Column(String, unique=True)

class Content(Base):
    __tablename__="content"

    content_id=Column(Integer, index=True, nullable=False, primary_key=True)
    user_id=Column(Integer, ForeignKey("user_ext.user_id"), nullable=False)
    content=Column(Text, nullable=False)
    date_time=Column(DateTime, nullable=False)

class Comment(Base):
    __tablename__="comment"

    comment_id=Column(Integer, index=True, nullable=False, primary_key=True)
    user_id=Column(Integer, ForeignKey("user_ext.user_id"), nullable=False)
    comment=Column(Text, nullable=False)
    date_time=Column(DateTime, nullable=False)

class Like(Base):
    __tablename__="like"

    like_id=Column(Integer, index=True, nullable=False, primary_key=True)
    user_id=Column(Integer, ForeignKey("user_ext.user_id"), nullable=False)
    content_id=Column(Integer, ForeignKey("content.content_id"), nullable=False )
    date_time=Column(DateTime, nullable=False)


