import serial
import serial.tools.list_ports
import time
import queue 

#serial_port = serial.Serial('/dev/ttyUSB0', '115200')
command = "ATI+CGSN\r\n"
start_line = "+CGSN"

#read comports (ttyUSB...)
def comports_cheak():
	ports = serial.tools.list_ports.comports()
	
	for port in ports:
		print(port.device)

def close_connect():
	serial_port.close()
	print ("AT conection close")
	
	
def at_read_write(que_imei):
	serial_port = serial.Serial('/dev/ttyUSB0', '115200')
	if serial_port:
		print ("open")
		time.sleep(0.5)
		serial_port.flushInput()
		serial_port.flushOutput()
		serial_port.write(command.encode())
		print("command send")
		while True:
			#line = serial_port.readline().decode().strip()
			line = serial_port.readline()
			if (line):
				#print("Rec:", line)
				
				#### errors of decode() ####
				if (start_line in line.decode()):
					print ("imei:", line)
					que_imei.put(line.decode())
					
					serial_port.close()
					print ("AT conection close")
					break
				#else:
				#	print("not equalse")
			#else:
			#	print ("empty")
	else:
		print("close")

	

