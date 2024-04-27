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
    at.close_connect()
    
def data_in():
    print ("Thread CAN communicate start")
    while True:
        dt.put_data(q)
        
def at_con(out_q):
    print ("Thread AT communicate start")
    #ui2 = uiii.Ui_MainWindow()
    while True:
        data = at.at_read_write()
        if data:
            out_q.put(data, block = False)
            print (data)
        #ui2.GSM(data)
    if data > "":
        uiii.GSM(data)
    
        
if __name__ == "__main__":
    q = queue.Queue()
    t1 = Thread(target = UI, args = (q, ))
    t2 = Thread(target = data_in)
    t3 = Thread(target = at_con, args = (q, ))
    t1.deamon = False   #main prcocess
    t2.deamon = True    #deamon process
    t3.deamon = True    #deamon process
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    
