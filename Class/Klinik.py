from Pasien import Pasien
class Klinik:
    
    def __init__(self,Nama="Klinik ITK",Alamat="Karang Joang"):
        self.__Nama_Klinik = Nama
        self.__Alamat = Alamat
        self.DaftarPoli = []
        self.Daftar_Pasien = []
        self.JumlahPasien = Pasien.JumlahPasien
    
    def UpdateJumlahPasien(self,jumlah):
        self.JumlahPasien = Pasien.Jumlah

    def getNama_Klinik(self):
        return self.__Nama_Klinik

    def setNama_Klinik(self,nama):
        sefl.__Nama_Klinik = nama
    
    def getAlamat(self):
        return self.__Alamat

    def setNama_Klinik(self,alamat):
        self.__Alamat = alamat

    def Register_Pasien(self):
        pass