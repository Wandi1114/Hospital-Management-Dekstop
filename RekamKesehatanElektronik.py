from Pasien import Pasien
from Dokter import Dokter
import datetime

class RekamKesehatanElektronik:

    def __init__(self, Dokter, Daftar_RKE, Diagnosa):
        self.__XDokter= []
        self.__Daftar_RK= []
        self.__Diagnosa_Kesehatan = []
        self.__Riwayat_Penyakit = Pasien.getRiwayat_Penyakit
        self.Pasien=Pasien

    def getXDokter (self) :
        return self.__XDokter
    def addXDokter (self,XD):
        self.__XDokter.append(XD)
    def delXDokter (self,XD):
        self.__XDokter.del(XD)
    
    def getDaftar_RK (self) :
        return self.__Daftar_RK
    def addDaftar_RK (self,DRK):
        self.__Daftar_RK.append(DRK)
    def delDaftar_RK (self,DRK):
        self.__Daftar_RK.del(DRK)

    def getDiagnosa_Kesehatan (self,XDokter) :
        return self.__Diagnosa.XDokter
    def addDiagnosa (self,Diag,Tgl,ID_Dokter):
        self.Diag = Tgl (dt,strftime),ID_Dokter.getID_Dokter
        self.__Diagnosa.append(Diag)
    def delDiagnosa (self,Diag):
        self.__Diagnosa.del(Diag)

    def getRiwayat_Penyakit (self):
        return self.Pasien.getRiwayat_Penyakit
    def setRiwayat_Penyakit (self,DRK):
        self.__Riwayat_Penyakit = RiwPe
