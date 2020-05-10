from sqlalchemy import Column, String, Integer, Text, Date
from Model.base import sessionFactory, modelFactory, Base


class ORM_RME(Base):
    __tablename__ = 'RME'
    ID_Pasien = Column(String, nullable=False, primary_key=True)
    namaPasien = Column(String, nullable=False)
    Dokter = Column(String, nullable=False)
    TanggalKonsul = Column(Date, nullable=False)
    #Diagnosa = Column(String,nullable=False)
    #Riw_Obat = Column (String,nullable=False)

    def __init__(self, ID, Nama, dokter, Diagnosa, tgl):
        session = sessionFactory()
        self.ID_Pasien = ID
        self.namaPasien = Nama
        self.Dokter = dokter
        #self.Diagnosa = Diagnosa
        self.TanggalKonsul = tgl
        session.add(self)
        session.commit()
        session.close()

    def delete_RME(ID):
        session = sessionFactory()
        session.quert(ORM_RME).filter_by(ID_Dokter=ID).delete()
        session.commit()
        session.close()

    def update_RME(ID):
        pass

    def view_RME():
        session = sessionFactory()
        return session.query(ORM_RME), all()
        session.close()


modelFactory()
