from Dokter import Dokter
from Pasien import Pasien
class AntrianFarmasi:

    __JumlahAntrian = 0

    def __init__(self,dokter):
        AntrianFarmasi.__JumlahAntrian+=1
        self.__Nomor_Antrian = AntrianFarmasi.__JumlahAntrian
        self.Pasien = Pasien.getNama_Lengkap()
        self.Dokter = dokter.getNama_Dokter

    def getJumlahAntrian():
        return AntrianFarmasi.__JumlahAntrian

    def GetNomor_Antrian(self):
        return self.__Nomor_Antrian
    
    def SetNomor_Antrian(self,Nomr):
        self.__Nomor_Antrian = Nomr

    def getNama_Pasien(self):
        return  self.Pasien.getNama_Pasien()