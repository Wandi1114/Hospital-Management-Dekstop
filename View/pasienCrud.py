#berisi code code untuk percobaan untuk menunjang aplikasi
# yang kemudian akan memanggil setiap class
#from Class.Pasien import Pasien
#from Model.base import sessionFactory,modelFactory
#from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication,QAbstractItemView,QMessageBox,QMainWindow, QWidget,QHBoxLayout, QPushButton,QTableWidget,QTableWidgetItem,QVBoxLayout)
from PyQt5.QtCore import QDate
import sys
from Model.ORMPasien import ORMPasien
from View.myWidget.PasienInput import InputPasien

class TablePasien(QWidget):
    def  __init__(self):
        super(TablePasien,self).__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Data Pasien")
        self.setGeometry(200,200,900,500)

        self.create_table()
        self.vbox = QVBoxLayout(self)

        self.input_btn = QPushButton(self)
        self.input_btn.setText("Tambah Pasien")
        #self.input_btn.setFixedWidth(200)
        self.input_btn.clicked.connect(self.addPasien)

        self.close_btn = QPushButton(self)
        self.close_btn.setText("Update")
        self.close_btn.adjustSize()
        self.close_btn.clicked.connect(self.updateTable)

        self.formInput = InputPasien()
        self.formInput.setFixedSize(300,400)

        self.hbox = QHBoxLayout(self)
        self.hbox.addWidget(self.table)
        self.hbox.addWidget(self.formInput)

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.input_btn)
        self.vbox.addWidget(self.close_btn)

        #self.container = QWidget(self)
        #self.container.setLayout(self.vbox)
        #self.container.adjustSize()
        #self.setCentralWidget(self.container)
        #self.setCentralLayout(self.vbox)

    def updateTable(self):
        self.formInput.update_btn()
        self.isiTable()
        self.formInput.clear()

    def addPasien(self):
        self.formInput.submit_btn()
        self.isiTable()
        self.formInput.clear_btn()
        #self.hbox.removeWidget(self.table)
        #self.hbox.addWidget(self.table)

    def fillForm(self,row):
        print(self.table.item(row,0).text())#ID
        print(self.table.item(row,1).text())#Nama
        print(self.table.item(row,2).text())#TglLahir
        print(self.table.item(row,3).text())#NIK
        print(self.table.item(row,4).text())#Alamat
        print(self.table.item(row,5).text())#JEnisKelamin
        print(self.table.item(row,6).text())#Notelp


        self.formInput.ID.setText(self.table.item(row,0).text())
        self.formInput.nama.setText(str(self.table.item(row,1).text()))
        self.formInput.Nik.setText((self.table.item(row,3).text()))
        self.formInput.noTel.setText(self.table.item(row,6).text())

        if str(self.table.item(row,5).text()) =='Wanita':
            idx=1
        else:
            idx=0
        self.formInput.jk.setCurrentIndex(idx)
        self.formInput.alamat.setText(self.table.item(row,4).text())

        a=self.table.item(row,2).text().split('/')
        dd = int(a[0])
        mm = int(a[1])
        yy = int(a[2])
        self.formInput.tglLahir.setDate(QDate(yy,mm,dd))
        #print(f'{dd}/{mm}/{yy}')

    def create_table(self):
        self.table = QTableWidget(self)
        self.table.cellClicked.connect(self.fillForm)
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
