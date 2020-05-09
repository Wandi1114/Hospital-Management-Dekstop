from sqlalchemy import Column, String, Integer, Text
from base import sessionFactory,Base,modelFactory
class ORM_RKE(Base):
    __tablename__ = 'RKE'
    ID_Pasien = Column(String,nullable=False, primary_key = True)
    namaPasien = Column(String,nullable=False)
    #Dokter = Column(String,nullable=False)
    Diagnosa = Column(String,nullable=False)
    #Daftar_RKE=Column (String,nullable=False)
    
    def __init__(self,ID,Nama,doker,Diagnosa):
        session = sessionFactory()
        self.ID_Pasien = ID
        self.namaPasien = Nama
        #self.Dokter = dokter
        self.Diagnosa = Diagnosa
        #self.Daftar_RKE=Daf_RKE
        session.add(self)
        session.commit()
        session.close()

    def delete_RKE(ID):
        session = sessionFactory()
        session.query(ORM_RKE).filter_by(ID_Pasien=ID).delete()
        session.commit()
        session.close()
    
    def update_RKE(ID):
        pass

    def view_RKE():
        session=sessionFactory()
        return session.query(ORM_RKE).all()
        session.close()
modelFactory()
