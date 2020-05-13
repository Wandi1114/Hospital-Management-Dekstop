#berisi code code untuk percobaan untuk menunjang aplikasi
# yang kemudian akan memanggil setiap class
from Class.Pasien import Pasien
#from Model.base import sessionFactory,modelFactory
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QDateEdit,QMessageBox, QComboBox, QTextEdit, QFormLayout, QMainWindow, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout)
import sys
 

class InputPasien(QWidget):
    def  __init__(self):
        super(InputPasien,self).__init__()
        self.setWindowTitle("Input Pasien")
        #self.setGeometry(200,200,300,400)
        self.InitUI()

    def InitUI(self):

        self.form = QFormLayout(self)

        self.nama = QLineEdit(self)
        self.nama.setPlaceholderText("Nama Pasien")
        self.form.addRow("Nama Pasien", self.nama)

        self.tglLahir = QDateEdit(self)
        self.tglLahir.setCalendarPopup(True)
        self.form.addRow("Tanggal Lahir", self.tglLahir)

        self.Nik = QLineEdit(self)
        self.Nik.setValidator(QIntValidator())
        self.Nik.setMaxLength(16)
        self.form.addRow("NIK", self.Nik)

        self.noTel = QLineEdit(self)
        self.noTel.setInputMask("+62 9999 9999 999")
        self.form.addRow("No Telpon", self.noTel)

        self.jk = QComboBox()
        self.jk.addItem("Pria")
        self.jk.addItem("Wanita")
        self.form.addRow("Jenis Kelamin ",self.jk)

        self.alamat = QTextEdit(self)
        self.alamat.setPlaceholderText("Alamat Lengkap")
        self.alamat.setFixedHeight(50)
        self.form.addRow("Alamat", self.alamat)

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
        self.noTel.clear()
        self.alamat.clear()
        self.Nik.clear()
        self.tglLahir.clear()

    def update_btn(self):
        pass

    def submit_btn(self):
        try:

            x = Pasien(self.nama.text(),
                        self.tglLahir.text(),
                        self.Nik.text(),
                        self.alamat.toPlainText(),
                        self.noTel.text(),
                        self.jk.currentText())
            kode = x.getID_Pasien()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Telah Disimpan")
            msg.setInformativeText(f"ID Pasien adalah {kode}")
            msg.setWindowTitle("Berhasil")
            s = msg.exec_()
            self.clear_btn()
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("Data Gagal Input")
            msg.setInformativeText(f"KESALAHAN : {e}")
            msg.setWindowTitle("Gagal")
            s = msg.exec_()
        
def addPasien():
    app = QApplication([sys.argv])
    win = InputPasien()
    win.show()
    sys.exit(app.exec_())
