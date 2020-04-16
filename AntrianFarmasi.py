#from Pasien import Pasien
#from Dokter import Dokter
class AntrianFarmasi:

    __JumlahAntrian = 0

    def __init__(self,pasien=None):
        AntrianFarmasi.__JumlahAntrian+=1
        self.__Nomor_Antrian = AntrianFarmasi.__JumlahAntrian
        #self.Pasien = Pasien()

    def getJumlahAntrian():
        return AntrianFarmasi.__JumlahAntrian

    def GetNomor_Antrian(self):
        return self.__Nomor_Antrian
    
    def SetNomor_Antrian(self,Nomr):
        self.__Nomor_Antrian = Nomr

    def getNama_Pasien(self):
        return  self.__NamaPasien


wandi=AntrianFarmasi()
thamrin=AntrianFarmasi()
Ody=AntrianFarmasi()
Sarah=AntrianFarmasi()

print(wandi.GetNomor_Antrian())
wandi.SetNomor_Antrian(7)
print(wandi.GetNomor_Antrian())