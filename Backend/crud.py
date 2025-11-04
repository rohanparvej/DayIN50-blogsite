from sqlalchemy.orm import Session
from . import models, schemas

#importing done-----------------------

def create_user_ext(db: Session, user: schemas.CreateUserExt):
    new_user_ext=models.User_ext(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        contact=user.contact,
        password=user.password
    )
    db.add(new_user_ext)
    db.commit()
    db.refresh(new_user_ext)
    return new_user_ext

def create_user_int(db: Session, user: schemas.CreateUserInt):
    new_user_int=models.User_int(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        contact=user.contact,
        password=user.password
    )
    db.add(new_user_int)
    db.commit()
    db.refresh(new_user_int)
    return new_user_int

def create_comment(db: Session, comment: schemas.MakeComment, user: schemas.UserExtBase):
    new_comment=models.Comment(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        contact=user.contact,
        password=user.password
    )
    db.add(new_user_ext)
    db.commit()
    db.refresh(new_user_ext)
    return new_user_ext




