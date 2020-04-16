from Dokter import Dokter

class DokterLainnya(Dokter):
    
        def __init__(self,ID_Dokter,Nama_Dokter,JadwalDokter,Spesialis,NoSerialDokter,Asal_Instansi):
            super().__init__(self,ID_Dokter,Nama_Dokter,JadwalDokter,Spesialis,NoSerialDokter)
            self.__Asal_Instansi = Asal_Instansi

        def getAsal_Instansi(self):
            return self.Asal_Instansi
        
        def setAsal_INstansi(self,ai):
            self.__Asal_Instansi = ai
