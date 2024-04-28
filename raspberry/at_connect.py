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
	
comports_list = ['/dev/ttyCH9344USB0', '/dev/ttyCH9344USB1', '/dev/ttyCH9344USB2',
				 '/dev/ttyCH9344USB3', '/dev/ttyCH9344USB4', '/dev/ttyCH9344USB5',
				 '/dev/ttyCH9344USB6', '/dev/ttyCH9344USB7']
baudrate = '115200'
				 
def at_read_write(que_imei):
	serial_port = serial.Serial(comports_list[0], baudrate)
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
				print("Rec:", line)
				
				#### errors of decode() ####
				try: 
					unicode_string = line.decode('utf-8')
				except UnicodeDecodeError:
					unicode_string = line.decode('utf-8', 'ignore')
				except serial.SerialException as se:
					print("Serial port error:", str(se))
				except serial.SerialTimeoutExcepction as ter:
					print ("Timeout error", str(ter))
					
				if (start_line in unicode_string):
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

	

