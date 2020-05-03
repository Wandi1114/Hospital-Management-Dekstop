class Dokter:

    def __init__(self,ID_Dokter,Nama_Dokter,JadwalDokter,Spesialis,NoSerialDokter):
       self.__ID_Dokter = ID_Dokter
       self.__Nama_Dokter = Nama_Dokter
       self.__JadwalDokter = JadwalDokter
       self.__Spesialis = Spesialis
       self.__NoSerialDokter = NoSerialDokter

    def getID_Dokter(self):
        return self.__ID_Dokter
    
    def setID_Dokter(self,id):
        self.__ID_Dokter = id

    def getNama_Dokter(self):
        return self.__Nama_Dokter

    def setNama_Dokter(self,nm):
        self.__Nama_Dokter = nm

    def getJadwalDokter(self):
        return self.__JadwalDokter

    def setJadwal_Dokter(self,jdw):
        self.__Jadwal_Dokter = jdw

    def getSpesialis(self):
        return self.__Spesialis

    def setSpesialis(self,spesial):
        self.__Spesialis = spesial

    def getNoSerialDokter(self):
        return self.__NoSerialDokter

    def setNoSerialDokter(self,nsd):
        self.__NoSerialDokter = nsd