import serial
import time

serial_port = serial.Serial('/dev/ttyCH9344USB0', '115200')
command = "ATI+CGSN\r\n"

def at_read_write():
	while True:
		serial_port.write(command.encode())
		response = serial_port.readline()
		print (response)
		time.sleep(1)
	serial_port.close()

'''if __name__ == "__main__":
	at_read_write()'''
