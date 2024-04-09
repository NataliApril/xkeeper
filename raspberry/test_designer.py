import test_ui9 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import queue 

q = queue.Queue()

if __name__ == "__main__":
    app = uiii.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiii.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.thread(q)
    sys.exit(app.exec_())
    

