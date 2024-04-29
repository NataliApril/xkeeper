import test_ui11 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import queue 
import data_take as dt
from threading import *
#import at_connect as at
import detect_devices as dd
import os

stop_tread = False

def UI(imei_q):
    global flag_end
    app = uiii.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiii.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    '''while (imei_q.qsize() <= 0):
        ui.GSM("test")
    ui.GSM(str(imei_q.get(block = False)))'''
    sys.exit(app.exec_())
    print ("stop UI")
    #os._exit(app.exec_())
    
def data_in(in_q):
    global stop_tread
    print ("Thread CAN communicate start")
    dt.clear_buffer()
    while not stop_tread:
        print ("read CAN")
        dt.take(in_q)
    #os._exit(1)
        
if __name__ == "__main__":
    q = queue.Queue()
    imei = queue.Queue()
    can_pack = queue.Queue()
    t1 = Thread(target = UI, args = (imei, ))
    t2 = Thread(target = data_in, args = (q, ))
    t3 = Thread (target = dd.detect_imei, args = (imei, ))
    t1.deamon = True    #deamon process
    t2.deamon = True    #deamon process
    t3.deamon = True    #deamon process
    t1.start()
    t2.start()
    t3.start()
    t3.join()
    t1.join()
    while imei.qsize() > 0:
        print (imei.get())
    stop_tread = True
    print("thread 1 ended")
    t2.join()
    print("thread 2 ended")
    

    
