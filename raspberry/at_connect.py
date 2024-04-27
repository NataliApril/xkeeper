import serial
import serial.tools.list_ports
import time

#serial_port = serial.Serial('/dev/ttyUSB0', '115200')
command = "ATI+CGSN\r\n"


#read comports (ttyUSB...)
def comports_cheak():
	ports = serial.tools.list_ports.comports()
	
	for port in ports:
		print(port.device)


def at_read_write(que_imei):
	serial_port = serial.Serial('/dev/ttyUSB0', '115200')
	if serial_port:
		print ("open")
		line = serial_port.readline().decode().strip()
		if (line):
			print("Rec:", line)
	else:
		print("close")

	
def close_connect():
	serial_port.close()
	print ("AT conection close")
