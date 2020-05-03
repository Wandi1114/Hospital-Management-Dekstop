from sqlalchemy import Column, String, Integer, Text, Date
from Model.base import sessionFactory,modelFactory,Base
class ORM_RME(Base):
    __tablename__ = 'RME'
    ID_Pasien = Column(String,nullable=False, primary_key = True)
    namaPasien = Column(String,nullable=False)
    Dokter = Column(String,nullable=False)
    Diagnosa = Column(String,nullable=False)
    TanggalKonsul = Column(Date,nullable=False)

    
    def __init__(self,ID,Nama,dokter,Diagnosa,tgl):
        self.ID_Pasien = ID
        self.namaPasien = Nama
        self.Dokter = dokter
        self.Diagnosa = Diagnosa
        self.TanggalKonsul = tgl
modelFactory()