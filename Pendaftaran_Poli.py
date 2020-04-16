#from Pasiem import Pasien
#from Poli import Poli
import datetime
dt = datetime.datetime.now()


class pendaftaran_poli:
    def __init__(self):
        self.__waktu = ""
        self.__tanggal = ""
        self.__keluhan = ""

    def setWaktu(self):
        self.__waktu = dt.strftime("%I:%M %p")

    def getWaktu(self):
        return self.__waktu

    def setTanggal(self):
        self.__tanggal = dt.strftime("%Y/%m/%d")

    def getTanggal(self):
        return self.__tanggal

    def setKeluhan(self, keluhan):
        self.__keluhan = keluhan

    def getKeluhan(self):
        return self.__keluhan
