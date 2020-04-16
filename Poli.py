from Dokter import Dokter

class Poli:
    def __init__(self):
        self.__jenis_poli = []
        self.__daftar_dokter = []

    def getJenis_poli(self):
        return self.__jenis_poli

    def addJenis_poli(self, jenis):
        self.__jenis_poli.append(jenis)

    def getDaftar_dokter(self):
        return self.__daftar_dokter

    def addDaftar_dokter(self, daftar):
        self.__daftar_dokter.append(daftar)
