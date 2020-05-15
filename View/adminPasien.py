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
        super(AdminPasien, self).__init__()

        self.InitUI()

    def InitUI(self):
        self.stylesheet = """
        QPushButton{
            background-color: #f7f7f7;
			border: 0.5px solid #d1d1d1;
            border-radius: 3;
            color: #333;
        }
        QPushButton::hover{
            background-color: #47F1A0;
        }
        """

        self.setStyleSheet(self.stylesheet)

        font = QFont()

        self.adminLay = QVBoxLayout()

        self.controlLay = QHBoxLayout()
        self.antriLay = QHBoxLayout()

        self.antri_form()

        font.setPointSize(11)
        font.setWeight(2)
        self.halUt = QPushButton("<-- Halaman Utama")
        self.halUt.setFont(font)
        self.halUt.setFixedHeight(50)
        self.halUt.clicked.connect(self.hal_utama)

        font.setPointSize(11)
        font.setWeight(2)
        self.Pasien = QPushButton("Control Pasien -->")
        self.Pasien.setFont(font)
        self.Pasien.setFixedHeight(50)
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
        font = QFont()

        font.setPointSize(10)
        font.setWeight(1)
        self.pilihPasien = QPushButton("Pilih Pasien")
        self.pilihPasien.setFont(font)
        self.pilihPasien.clicked.connect(self.pilih)
        self.pilihPasien.setFixedHeight(20)
        self.formAntri.addRow("Pilih Pasien", self.pilihPasien)

        self.pilihPoli = QComboBox()
        self.pilihPoli.setFixedHeight(20)
        self.pilihPoli.addItems(["Poli KIA", "Poli Umum", "Poli Gigi"])
        self.formAntri.addRow("Pilih Poli", self.pilihPoli)

        font.setPointSize(10)
        font.setWeight(1)
        self.btnAntri = QPushButton("Daftarkan Pasien")
        self.btnAntri.setFixedHeight(20)
        self.btnAntri.setFont(font)
        self.btnClear = QPushButton("Clear")
        self.btnClear.setFont(font)
        self.btnClear.setFixedSize(50, 20)
        self.formAntri.addRow(self.btnClear, self.btnAntri)
        # self.formAntri.resize(450,300)

        self.Antrian = QWidget()
        self.Antrian.setLayout(self.formAntri)
        self.Antrian.setFixedWidth(500)

    def pilih(self):
        from View.myWidget.pilihPasien import pilihPasien
        self.pilPasien = pilihPasien()
        print(self.pilPasien.show())

    def terpilih(self, idx):
        query = ORMPasien.view_pasien()
        self.id = query[idx].ID_Pasien
        self.nama = query[idx].namaPasien
        print(self.id, self.nama)

    def hal_utama(self):
        self.parent().halUt()

    def crudPas(self):
        self.parent().crudPas()


def adminPasien():
    app = QApplication(sys.argv)
    win = AdminPasien()
    win.show()
    sys.exit(app.exec_())
