#installing and importing libraries we need to work
from fastapi import FastAPI
from database import Base, engine

#this line is to create a table using metadata, declarative_base method and binding with engine
Base.metadata.create_all(bind=engine)

#this line is to connect to fastapi and use its features via created variable 'app'
app=FastAPI()

#here we import all the files from api package to run the website for visuals
# example: from api.comments_api import comments
from api.video_api import video_api
from api.playlsit_api import play_list
from user_api import users



#we can run the website via terminal using: uvicorn main:app --reload - code