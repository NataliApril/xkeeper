import tty
import at_connect as at
from threading import *
import time


#function for start thread
def at_con(imei_que, com_num):
    print ("Thread AT communicate start", com_num)
    at.at_read_write(imei_que, com_num)

def detect_imei(imei_in):  
	time.sleep(3)
	#take com-ports list
	comports_list = tty.GetCHDevices("ttyCH")
	
	#start threads for exist com-ports
	for port in comports_list:
		dev = Thread(target = at_con, args = (imei_in, port))
		dev.deamon = True
		dev.start()

    
