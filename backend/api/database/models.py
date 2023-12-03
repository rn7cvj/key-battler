import enum

from database.database import base
from sqlalchemy import TEXT, TIMESTAMP, Column, Enum, Float, ForeignKey, Integer


class UserTypes(enum.Enum):
    client = "client"
    moderator = "moderator"


class User(base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)

    nickname = Column(TEXT, unique=True)
    password = Column(TEXT)

    type = Column(Enum(UserTypes), default='client')


class RefreshTokenStorage(base):
    __tablename__ = "refresh_token_storage"

    id = Column(Integer, primary_key=True)

    refresh_token = Column(TEXT)
    expired = Column(TIMESTAMP)


class Tier(base):
    __tablename__ = "tier"

    id = Column(Integer, primary_key=True)

    name = Column(TEXT)
    speed_ratio = Column(Float)
    correct_rate_ratio = Column(Float)


class Text(base):
    __tablename__ = "text"

    id = Column(Integer, primary_key=True)
    text = Column(TEXT)
    tier = Column(ForeignKey(Tier.id))


class Result(base):
    __tablename__ = "result"

    id = Column(Integer, primary_key=True)

    text_id = Column(ForeignKey(Text.id))
    user_id = Column(ForeignKey(User.id))

    speed = Column(Integer)
    correct_rate = Column(Integer)
    time = Column(TIMESTAMP)
