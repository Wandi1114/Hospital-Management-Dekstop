from PyQt5.QtWidgets import QApplication,QDialog,QAbstractItemView,QMessageBox, QWidget,QHBoxLayout,QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Model.ORMPasien import ORMPasien 
#from Class.PendaftaranPoli import PendaftaranPoli

class pilihPasien(QDialog):
    def __init__(self):
        super(pilihPasien,self).__init__()
        self.InitUI()
    
    def InitUI (self):
        self.create_table()

    def cek(self,row):
        print(row)
        self.parent().terpilih(row)

    
    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellDoubleClicked.connect(self.cek)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID","NAMA PASIEN","NIK"])
        self.table.setFixedSize(335,350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()
    
    def isiTable(self):
        query = ORMPasien.view_pasien()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row,0,QTableWidgetItem(query[row].ID_Pasien))
            self.table.setItem(row,1,QTableWidgetItem(query[row].namaPasien))
            self.table.setItem(row,2,QTableWidgetItem(query[row].NIK))



def coba():
    app = QApplication(sys.argv)
    win = pilihPasien()
    win.show()
    sys.exit(app.exec_())