from Pasien import Pasien
from Dokter import Dokter
from Dokter Lainnya import DokterLainnya
import datetime

class RekamMedisElektronik:

    def __init__(self, ID, Diagnosa, Tgl_konsultasi, Riwayat_obat):
        self.__ID_Dokter = ID
        self.__Diagnosa = []
        self.__Tanggal_konsultasi = Tgl_konsultasi
        self.__Riwayat_Obat = []

    @property
    def ID_Dokter(self):
        return self.__ID_Dokter
    @ID_Dokter.setter
    def ID_Dokter(self, ID):
        self.__ID_Dokter = ID

    @property
    def Diagnosa(self):
        return self.__Diagnosa    
    @Diagnosa.setter
    def Diagnosa(self, Diagnosa=[]):
        self.__Diagnosa = Diagnosa

    @property
    def Tanggal_konsultasi(self):
        Tanggal_konsultasi.datetime.date
        return self.__Tanggal_konsultasi
    @Tanggal_konsultasi.setter
    def Tanggal_konsultasi(self, Tgl_konsultasi):
        self.__Tanggal_konsultasi = Tgl_konsultasi


    @property
    def Riwayat_obat(self):
        return self.__Riwayat_Obat
    @Riwayat_obat.setter
    def Riwayat_obat(self, Riwayat_Obat):
        self.__Riwayat_obat = Riwayat_Obat

    def __str__(self):
        return "ID_Dokter : {} \n  Diagnosa : {}\n Tanggal_Konsultasi : {}\n Riwayat_Obat : {}".format(self.ID_Dokter,self.Diagnosa,self.Tanggal_konsultasi,self.Riwayat_obat)
print(RekamMedisElektronik)