from sqlalchemy import Column, String, Integer, Text
from base import Session,engine,Base
class ORMPasien(Base):
    __tablename__ = 'Pasien_Klinikewq'
    ID_Pasien = Column(String,nullable=False, primary_key = True)
    namaPasien = Column(String,nullable=False)
    Tanggal_Lahir = Column(String,nullable=False)
    NIK = Column(String,nullable=False)
    Alamat = Column(Text,nullable=False)
    JenisKelamin = Column(String,nullable=False)
    noTelpPasien = Column(String,nullable=False)
    
    def __init__(self,ID,Nama,TL,NIK,Almt,Notel,JK):
        self.ID_Pasien = ID
        self.namaPasien = Nama
        self.Tanggal_Lahir = TL
        self.NIK = NIK
        self.Alamat = Almt
        self.noTelpPasien = Notel
        self.JenisKelamin = JK
Base.metadata.create_all(engine)
