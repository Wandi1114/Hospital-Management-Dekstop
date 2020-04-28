from base import Base, Session, engine
from sqlalchemy import Column, Integer, String


class Dokter(Base):

    __tablename__ = "Dokter"

    ID_Dokter = Column(Integer, primary_key=True)
    Nama_Dokter = Column(String)
    Jadwal_Dokter = ""
    Spesialis = ""
    No_Serial_Dokter = ""

    def __init__(self, Nama_Poli, Daftar_Dokter):

        self.Nama_Poli = namaPoli
        self.Daftar_Dokter = Daftar_Dokter


Base.metadata.create_all(engine)
