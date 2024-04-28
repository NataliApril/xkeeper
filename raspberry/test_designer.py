import test_ui11 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import queue 
import data_take as dt
from threading import *
import at_connect as at
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
        
def at_con(imei_que, com_num):
    print ("Thread AT communicate start", com_num)
    at.comports_cheak()
    at.at_read_write(imei_que, com_num)
    
def at_con_1(imei_que, com_num):
    print ("Thread AT communicate start", com_num)
    at.comports_cheak()
    at.at_read_write(imei_que, com_num)
    
        
if __name__ == "__main__":
    #global stop_tread
    q = queue.Queue()
    imei = queue.Queue()
    can_pack = queue.Queue()
    t1 = Thread(target = UI, args = (imei, ))
    t2 = Thread(target = data_in, args = (q, ))
    t3 = Thread(target = at_con, args = (imei, 0))
    t4 = Thread(target = at_con, args = (imei, 1))
    t1.deamon = True    #main prcocess
    t2.deamon = True    #deamon processt
    t3.deamon = True    #deamon process
    t4.deamon = True
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t3.join()
    t4.join()
    print("thread 3, 4 ended")
    t1.join()
    stop_tread = True
    print("thread 1 ended")
    t2.join()
    print("thread 2 ended")
    

    
