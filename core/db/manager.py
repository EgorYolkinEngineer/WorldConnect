from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.db.models import Base

# engine = create_engine('sqlite:///database.db')
engine = create_engine('postgresql://postgres:1111@0.0.0.0:5432/pixeltype')

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
