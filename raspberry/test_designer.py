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
        #dt.put_data(q)
        dt.take(in_q)
        
def at_con(imei_que):
    print ("Thread AT communicate start")
    at.comports_cheak()
    at.at_read_write(imei_que)
    
    #if (imei_que.qsize() > 0):
    #    ui2.GSM(imei_que.get())
    #at.at_read_write(imei_q)
        #uiii.GSM("test")
        #if imei_q:
            #uiii.GSM (imei_q.get())
            #print (data)
        #ui2.GSM(data)
        #if data > "":
            #uiii.GSM(data)
    
        
if __name__ == "__main__":
    q = queue.Queue()
    imei = queue.Queue()
    t1 = Thread(target = UI, args = (imei, ))
    t2 = Thread(target = data_in, args = (q, ))
    t3 = Thread(target = at_con, args = (imei, ))
    t1.deamon = False   #main prcocess
    t2.deamon = True    #deamon processt
    t3.deamon = True    #deamon process
    t1.start()
    t2.start()
    t3.start()
    #t1.join()
    t2.join()
    t3.join()

    
