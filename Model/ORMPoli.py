from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory, Base, modelFactory


class ormPoli(Base):
    __tablename__ = "Daftar_Poli"
    id = Column(Integer, primary_key=True)
    # nama_poli = Column(String)
    # daftar_dokter = Column(String)

    def __init__(self, ID, nama, daftar):
        session = sessionFactory()
        self.id = ID
        # self.namaPoli = nama
        # self.daftarDokter = daftar
        session.add(self)
        session.commit()
        session.close()

    def delete_poli(ID):
        session = sessionFactory()
        session.quert(ormPoli).filter_by(id=ID).delete()
        session.commit()
        session.close()

    def update_poli(ID):
        pass

    def view_poli():
        session = sessionFactory()
        return session.query(ormPoli), all()
        session.close()


modelFactory()
