

import serial
from serial.tools import list_ports

for port in list_ports.comports():
	#if "USB" in port.hwid():
	print(port)
	
	
	

