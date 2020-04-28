from base import Base, Session, engine
from sqlalchemy import Column, Integer, String


class Klinik(Base):
    """"""
    __tablename__ = "Poli"

    id = Column(Integer, primary_key=True)
    Nama_Poli = Column(String)
    Daftar_Dokter = Column(String)
    # Antrian_Poli = Antrian

    def __init__(self, Nama_Poli, Daftar_Dokter):
        """"""
        self.Nama_Poli = namaPoli
        self.Daftar_Dokter = Daftar_Dokter


Base.metadata.create_all(engine)
