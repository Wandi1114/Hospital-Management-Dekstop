from Model.base import sessionFactory
from Class.Dokter import Dokter
from Model.ORMPoli import ormPoli


class Poli:
    def __init__(self, nama_poli, daftar_dokter):
        self.__nama_poli = []
        self.__daftar_dokter = []

    @property
    def nama_poli(self):
        return self.__nama_poli

    @nama_poli.setter
    def nama_poli(self, nama_poli=[]):
        self.__nama_poli = nama_poli

    @property
    def daftar_dokter(self):
        return self.__daftar_dokter

    @daftar_dokter.setter
    def daftar_dokter(self, daftar_dokter):
        self.__daftar_dokter = daftar_dokter


def __str__(self):
    return "nama_poli : {} \n  daftar_dokter : {}".format(self.nama_poli, self.daftar_dokter)


print(Poli)
