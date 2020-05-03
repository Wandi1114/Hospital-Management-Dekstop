from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Model/db/Kinik.db')
Base = declarative_base()
def modelFactory():
    return Base.metadata.create_all(bind=engine)

SessionFactory = sessionmaker()
SessionFactory.configure(bind=engine)
def sessionFactory():
    return SessionFactory()
modelFactory()