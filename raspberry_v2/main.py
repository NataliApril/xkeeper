import os
import sys
import queue 
from threading import *
import UI as UI
import USB_communicate as USB
import CAN_communicate as CAN
#import GPIO_communicate as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets

stop_tread = False

def UI_thread(imei_q):
    global flag_end
    app = UI.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    print ("stop UI")
    #os._exit(app.exec_())
    
def data_in(in_q):
    global stop_tread
    can = CAN.CAN_communicate()
    print ("Thread CAN communicate start")
    can.clear_buffer()
    while not stop_tread:
        print ("read CAN")
        can.take(in_q)
    #os._exit(1)
    
if __name__ == "__main__":
    q = queue.Queue()
    imei = queue.Queue()
    can_pack = queue.Queue()
    usb = USB.USB_communicate()
    t1 = Thread(target = UI_thread, args = (imei, ))
    t2 = Thread(target = data_in, args = (q, ))
    t3 = Thread (target = usb.detect_imei, args = (imei, ))
    
    t1.deamon = True    #deamon process
    t2.deamon = True    #deamon process
    t3.deamon = True    #deamon process
    
    t1.start()
    t2.start()
    t3.start()

    t3.join()
    print ("t3 ended")
    t1.join()
    while imei.qsize() > 0:
        print (imei.get())
    stop_tread = True
    print("thread 1 ended")
    t2.join()
    print("thread 2 ended")

    

    
