class Dokter:

    def __init__(self,ID_Dokter,Nama_Dokter,JadwalDokter,Spesialis,NoSerialDokter):
       self.ID_Dokter = ID_Dokter
       self.Nama_Dokter = Nama_Dokter
       self.JadwalDokter = JadwalDokter
       self.Spesialis = Spesialis
       self.NoSerialDokter = NoSerialDokter

    def getID_Dokter(self):
        return "Dokter: {}".format(self.ID_Dokter)

    def getNama_Dokter(self):
        return "Nama: {}".format(self.Nama_Dokter)

    def getJadwalDokter(self):
        return   "Jadwal: {}".format(self.JadwalDokter)

    def getSpesialis(self):
        return   "Spesialis: {}".format(self.Spesialis)

    def getNoSerialDokter(self):
        return   "Serial: {}".format(self.NoSerialDokter)


class DokterLainnya(Dokter):
        def __init__(self,ID_Dokter,Nama_Dokter,JadwalDokter,Spesialis,NoSerialDokter,Asal_Instansi):
            super().__init__(ID_Dokter,Nama_Dokter,JadwalDokter,Spesialis,NoSerialDokter,Asal_Instansi)
            self.Asal_Instansi = Asal_Instansi
        def getAsal_Instansi(self):
            return "Asal Instansi: {}".format(self.Asal_Instansi)



Audy = DokterLainnya(25,"ODY","Selasa","Kandungan",2102,"Balikpapan")
print(Audy.getID_Dokter())
print(Audy.getNama_Dokter())
print(Audy.getJadwalDokter())
print(Audy.getSpesialis())
print(Audy.getNoSerialDokter())
print(Audy.getAsal_Instansi())
