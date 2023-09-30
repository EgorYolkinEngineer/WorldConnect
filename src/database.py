from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from global_config import sqlalchemy_base

engine = create_engine('sqlite:///database.db')

Session = sessionmaker(bind=engine)
session = Session()

sqlalchemy_base.metadata.create_all(engine)
