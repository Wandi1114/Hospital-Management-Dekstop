from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory,Base,modelFactory
class Poli_KIA(Base):
    __tablename__ = 'Poli_KIA'
    No_Antrian = Column(Integer,nullable=False, primary_key = True)
    Nama_Pasien = Column(String,nullable=False)
    noAntri = 0
    def __init__(self,nama):
        Poli_KIA.noAntri+=1
        session = sessionFactory()
        self.No_Antrian = Poli_KIA.noAntri
        self.Nama_Pasien = nama
        session.add(self)
        session.commit()
        session.close()
    
    def delete_poli(No_Antrian):
        session = sessionFactory()
        session.quert(Poli_KIA).filter_by(No_Antrian=noAntri).delete()
        session.commit()
        session.close()

    def update_poli(No_Antrian):
        pass

    def view_poli():
        session = sessionFactory()
        return session.query(Poli_KIA).all()
        session.close()
modelFactory()