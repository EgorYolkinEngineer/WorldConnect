from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import func
from database_mixins import SqlalchemyTableMixin, SqlalchemySerializerMixin
from global_config import sqlalchemy_base


class Message(sqlalchemy_base, SqlalchemyTableMixin, SqlalchemySerializerMixin):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    text = Column(String)

    created = Column(DateTime, default=func.now())
