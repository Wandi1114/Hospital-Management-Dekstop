from dbase import Base, Session, engine
from sqlalchemy import Column, Integer, String


class Klinik(Base):
    """"""
    __tablename__ = "Poli"

    id = Column(Integer, primary_key=True)
    Nama_Poli = Column(String)
    Daftar_Dokter = Column(String)

    def __init__(self, Nama_Poli, Daftar_Dokter):
        """"""
        self.Nama_Poli = Nama_Poli
        self.Daftar_Dokter = Daftar_Dokter


Base.metadata.create_all(engine)
