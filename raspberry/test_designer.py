import test_ui11 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import queue 
import data_take as dt
from threading import *
import at_connect as at



def UI(imei_q):
    app = uiii.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiii.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    '''while (imei_q.qsize() <= 0):
        ui.GSM("test")
    ui.GSM(str(imei_q.get(block = False)))'''
    sys.exit(app.exec_())
    
def data_in(in_q):
    print ("Thread CAN communicate start")
    dt.clear_buffer()
    while True:
        dt.take(in_q)
        
def at_con(imei_que, com_num):
    print ("Thread AT communicate start", com_num)
    at.comports_cheak()
    at.at_read_write(imei_que, com_num)
    
def at_con_1(imei_que, com_num):
    print ("Thread AT communicate start", com_num)
    at.comports_cheak()
    at.at_read_write(imei_que, com_num)
    
        
if __name__ == "__main__":
    q = queue.Queue()
    imei = queue.Queue()
    can_pack = queue.Queue()
    #UI(imei)
    t1 = Thread(target = UI, args = (imei, ))
    t2 = Thread(target = data_in, args = (q, ))
    t3 = Thread(target = at_con, args = (imei, 0))
    t4 = Thread(target = at_con, args = (imei, 1))
    t1.deamon = False   #main prcocess
    t2.deamon = True    #deamon processt
    t3.deamon = True    #deamon process
    t4.deamon = True
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    
