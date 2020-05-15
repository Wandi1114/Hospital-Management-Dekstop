import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from View.pasienCrud import TablePasien


class utama(QWidget):
    def __init__(self):
        super(utama, self).__init__()
        # self.setWindowTitle("Login")
        #self.setGeometry(360, 180, 680, 400)
        # self.setStyleSheet("background-color : #47F1A0")

        self.InitUI()
        # self.setCentralWidget(self.centralWidget)

    def InitUI(self):
        self.stylesheet = """
        QPushButton{
            background-color: #f7f7f7;
            border: 2px solid black;
            border-radius: 4;
            color: #333;
        }
        QPushButton::hover{
            background-color: #47F1A0;
        }
        """
        self.centralWidget = QWidget(self)
        self.setStyleSheet(self.stylesheet)

        self.vbox = QVBoxLayout()

        font = QFont()
        font.setPointSize(20)
        font.setWeight(5)
        font.setBold(True)
        self.teksUtama = QLabel("Selamat Datang! di Aplikasi Klinik Sayang")
        self.teksUtama.setFont(font)
        self.teksUtama.setWordWrap(True)
        self.teksUtama.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.teksUtama, alignment=Qt.AlignCenter)
        #self.teksUtama.setGeometry(180, 10, 310, 65)

        font.setPointSize(12)
        font.setWeight(3)
        self.teksKet = QLabel(
            "Silahkan pilih tampilan sesuai dengan kebutuhan! ^.^")
        self.teksKet.setFont(font)
        # self.teksKet.setWordWrap(True)
        self.teksKet.setAlignment(Qt.AlignCenter)
        self.vbox.addWidget(self.teksKet, alignment=Qt.AlignCenter)
        self.hbox = QHBoxLayout()
        font.setPointSize(12)
        font.setWeight(2)
        self.btnAdmin = QPushButton("Administrasi Pasien")
        # self.btnAdmin.setObjectName("btnAdmin")
        #self.btnAdmin.setGeometry(100, 230, 100, 20)
        self.btnAdmin.setFixedSize(200, 45)
        self.btnAdmin.setFont(font)
        self.btnAdmin.clicked.connect(self.adminPas)
        self.btnAdmin.setCursor(QCursor(Qt.PointingHandCursor))
        self.hbox.addWidget(self.btnAdmin)

        font.setPointSize(12)
        font.setWeight(2)
        self.btnDokter = QPushButton("Administrasi Dokter")
        # self.btnDokter.setObjectName("btnDokter")
        #self.btnDokter.setGeometry(380, 230, 100, 20)
        self.btnDokter.setFixedSize(200, 45)
        self.btnDokter.setFont(font)
        self.btnDokter.setCursor(QCursor(Qt.PointingHandCursor))
        self.hbox.addWidget(self.btnDokter)

        self.vbox.addLayout(self.hbox)
        self.vbox.setSpacing(40)
        #self.teksKet.setGeometry(160, 100, 355, 40)
        #self.Frame.setFixedSize(683, 360)
        # self.Frame.setObjectName("frame")
        # self.Frame.setLayoutDirection(Qt.LeftToRight)
        self.centralWidget.setLayout(self.vbox)
        self.centralWidget.move(300, 100)
        # self.centralWidget.

    def crudPasien(self):
        self.parent().crudPas()

    def adminPas(self):
        self.parent().adminPasien()

    def mainWindow(self):
        self.setCentralWidget(self.centralWidget)


def main():
    app = QApplication(sys.argv)
    win = utama()
    win.show()
    sys.exit(app.exec_())

    # self.centralWidget = QWidget(self)
    # #self.centralWidget.setObjectName("depanWidget")
    # #self.centralWidget.setFixedSize(683, 360)
    # self.centralWidget.setStyleSheet(self.stylesheet)

    # self.verticalLay = QVBoxLayout(self.centralWidget)
    # #self.verticalLay.setObjectName("verticalLayout")

    # self.frame = QFrame(self.centralWidget)

    # self.vertical = QVBoxLayout(self.frame)
    # #self.vertical.setObjectName("vLayout")
