#berisi code code untuk percobaan untuk menunjang aplikasi
# yang kemudian akan memanggil setiap class
#from Class.Pasien import Pasien
#from Model.base import sessionFactory,modelFactory
#from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication,QMessageBox,QMainWindow, QWidget, QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout)
import sys
from Model.ORMPasien import ORMPasien
from View.PasienInput import InputPasien

class TablePasien(QMainWindow):
    def  __init__(self):
        super(TablePasien,self).__init__()
        #self.setGeometry(200,200,300,400)
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Data Pasien")
        self.setGeometry(200,200,900,500)

        self.create_table()

        self.input_btn = QPushButton(self)
        self.input_btn.setText("Tambah Pasien")
        self.input_btn.adjustSize()
        self.input_btn.clicked.connect(self.addWindow)

        self.close_btn = QPushButton(self)
        self.close_btn.setText("TUTUP")
        self.close_btn.adjustSize()
        self.close_btn.clicked.connect(self.closeWindow)

        self.vbox = QVBoxLayout(self)
        self.vbox.addWidget(self.table)
        self.vbox.addWidget(self.close_btn)
        self.vbox.addWidget(self.input_btn)


        self.container = QWidget(self)
        self.container.setLayout(self.vbox)
        self.container.adjustSize()
    
    def create_table(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setRowCount(len(ORMPasien.view_pasien()))
        self.table.setHorizontalHeaderLabels(["ID","NAMA","Tanggal Lahir","NIK","Alamat","Jenis Kelamin","No. Telp."])

        self.isiTable()
        self.table.setFixedSize(717,400)
        
    def closeWindow(self):
        self.hide()

    def addWindow(self):
        self.form = InputPasien()
        self.form.show()

    def isiTable(self):
        query = ORMPasien.view_pasien()
        for row in range(len(query)):
            #self.table.insertRow(1)
            self.table.setItem(row,0,QTableWidgetItem(query[row].ID_Pasien))
            self.table.setItem(row,1,QTableWidgetItem(query[row].namaPasien))
            self.table.setItem(row,2,QTableWidgetItem(query[row].Tanggal_Lahir))
            self.table.setItem(row,3,QTableWidgetItem(query[row].NIK))
            self.table.setItem(row,4,QTableWidgetItem(query[row].Alamat))
            self.table.setItem(row,5,QTableWidgetItem(query[row].JenisKelamin))
            self.table.setItem(row,6,QTableWidgetItem(query[row].noTelpPasien))
        
        
def crudPasien():
    app = QApplication(sys.argv)
    win = TablePasien()
    win.show()
    sys.exit(app.exec_())