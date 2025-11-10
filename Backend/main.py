from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, local_session

#-------------------------------------------
# 1. Create database tables (only once)
#-------------------------------------------
models.Base.metadata.create_all(bind=engine)

#-------------------------------------------
# 2. Make FastAPI app
#-------------------------------------------
app = FastAPI()

#-------------------------------------------
# 3. Dependency: Get DB Session
#-------------------------------------------
def get_db():
    db = local_session()
    try:
        yield db   # give the database session to the path operation
    finally:
        db.close() # close it when done

#-------------------------------------------
# 4. Root route
#-------------------------------------------
@app.get("/")
def root():
    return {"response": "400. Ok."}

#-------------------------------------------
# 5. Create internal user
#-------------------------------------------
@app.post("/user/internal", response_model=schemas.UserIntOut)
def create_user_int(user: schemas.CreateUserInt, db: Session = Depends(get_db)):
    return crud.create_user_int(db=db, user=user)

#-------------------------------------------
# 6. Create external user
#-------------------------------------------
@app.post("/user/external", response_model=schemas.UserExtOut)
def create_user_ext(user: schemas.CreateUserExt, db: Session = Depends(get_db)):
    return crud.create_user_ext(db=db, user=user)

#-------------------------------------------
# 7. Create content
#-------------------------------------------
@app.post("/content", response_model=schemas.ContentOut)
def create_content(content: schemas.MakeContent, db: Session = Depends(get_db)):
    return crud.create_content(db=db, content=content)

#-------------------------------------------
# 8. Create comment
#-------------------------------------------
@app.post("/comment", response_model=schemas.CommentOut)
def create_comment(comment: schemas.MakeComment, db: Session = Depends(get_db)):
    return crud.create_comment(db=db, comment=comment)

#-------------------------------------------
# 9. Create like
#-------------------------------------------
@app.post("/like", response_model=schemas.LikeOut)
def create_like(like: schemas.MakeLike, db: Session = Depends(get_db)):
    return crud.create_like(db=db, like=like)
