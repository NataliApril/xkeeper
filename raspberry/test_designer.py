import test_ui9 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import queue 
import data_take as dt
from threading import *

q = queue.Queue()

def UI():
    app = uiii.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiii.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
def data_in():
    while True:
        #dt.take()
        dt.put_data(q)
    
        
if __name__ == "__main__":
    t1 = Thread(target = UI)
    t2 = Thread(target = data_in)
    t1.deamon = True
    t2.deamon = True
    t1.start()
    t2.start()
    
