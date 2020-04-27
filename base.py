from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///Dokter.db')

Session = sessionmaker(bind=engine)

def session():
    Base.metadata.create_all(engine)
    return session()
