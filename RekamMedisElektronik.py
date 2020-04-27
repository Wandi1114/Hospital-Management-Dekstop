from Pasien import Pasien
from Dokter import Dokter
import datetime

class RekamMedisElektronik:

    def __init__(self, Pasien):
        self.Dokter = dokter.getID_Dokter()
        self.__Diagnosa = []
        self.__Tanggal_konsultasi = dokter.getTgl_konsultasi()
        self.__Riwayat_Obat = []
        self.Pasien = Pasien

    def getID_Dokter (self):
        return self.Dokter.getID_Dokter()

    def getDiagnosa (self) :
        return self.__Diagnosa
    def addDiagnosa (self,Diag):
        self.__Diagnosa.append(Diag)
    def delDiagnosa (self,Diag):
        self.__Diagnosa.del(Diag)

    def getRiwayat_Obat (self) :
        return self.__Riwayat_Obat
    def addRiwayat_Obat (self,RO):
        self.__Riwayat_Obat.append(RO)
    def delRiwayat_Obat (self,RO):
        self.__Riwayat_Obat.del(RO)

    def getTgl_konsultasi (self):
        return self.__Tanggal_konsultasi
    def setTgl_Konsultasi (self):
        self.__Tanggal_konsultasi = dt.strftime("%Y/%m/%d")
