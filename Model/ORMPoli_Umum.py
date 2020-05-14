from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory,Base,modelFactory
class Poli_Umum(Base):
    __tablename__ = 'Poli_Umum'
    No_Antrian = Column(Integer,nullable=False, primary_key = True)
    Nama_Pasien = Column(String,nullable=False)
    noAntri = 0
    def __init__(self,nama):
        Poli_Umum.noAntri+=1
        session = sessionFactory()
        self.No_Antrian = Poli_Umum.noAntri
        self.Nama_Pasien = nama
        session.add(self)
        session.commit()
        session.close()

    def delete_poli(No_Antrian):
        session = sessionFactory()
        session.quert(Poli_Umum).filter_by(No_Antrian=noAntri).delete()
        session.commit()
        session.close()

    def update_poli(No_Antrian):
        pass

    def view_poli():
        session = sessionFactory()
        return session.query(Poli_Umum).all()
        session.close()
modelFactory()