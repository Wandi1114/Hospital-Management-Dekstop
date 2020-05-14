from Class.Dokter import Dokter
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QDateEdit,QMessageBox, QComboBox, QTextEdit, QFormLayout, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
import sys
 

class InputDokter(QWidget):
    def  __init__(self):
        super(InputDokter,self).__init__()
        self.setWindowTitle("Dokter")
        #self.setGeometry(200,200,300,400)
        self.InitUI()

    def InitUI(self):

        self.form = QFormLayout(self)

        self.nama = QLineEdit(self)
        self.nama.setPlaceholderText("Nama Dokter")
        self.form.addRow("Nama Dokter", self.nama)

        self.Jdwl = QDateEdit(self)
        self.Jdwl.setCalendarPopup(True)
        self.form.addRow("Jadwal Dokter", self.Jdwl)

        self.Id = QLineEdit(self)
        self.Id.setValidator(QIntValidator())
        self.Id.setMaxLength(16)
        self.form.addRow("ID DOKTER", self.Id)

        self.noSeri = QLineEdit(self)
        self.noSeri.setInputMask("9999")
        self.form.addRow("No Serial Dokter", self.noSeri)

        self.Spesialis = QComboBox()
        self.Spesialis.addItem("RME")
        self.Spesialis.addItem("RKE")
        self.Spesialis.addRow("Spesialis ",self.Spesialis)

        self.submit = QPushButton(self)
        self.submit.setText("Update")
        self.submit.clicked.connect(self.update_btn)

        self.clear = QPushButton(self)
        self.clear.setText("Bersihkan")
        self.clear.clicked.connect(self.clear_btn)

        self.form.addRow(self.clear,self.submit)
        #self.form.addRow()
        
    def clear_btn(self):
        self.nama.clear()
        self.Jdwl.clear()
        self.Id.clear()
        self.NoSeri.clear()
        self.Spesialis.clear()

    def update_btn(self):
        pass

    def submit_btn(self):
        try:

            x = Dokter(self.nama.text(),
                        self.Jdwl.text(),
                        self.Id.text(),
                        self.NoSeri.toPlainText(),
                        self.Spesialis.currentText())
            kode = x.getID_Dokter()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
        
def InputDokter():
    app = QApplication([sys.argv])
    win = InputDokter()
    win.show()
    sys.exit(app.exec_())
