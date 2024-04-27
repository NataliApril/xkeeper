import serial
import time

serial_port = serial.Serial('/dev/ttyUSB0', '115200')
command = "ATI+CGSN\r\n"

def at_read_write():
	serial_port.write(command.encode())
	response = serial_port.readline()
	#print (response)
	time.sleep(1)
	return response
		
	#serial_port.close()

'''if __name__ == "__main__":
	at_read_write()'''
	
def close_connect():
	serial_port.close()
	print ("AT conection close")
