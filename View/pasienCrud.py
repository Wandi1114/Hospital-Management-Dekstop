#berisi code code untuk percobaan untuk menunjang aplikasi
# yang kemudian akan memanggil setiap class
#from Class.Pasien import Pasien
#from Model.base import sessionFactory,modelFactory
#from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication,QAbstractItemView,QMessageBox,QMainWindow, QWidget,QHBoxLayout, QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout)
import sys
#from PyQt5.QtCore import QAbstractItemView
from Model.ORMPasien import ORMPasien
from View.PasienInput import InputPasien

class TablePasien(QMainWindow):
    def  __init__(self):
        super(TablePasien,self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Data Pasien")
        self.setGeometry(200,200,900,500)

        self.create_table()

        self.input_btn = QPushButton(self)
        self.input_btn.setText("Tambah Pasien")
        self.input_btn.adjustSize()
        self.input_btn.clicked.connect(self.addPasien)

        self.close_btn = QPushButton(self)
        self.close_btn.setText("TUTUP")
        self.close_btn.adjustSize()
        self.close_btn.clicked.connect(self.closeWindow)

        self.formInput = InputPasien()
        self.formInput.setFixedSize(300,400)

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.table)
        self.hbox.addWidget(self.formInput)

        self.vbox = QVBoxLayout(self)
        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.input_btn)
        self.vbox.addWidget(self.close_btn)


        self.container = QWidget(self)
        self.container.setLayout(self.vbox)
        self.container.adjustSize()
        self.setCentralWidget(self.container)

    def closeWindow(self):
        self.hide()

    def addPasien(self):
        self.formInput.submit_btn()
        #self.hbox.removeWidget(self.table)
        self.isiTable()
        #self.hbox.addWidget(self.table)

    def cek(self,row):
        print(self.table.item(row,0).text())
        print(self.table.item(row,1).text())
        print(self.table.item(row,2).text())
        print(self.table.item(row,3).text())
        print(self.table.item(row,4).text())
        print(self.table.item(row,5).text())
        print(self.table.item(row,6).text())


    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.cek)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID","NAMA","Tanggal Lahir","NIK","Alamat","Jenis Kelamin","No. Telp."])
        self.table.setFixedSize(741,350)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.isiTable()

    def isiTable(self):
        query = ORMPasien.view_pasien()
        self.table.setRowCount(len(query))
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
    #app.setStyle('fusion')
    win = TablePasien()
    win.show()
    sys.exit(app.exec_())
