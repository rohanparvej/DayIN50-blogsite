from sqlalchemy.orm import Session
from datetime import datetime
from . import models, schemas

#-------------------------------------------
# USER CREATION (External User)
#-------------------------------------------
def create_user_ext(db: Session, user: schemas.CreateUserExt):
    # Create a new user_ext object (row)
    new_user = models.User_ext(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        contact=user.contact,
        password=user.password
    )
    # Add to database session
    db.add(new_user)
    # Save (commit) the new user
    db.commit()
    # Refresh so it gets the new user_id from DB
    db.refresh(new_user)
    # Return the newly created user
    return new_user


#-------------------------------------------
# USER CREATION (Internal User)
#-------------------------------------------
def create_user_int(db: Session, user: schemas.CreateUserInt):
    new_user = models.User_int(
        username=user.username,
        full_name=user.full_name,
        email=user.email,
        contact=user.contact,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#-------------------------------------------
# CREATE CONTENT
#-------------------------------------------
def create_content(db: Session, content: schemas.MakeContent):
    new_content = models.Content(
        user_id=content.user_id,
        content=content.content,
        date_time=datetime.now()
    )
    db.add(new_content)
    db.commit()
    db.refresh(new_content)
    return new_content


#-------------------------------------------
# CREATE COMMENT
#-------------------------------------------
def create_comment(db: Session, comment: schemas.MakeComment):
    new_comment = models.Comment(
        user_id=comment.user_id,
        comment=comment.comment,
        date_time=datetime.now()
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


#-------------------------------------------
# CREATE LIKE
#-------------------------------------------
def create_like(db: Session, like: schemas.MakeLike):
    new_like = models.Like(
        user_id=like.user_id,
        content_id=like.content_id,
        date_time=datetime.now()
    )
    db.add(new_like)
    db.commit()
    db.refresh(new_like)
    return new_like
