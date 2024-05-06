import os
import sys
import queue 
import time
import UI_2 as UI
from threading import *
import USB_communicate as USB
import CAN_communicate as CAN
import GPIO_communicate as GPIO
from PyQt5 import QtCore, QtGui, QtWidgets

stop_thread = False
q = queue.Queue()
imei = queue.Queue()
can_pack = queue.Queue()

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
    
def data_in(que):
    global stop_thread
    global programming_pass_status
    global programming_fail_status
    
    can = CAN.CAN_communicate()
    print ("Thread CAN communicate start")
    can.clear_buffer()
    while not stop_thread:
        result = can.take(que)

    
def toggle():
    global stop_thread
    gpio = GPIO.GPIO_communicate()
    while not stop_thread:
        gpio.write_pin(21, 1, 1)
        gpio.write_pin(21, 0, 1)
        
        
def print_cmd():
    cmd = USB.system_cmd()
    cmd.upload_file("esp8266", "/dev/ttyUSB0", "115200")
    
if __name__ == "__main__":
    q = queue.Queue()
    #imei = queue.Queue()
    can_pack = queue.Queue()
    #usb = USB.USB_communicate()
    
    t1 = Thread(target = UI_thread, args = (imei, ))
    t2 = Thread(target = data_in, args = (q, ))
    #t3 = Thread (target = usb.detect_imei, args = (imei, ))
    t4 = Thread (target = toggle)
    t5 = Thread (target = print_cmd)
    #t6 = Thread(target = test)
    
    t1.deamon = True    #deamon process
    t2.deamon = True    #deamon process
    #t3.deamon = True    #deamon process
    t4.deamon = True
    t5.deamon = True
    #t6.deamon = True
    
    t1.start()
    t2.start()
    #t3.start()
    t4.start()
    t5.start()
    #t6.start()
    
    #t3.join()
    print ("t3 ended")
    t1.join()
    '''while imei.qsize() > 0:
        print ("queue elenment: ", imei.get())
    print ("!!!!!!!!!!!")'''
    stop_thread = True
    print("thread 1 ended")
    t2.join()
    print("thread 2 ended")
    t4.join()
    print ("thread 4 ended")
    t5.join()
    print ("thread 5 ended")
    #t6.join()
    #print ("thread 6 ended")

    

    
