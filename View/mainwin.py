import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

class mainwin(QMainWindow):
	def __init__(self):
		super(mainwin,self).__init__()
		self.setGeometry(200,100,1100,600)
		self.setWindowTitle("Administrasi Klinik")
		self.setMaximumSize(1100,600)
		#self.expand(False)
		#self.InitUI()
		
		self.halUt()

	def halUt(self):
		from View.halamanUtama import utama
		self.utama = utama()
		self.setCentralWidget(self.utama)

	def crudPas(self):
		from View.pasienCrud import TablePasien
		self.crudPasien = TablePasien()
		self.setCentralWidget(self.crudPasien)

	def adminPasien(self):
		from View.adminPasien import AdminPasien
		self.admin = AdminPasien()
		self.setCentralWidget(self.admin)

def App():
	app = QApplication(sys.argv)
	win = mainwin()
	win.show()
	sys.exit(app.exec_())