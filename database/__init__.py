#we need to install and import below libraries to create our project
from sqlalchemy import create_engine #this is neccessary and starting point to create connection with database (postgres)
from sqlalchemy.ext.declarative import declarative_base #this is to create tables and use the metadata variables (int, str, dict, ...)
from sqlalchemy.orm import sessionmaker #this is to connect user and database by creating sessions


#create connection with posthres
SQLALCHEMY_DATABASE_URI='postgresql://postgres:Otashchik@localhost/youtube'
engine=create_engine(SQLALCHEMY_DATABASE_URI)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()

#import our models to generate object and sessions to work
from database.models import User, Video, Playlist, Shorts

#create function to make objections
def get_db():
    db=SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally: #closes all the sessions in order not to create additional burdens for the database
        db.close()