from Pasien import *
from Poli import *
import datetime
dt = datetime.datetime.now()
nama_poli = a.getNama_Poli()
id_pasien = wandi.getID_Pasien()


class Pendaftaran_Poli:

    def __init__(self):
        self.__Waktu = ""
        self.__Tanggal = ""
        self.__Keluhan = ""

    def getWaktu(self):
        return self.__Waktu

    def setWaktu(self):
        self.__Waktu = dt.strftime("%I:%M %p")

    def getTanggal(self):
        return self.__Tanggal

    def setTanggal(self):
        self.__Tanggal = dt.strftime("%Y/%m/%d")

    def getKeluhan(self):
        return self.__Keluhan

    def setKeluhan(self, keluhan):
        self.__Keluhan = keluhan


class Antri_Pasien:

    def __init__(self):
        self.__Nomor_Antrian = ""

    def getNomor_Antrian(self):
        return self.__Nomor_Antrian

    def setNomor_Antrian(self, nomor):
        self.__Nomor_Antrian = int(nomor)


p = Antri_Pasien()
p.setNomor_Antrian("1")

x = p.getNomor_Antrian()
y = id_pasien
z = nama_poli

print("Nomor Antrian : ", x)
print("ID Pasien :", y)
print("Poli : ", z)
