from PyQt5.QtWidgets import QApplication,QAbstractItemView,QMessageBox, QWidget,QHBoxLayout,QTableWidget,QTableWidgetItem,QVBoxLayout
import sys
from Model.ORMPoli import ormPoli 
from Class.PendaftaranPoli import PendaftaranPoli

class TablePendaftaranPoli (QWidget):
    def __init__(self):
        super(TablePendaftaranPoli,self).__init__()
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
        self.table.setHorizontalHeaderLabels(["ID","NAMA POLI"])
        self.table.setFixedSize(741,350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()
    
    def isiTable(self):
        query = ormPoli.view_poli()
        self.table.setRowCount(len(query))
        for row in range(len(query)):
            self.table.setItem(row,0,QTableWidgetItem(query[row].id))
            self.table.setItem(row,1,QTableWidgetItem(query[row].nama_poli))

def draftPendaftaranPoli():
    app = QApplication(sys.argv)
    win = TablePendaftaranPoli()
    win.show()
    sys.exit(app.exec_())