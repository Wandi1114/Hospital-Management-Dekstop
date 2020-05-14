from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory, Base, modelFactory

class ormPoli(Base):
    __tablename__ = "Daftar_Poli"
    id_poli = Column(String, primary_key=True)
    nama_poli = Column(String)
    SN = 0
    def __init__(self, ID, nama):
        ormPoli.SN+=1
        session = sessionFactory()
        self.id_poli = ID+str(ormPoli.SN)
        self.nama_poli = nama
        session.add(self)
        session.commit()
        session.close()

    def delete_poli(ID):
        session = sessionFactory()
        session.quert(ormPoli).filter_by(id=ID).delete()
        session.commit()
        session.close()

    def update_poli(ID,newNama):
        session = sessionFactory()
        session.query(ormPoli).filter_by(id_poli=ID).update({
                ormPoli.nama_poli: newNama,
            }, synchronize_session=False)
        session.commit()
        session.close()

    def view_poli():
        session = sessionFactory()
        return session.query(ormPoli).all()
        session.close()
modelFactory()
