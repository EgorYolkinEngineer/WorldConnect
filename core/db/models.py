from sqlalchemy import Column, Integer, String
from sqlalchemy import func, DateTime
from sqlalchemy.ext.declarative import declarative_base
from core.db.mixins import SqlalchemyTableMixin, SqlalchemySerializerMixin

Base = declarative_base()


class User(Base, SqlalchemyTableMixin, SqlalchemySerializerMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)

    created = Column(DateTime, default=func.now())


class Message(Base, SqlalchemyTableMixin, SqlalchemySerializerMixin):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    text = Column(String)
    created = Column(DateTime, default=func.now())
