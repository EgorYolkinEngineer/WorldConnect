from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from database_mixins import SqlalchemyTableMixin, SqlalchemySerializerMixin
from global_config import sqlalchemy_base
from database import engine


class Message(sqlalchemy_base, SqlalchemyTableMixin, SqlalchemySerializerMixin):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    topic_id = Column(Integer)
    text = Column(String)

    created = Column(DateTime, default=func.now())


class Topic(sqlalchemy_base, SqlalchemyTableMixin, SqlalchemySerializerMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    creator_id = Column(Integer)


sqlalchemy_base.metadata.create_all(engine)
