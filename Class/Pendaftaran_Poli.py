from Class.Pasien import Pasien
from Class.Poli import Poli
import datetime
dt = datetime.datetime.now()


class pendaftaran_poli:
    def __init__(self, wktu, tgl, klhn):
        self.__waktu = wktu
        self.__tanggal = tgl
        self.__keluhan = klhn

    @property
    def waktu(self):
        waktu.dt.strftime("%I:%M %p")
        return self.__waktu

    @waktu.setter
    def setWaktu(self, wktu):
        self.__waktu = wktu

    @property
    def tanggal(self):
        tanggal.dt.strftime("%Y/%m/%d")
        return self.__tanggal

    @tanggal.setter
    def tanggal(self, tgl):
        self.__tanggal = tgl

    @property
    def keluhan(self):
        return self.__keluhan

    @keluhan.setter
    def keluhan(self, klhn):
        self.__keluhan = klhn


def __str__(self):
    return "waktu : {} \n  tanggal : {} \n keluhan : {}".format(self.waktu, self.tanggal, self.keluhan)


print(pendaftaran_poli)
