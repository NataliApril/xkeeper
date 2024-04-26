import serial
import time

serial_port = serial.Serial('/dev/ttyCH9344USB0', '115200')
#serial_port.open()
command = "ATI+CGSN\r\n"

while True:
	serial_port.write(command.encode())
	response = serial_port.readline()
	print (response)
	time.sleep(1)
	
serial_port.close()
