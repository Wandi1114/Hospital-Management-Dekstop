from sqlalchemy import Column, String, Integer, Text
from base import sessionFactory,Base,modelFactory
class ORM_RKE(Base):
    __tablename__ = 'RKE'
    ID_Pasien = Column(String,nullable=False, primary_key = True)
    namaPasien = Column(String,nullable=False)
    Dokter = Column(String,nullable=False)
    Diagnosa = Column(String,nullable=False)
    
    def __init__(self,ID,Nama,doker,Diagnosa):
        self.ID_Pasien = ID
        self.namaPasien = Nama
        self.Dokter = dokter
        self.Diagnosa = Diagnosa
modelFactory()