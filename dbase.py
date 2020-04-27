from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///Klinik.db', echo=True)

Session = sessionmaker(bind=engine)

def session():
    Base.metadata.create_all(engine)
    return session()
