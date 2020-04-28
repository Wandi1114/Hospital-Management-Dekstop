
class Dokter:

    def __init__(self):
        self.__ID_Dokter = ""
        self.__Nama_Dokter = ""
        self.__Jadwal_Dokter = ""
        self.__Spesialis = ""
        self.__No_Serial_Dokter = ""

    def getID_Dokter(self):
        return self.__ID_Dokter

    def setID_Dokter(self, id):
        self.__ID_Dokter = id

    def getNama_Dokter(self):
        return self.__Nama_Dokter

    def setNama_Dokter(self, nmdok):
        self.__Nama_Dokter = nmdok

    def getJadwal_Dokter(self):
        return self.__Jadwal_Dokter

    def setJadwal_Dokter(self, jdwl):
        self.__Jadwal_Dokter = jdwl

    def getSpesialis(self):
        return self.__Spesialis

    def setSpesialis(self, spsls):
        self.__Spesialis = spsls

    def getNoSerial_Dokter(self):
        return self.NoSerial_Dokter

    def setNoSerial_Dokter(self, nsd):
        self.__NoSerial_Dokter = nsd
