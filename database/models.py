from sqlalchemy import Column, DateTime, Integer, BigInteger, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__='users'
    user_id=Column(BigInteger, autoincrement=True, primary_key=True)
    name=Column(String, nullable=False)
    email=Column(String, nullable=False)
    user_country=Column(String, nullable=False)
    phone_number=Column(String)
    password=Column(String)
    reg_date=Column(DateTime)

class Video(Base):
    __tablename__='videos'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    duration=Column(Integer, nullable=False)
    name=Column(String, nullable=False)
    reg_date=Column(DateTime)
    user_id=Column(BigInteger, ForeignKey('users.user_id'))
    video_path=Column(String, nullable=False)
    description=Column(String, )

    user_fk=relationship(User, lazy='subquery')


class Playlist(Base):
    __tablename__='user_playlist'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    name=Column(String, nullable=False)
    category=Column(String)

    user_name=Column(BigInteger, ForeignKey('users.user_id'))
    user_video=Column(BigInteger, ForeignKey('videos.id'))

    user_fk=relationship(User, lazy='subquery')
    video_fk=relationship(Video, lazy='subquery')


class Shorts(Base):
    __tablename__='shorts'
    id=Column(BigInteger, autoincrement=True, primary_key=True)
    name=Column(String, nullable=False)

    user_id = Column(BigInteger, ForeignKey('users.user_id'))
    video_id = Column(BigInteger, ForeignKey('videos.id'))

    user_fk = relationship(User, lazy='subquery')
    video_fk = relationship(Video, lazy='subquery')

