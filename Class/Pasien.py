from Model.base import sessionFactory
from Model.ORMPasien import ORMPasien
import datetime

class Pasien:
    JumlahPasien = 0
    def __init__(self,Nama,TL,NIK,Almt,Notel,JK):
        Pasien.JumlahPasien += 1
        self.__Nama_Lengkap = Nama
        self.__Tanggal_Lahir = TL
        self.__Umur = 0
        self.__NIK = NIK
        self.__Alamat = Almt
        self.__No_Telp = Notel
        self.__JenisKelamin = JK
        self.__Riwayat_Penyakit = [[],[]]
        self.__ID_Pasien = Nama[0]+TL.split('/')[2]+str(Pasien.JumlahPasien)
        self.InsertPasien()

    def InsertPasien(self):
        x = ORMPasien(self.__ID_Pasien,
                        self.__Nama_Lengkap,
                        self.__Tanggal_Lahir,
                        self.__NIK,
                        self.__Alamat,
                        self.__No_Telp,
                        self.__JenisKelamin)

            
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
    
    @property
    def Umur(self):
        self.setUmur()
        return self.__Umur
    
    def setUmur(self):
        tgl = self.getTanggal_Lahir().split('/')
        self.__Umur = datetime.date.today().year - int(tgl[2])
    
    def getNIK(self):
        return self.__NIK

    def setNIK(self,nik):
        self.__NIK = nik
    
    def getAlamat(self):
        return self.__Alamat
    
    def setAlamat(self,alm):
        self.__Alamat = alm

    def getNo_Telp(self):
        return self.__No_Telp

    def setNo_Telp(self,notel):
        self.__No_Telp = notel

    def getJenis_Kelamin(self):
        return self.__JenisKelamin

    def setJenis_Kelamin(self,jk):
        self.__Jenis_Kelamin = jk
    
    def showPasien():
        Session = sessionFactory()
        for pasien in Session.query(ORMPasien).all():
            print(
                    "ID Pasien = {}\nNama = {}\nTanggal Lahir = {}\nNIK = {}\nAlamat = {}\nJenis Kelamin = {}\nNo. Telpon = {}\n===================="
                        .format(pasien.ID_Pasien, pasien.namaPasien, pasien.Tanggal_Lahir, pasien.NIK,
                                pasien.Alamat, pasien.JenisKelamin, pasien.noTelpPasien))
        Session.close()