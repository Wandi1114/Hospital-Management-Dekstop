import datetime
class Pasien:
    JumlahPasien = 0
    def __init__(self,Nama):
        Pasien.JumlahPasien += 1
        self.__Nama_Lengkap = Nama
        self.__Tanggal_Lahir = "0000/00/00"
        self.__Umur = 0
        self.__NIK = "000"
        self.__Alamat = ""
        self.__No_Telp = ""
        self.__JenisKelamin = ""
        self.__Riwayat_Penyakit = [[],[]]
        self.__ID_Pasien = ""

        self.Daftar_Poli = []
    
    def getID_Pasien(self):
        return self.__ID_Pasien

    def setID_Pasien(self, id):
        self.__ID_Pasien = id

    def getNama_Lengkap(self):
        return self.__Nama_Lengkap

    def setNama_Lengkap(self,nl):
        self.__Nama_Lengkap = nl
    
    def getTanggal_Lahir(self):
        return self.__Tanggal_Lahir

    def setTanggal_Lahir(self,tl):
        self.__Tanggal_Lahir = tl
    
    def getUmur(self):
        self.setUmur()
        return self.__Umur

    def setUmur(self):
        tgl = self.getTanggal_Lahir.split('/')
        self.__Umur = datetime.date.today().year - int(tgl[0])
    
    def getNIK(self):
        return self.__NIK

    def setNIK(self,nik):
        self.__NIK = nik

    def getNo_Telp(self):
        return self.__No_Telp

    def setNo_Telp(self,notel):
        self.__No_Telp = notel

    def getJenis_Kelamin(self):
        return self.__Jenis_Kelamin

    def setJenis_Kelamin(self,jk):
        self.__Jenis_Kelamin = jk
    
    def Antri(self):
        pass