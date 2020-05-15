import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from View.myWidget.Poli_Gigi import TablePoliGigi
from View.myWidget.Poli_Umum import TablePoliUmum
from View.myWidget.Poli_KIA import TablePoliKIA
from Model.ORMPasien import ORMPasien

class AdminPasien(QWidget):
	
	def __init__(self):
		super(AdminPasien,self).__init__()

		self.InitUI()

	def InitUI(self):

		self.adminLay = QVBoxLayout()

		self.controlLay = QHBoxLayout()
		self.antriLay = QHBoxLayout()

		self.antri_form()
		self.halUt = QPushButton("Halaman Utama")
		self.halUt.clicked.connect(self.hal_utama)

		self.Pasien = QPushButton("Control Pasien")
		self.Pasien.clicked.connect(self.crudPas)

		self.controlLay.addWidget(self.halUt)
		self.controlLay.addWidget(self.Antrian)
		self.controlLay.addWidget(self.Pasien)

		self.antriGigi = TablePoliGigi()
		self.antriUmum = TablePoliUmum()
		self.antriKIA = TablePoliKIA()
		self.antriLay.addWidget(self.antriGigi)
		self.antriLay.addWidget(self.antriUmum)
		self.antriLay.addWidget(self.antriKIA)

		self.antriLay.setSpacing(20)
		self.adminLay.addLayout(self.controlLay)
		self.adminLay.addLayout(self.antriLay)
		self.setLayout(self.adminLay)

	def antri_form(self):
		# def pilih():
		# 	from pilisPas import pas
		#self.Poli = None

		self.formAntri = QFormLayout()

		self.pilihPasien = QPushButton("Pilih Pasien")
		self.pilihPasien.clicked.connect(self.pilih)
		self.formAntri.addRow("Pilih Pasien",self.pilihPasien)

		self.pilihPoli = QComboBox()
		self.pilihPoli.addItems(["Poli KIA","Poli Umum","Poli Gigi"])
		self.formAntri.addRow("Pilih Poli",self.pilihPoli)

		self.btnAntri = QPushButton("Daftarkan Pasien")
		self.btnClear = QPushButton("Clear")
		self.formAntri.addRow(self.btnClear,self.btnAntri)
		#self.formAntri.resize(450,300)

		self.Antrian = QWidget()
		self.Antrian.setLayout(self.formAntri)
		self.Antrian.setFixedWidth(500)

	def pilih(self):
		from View.myWidget.pilihPasien import pilihPasien
		self.pilPasien = pilihPasien()
		print(self.pilPasien.show())

	def terpilih(self,idx):
		query = ORMPasien.view_pasien()
		self.id= qury[idx].ID_Pasien
		self.nama = query[idx].namaPasien
		print(self.id,self.nama)

	def hal_utama(self):
		self.parent().halUt()

	def crudPas(self):
		self.parent().crudPas()



def adminPasien():
	app = QApplication(sys.argv)
	win = AdminPasien()
	win.show()
	sys.exit(app.exec_())