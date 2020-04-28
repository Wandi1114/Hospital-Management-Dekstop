from sqlalchemy import Column, String, Integer, Text
from base import Session,engine,Base
class ORMPasien(Base):
    __tablename__ = 'Pasien_Klinikewq'
    NOAntrian = Column(String,nullable=False, primary_key = True)
    namaPasien = Column(String,nullable=False)
    Dokter = Column(String,nullable=False)
    
    def __init__(self,id,nama,dokter):
        self.NOAntrian = id
        self.namaPasien = nama
        self.Dokter = dokter

Base.metadata.create_all(engine)
