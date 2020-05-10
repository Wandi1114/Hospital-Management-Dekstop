from sqlalchemy import Column, String, Integer, Text
from Model.base import sessionFactory, Base, modelFactory


class ORMPasien(Base):
    __tablename__ = 'Pasien_Klinik'
    ID_Pasien = Column(String, nullable=False, primary_key=True)
    namaPasien = Column(String, nullable=False)
    Tanggal_Lahir = Column(String, nullable=False)
    NIK = Column(String, nullable=False)
    Alamat = Column(Text, nullable=False)
    JenisKelamin = Column(String, nullable=False)
    noTelpPasien = Column(String, nullable=False)

    def __init__(self, ID, Nama, TL, NIK, Almt, Notel, JK):
        session = sessionFactory()
        self.ID_Pasien = ID
        self.namaPasien = Nama
        self.Tanggal_Lahir = TL
        self.NIK = NIK
        self.Alamat = Almt
        self.noTelpPasien = Notel
        self.JenisKelamin = JK
        session.add(self)
        session.commit()
        session.close()

    def delete_pasien(ID):
        session = sessionFactory()
        session.query(ORMPasien).filter_by(ID_Pasien=ID).delete()
        session.commit()
        session.close()

    def update_pasien(ID):
        pass

    def view_pasien():
        session = sessionFactory()
        return session.query(ORMPasien).all()
        session.close()


modelFactory()
