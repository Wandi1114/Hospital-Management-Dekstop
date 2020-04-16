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


Audy = Dokter(21,"Audy","Senin","Gigi",2105)
print(Audy.getID_Dokter())
print(Audy.getNama_Dokter())
print(Audy.getJadwalDokter())
print(Audy.getSpesialis())
print(Audy.getNoSerialDokter())
