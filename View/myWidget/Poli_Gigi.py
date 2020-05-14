from PyQt5.QtWidgets import QApplication,QAbstractItemView,QMessageBox, QWidget,QHBoxLayout,QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Model.ORMPoli_Gigi import Poli_Gigi
from Class.Poli import Poli

class TablePoliGigi (QWidget):
    def __init__(self):
        super(TablePoliGigi,self).__init__()
        self.InitUI()
    
    def InitUI (self):
        self.create_table()
    
    def cek(self,row):
        print(self.table.item(row,0).text())
        print(self.table.item(row,1).text())
    
    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["No Antrian","Nama Pasien"])
        self.table.setFixedSize(741,350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()
    
    def isiTable(self):
        query = Poli_Gigi.view_poli()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            #self.table.insertRow(1)
            self.table.setItem(row,0,QTableWidgetItem(query[row].No_Antrian))
            self.table.setItem(row,1,QTableWidgetItem(query[row].Nama_Pasien))

def draftPoliGigi():
    app = QApplication(sys.argv)
    win = TablePoliGigi()
    win.show()
    sys.exit(app.exec_())