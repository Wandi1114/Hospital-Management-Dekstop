from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory,Base,modelFactory
class ORMAntrianFarmasi(Base):
    __tablename__ = 'Antrian_Farmasi'
    noAntrian = Column(Integer,nullable=False, primary_key = True)
    namaPasien = Column(String,nullable=False)
    Dokter = Column(String,nullable=False)
    noAntri = 0
    def __init__(self,nama,dokter):
        ORMAntrianFarmasi.noAntri+=1
        session = sessionFactory()
        self.noAntrian = ORMAntrianFarmasi.noAntri
        self.namaPasien = nama
        self.Dokter = dokter
        session.add(self)
        session.commit()
        session.close()
modelFactory()