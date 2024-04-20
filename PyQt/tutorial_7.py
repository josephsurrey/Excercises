import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QAction

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


        self.actionNew_Combo.triggered.connect(self.new_combo)


    def new_combo(self):
        print("New Combo")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
