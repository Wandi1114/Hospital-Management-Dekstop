from Class.Pasien import Pasien
from Class.Dokter import Dokter


class RekamKesehatanElektronik:

    def __init__(self, Dokter, Daftar_RME, Diagnosa):
        self.__Dokter = []
        self.__Daftar_RME = []
        self.__Diagnosa = []

    @property
    def Dokter(self):
        return self.__Dokter

    @Dokter.setter
    def Dokter(self, Dokter):
        self.__Dokter = Dokter

    @property
    def Daftar_RKE(self):
        return self.__Daftar_RKE

    @Daftar_RKE.setter
    def Daftar_RKE(self, Daftar_RKE=[]):
        self.__Daftar_RKE = Daftar_RKE

    @property
    def Dokter(self):
        return self.__Diagnosa

    @Diagnosa.setter
    def Diagnosa(self, Diagnosa=[]):
        self.__Diagnosa = Diagnosa

    def __str__(self):
        return "Dokter : {} \n  Daftar_RKE : {}\n Diagnosa : {}".format(self.Dokter, self.Daftar_RKE, self.Diagnosa)
