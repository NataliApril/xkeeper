import test_ui11 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import queue 
import data_take as dt
from threading import *
import at_connect as at



def UI(in_q):
    app = uiii.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiii.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.GSM(in_q)
    MainWindow.show()
    sys.exit(app.exec_())
    
def data_in():
    while True:
        dt.put_data(q)
        
def at_con(out_q):
    #ui2 = uiii.Ui_MainWindow()
    while True:
        data = at.at_read_write()
        if data:
            out_q.put(data, block = False)
            print (data)
        #ui2.GSM(data)
    '''if data > "":
        uiii.GSM(data)'''
    
        
if __name__ == "__main__":
    q = queue.Queue()
    t1 = Thread(target = UI, args = (q, ))
    t2 = Thread(target = data_in)
    t3 = Thread(target = at_con, args = (q, ))
    t1.deamon = True
    t2.deamon = True
    t3.deamon = True
    t1.start()
    t2.start()
    t3.start()
    
