import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore


class utama:
    def __init__(self):
        super().__init__()
        self.app = QApplication([])
        self.mainWindow = QMainWindow()
        self.mainWindow.setWindowTitle("Login")
        self.mainWindow.setGeometry(360, 180, 683, 360)
        self.mainWindow.setStyleSheet("background-color : #47F1A0")

        self.depan()

        self.mainWindow.show()
        sys.exit(self.app.exec_())

    def depan(self):
        self.stylesheet = """
        QWidget{
            color: #fafafa;
            font-family: 'Nunito';
        }
        QFrame{
            background-color: #47F1A0;
        }
        QLabel#header{
            font-family: 'Raleway';
        }
        QPushButton{
            background-color: #f7f7f7;
            border: none;
            border-radius: 4;
            color: #333;
        }
        QPushButton::hover{
            background-color: #31b074;
        }
        """
        self.centralWidget = QWidget(self.mainWindow)
        self.centralWidget.setObjectName("depanWidget")
        self.centralWidget.setFixedSize(683, 360)
        self.centralWidget.setStyleSheet(self.stylesheet)

        self.verticalLay = QVBoxLayout(self.centralWidget)
        self.verticalLay.setObjectName("verticalLayout")

        self.frame = QFrame(self.centralWidget)
        self.frame.setFixedSize(683, 360)
        self.frame.setObjectName("frame")
        self.frame.setLayoutDirection(Qt.LeftToRight)

        self.vertical = QVBoxLayout(self.frame)
        self.vertical.setObjectName("vLayout")

        font = QFont()
        font.setPointSize(20)
        font.setWeight(5)
        font.setBold(True)
        self.teksUtama = QLabel(
            "Selamat Datang! di \n Aplikasi Klinik Sayang", self.frame)
        self.teksUtama.setFont(font)
        self.teksUtama.setWordWrap(True)
        self.teksUtama.setAlignment(Qt.AlignCenter)
        self.teksUtama.setGeometry(180, 10, 310, 65)

        font.setPointSize(12)
        font.setWeight(3)
        self.teksKet = QLabel(
            "Silahkan pilih tampilan sesuai dengan kebutuhan! ^.^", self.frame)
        self.teksKet.setFont(font)
        self.teksKet.setWordWrap(True)
        self.teksKet.setAlignment(Qt.AlignCenter)
        self.teksKet.setGeometry(160, 100, 355, 40)

        font.setPointSize(12)
        font.setWeight(2)
        self.btnAdmin = QPushButton("Admin View", self.frame)
        self.btnAdmin.setObjectName("btnAdmin")
        self.btnAdmin.setGeometry(100, 230, 100, 20)
        self.btnAdmin.resize(200, 45)
        self.btnAdmin.setFont(font)
        self.btnAdmin.setCursor(QCursor(Qt.PointingHandCursor))

        font.setPointSize(12)
        font.setWeight(2)
        self.btnDokter = QPushButton("Dokter View", self.frame)
        self.btnDokter.setObjectName("btnDokter")
        self.btnDokter.setGeometry(380, 230, 100, 20)
        self.btnDokter.resize(200, 45)
        self.btnDokter.setFont(font)
        self.btnDokter.setCursor(QCursor(Qt.PointingHandCursor))


utama()
