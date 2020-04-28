from Dokter import Dokter
# from Antrian import antrian

# Antrian = antrian.Antrian


class Poli:
    def __init__(self):
        self.__Nama_Poli = []
        self.__Daftar_Dokter = []
        # self.__Antrian_Poli = Antrian

    def getNama_Poli(self):
        return self.__Nama_Poli

    def setNama_Poli(self, jenis):
        self.__Nama_Poli = jenis

    def getDaftar_Dokter(self):
        return self.__Daftar_Dokter

    def setDaftar_Dokter(self, daftar):
        self.__Daftar_Dokter = daftar

    def getJadwal_Dokter(self, jadwal):
        return self.__Jadwal_Dokter


a = Poli()
a.setNama_Poli("GIGI")
a.getNama_Poli()
