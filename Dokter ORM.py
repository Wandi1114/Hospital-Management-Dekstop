from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite://Dokter.db', echo=True)
#Base = declative_base()

con = engine.connect()
try:
    print("iya bisa \n yaitu merupakan : {}".format(con))
except:
    print("tidak bisa")
