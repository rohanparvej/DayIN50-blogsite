from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#importing done-------------------------------

DB_URL=""

engine=create_engine(DB_URL) #created engine with passing db url
local_session=sessionmaker(autocommit=False, autoflush=False, bind=engine) #making session
Base=declarative_base(engine) #created a base instance by passing the engine

#instances created-----------------------------

def get_db():
    db=local_session()
    try:
        yield db
    finally:
        db.close()