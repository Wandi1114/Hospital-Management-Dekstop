from View.pasienCrud import TablePasien
from PyQt5.QtWidgets import QApplication
import sys
app = QApplication(sys.argv)
table = TablePasien()
table.show()
sys.exit(app.exec_())
#<Model.ORMPasien.ORMPasien object at 0x000000000363C3D0>
