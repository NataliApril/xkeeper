from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (QMainWindow, QApplication)
import sys
 
app = QApplication(sys.argv)
win = uic.loadUi("test_ui.ui") # расположение вашего файла .ui
# win = QMainWindow()
win.show()
app.exec()