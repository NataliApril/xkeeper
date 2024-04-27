'''import os

os.system("cd ")
#search esp
#s = os.system("esptool.py --port /dev/ttyUSB0 --chip auto chip_id")

#load *.bin file
num = os.system("ls /dev/ttyUSB* & ls /dev/ttyCH*")
print (num)
s = os.system("esptool.py --chip esp8266 --baud 115200 --port /dev/ttyUSB0 write_flash -z 0x0 /home/user/xkeeper/sketch_may06a/sketch_may06a.ino.esp8285.bin")
if s == 0:
	print ("sucess")
else:
	print ("error = ", s)


import pyudev 

ctx = pyudev.Context()
print (list(ctx.list_devices(subsystem='usb')))'''

import serial
from serial.tools import list_ports

for port in list_ports.comports():
	#if "USB" in port.hwid():
	print(port)
	
#import usb.core
	
	

