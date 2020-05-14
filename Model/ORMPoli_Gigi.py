from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory,Base,modelFactory
class Poli_Gigi(Base):
    __tablename__ = 'Poli_Gigi'
    No_Antrian = Column(Integer,nullable=False, primary_key = True)
    Nama_Pasien = Column(String,nullable=False)
    noAntri = 0
    def __init__(self,nama):
        Poli_Gigi.noAntri+=1
        session = sessionFactory()
        self.No_Antrian = Poli_Gigi.noAntri
        self.Nama_Pasien = nama
        session.add(self)
        session.commit()
        session.close()

    def delete_poli(No_Antrian):
        session = sessionFactory()
        session.quert(Poli_Gigi).filter_by(No_Antrian=noAntri).delete()
        session.commit()
        session.close()

    def update_poli(No_Antrian):
        pass

    def view_poli():
        session = sessionFactory()
        return session.query(Poli_Gigi).all()
        session.close()

modelFactory()