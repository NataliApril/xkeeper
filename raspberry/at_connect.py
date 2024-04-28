import serial
import serial.tools.list_ports
import time
import queue 

import tty

command = "ATI+CGSN\r\n"
start_line = "+CGSN"

#read comports (ttyUSB...)
def comports_cheak():
	ports = serial.tools.list_ports.comports()
	
	for port in ports:
		print(port.device)

def close_connect():
	serial_port.close()
	#print ("AT conection close ")
	
baudrate = '115200'

#timeout 5 sec
timeout = 5
delta_time = 1
				 
def at_read_write(que_imei, port_num):
	global timeout
	global delta_time
	#take com-ports list
	comports_list = tty.GetCHDevices("ttyCH")
	
	#open serial conection NON Block (timeout = 0)
	serial_port = serial.Serial(comports_list[port_num], baudrate, timeout = 0)
	
	if serial_port:
		#open com-port
		print ("open port: ", comports_list[port_num])
		
		#flush tx and rx buffers
		serial_port.flushInput()
		serial_port.flushOutput()
		
		#send IMEI AT-command
		serial_port.write(command.encode())
		
		#flag for stop thread
		stop_thread = False
		
		#take start time
		start_time = time.perf_counter()
		round_time = time.perf_counter()
		
		#read GSM-module
		while (not stop_thread):			
			line = serial_port.readline()
			
			#cheak timeout
			if ((time.perf_counter() - start_time) > timeout):
				stop_thread = True
				serial_port.close()
			elif ((time.perf_counter() - round_time) > delta_time):
				round_time = time.perf_counter()
				#resend IMEI AT-command
				serial_port.write(command.encode())
				
			if (line):
				#errors of decode()
				try: 
					unicode_string = line.decode('utf-8')
				except UnicodeDecodeError:
					unicode_string = line.decode('utf-8', 'ignore')
				except serial.SerialException as se:
					print("Serial port error:", str(se))
				except serial.SerialTimeoutExcepction as ter:
					print ("Timeout error", str(ter))
					
				#read IMEI line	
				if (start_line in unicode_string):
					print ("imei:", line)
					que_imei.put(line.decode())
					#close com-port
					serial_port.close()
					
					# debug info
					print (comports_list[port_num], ": conection close")
					stop_time = time.perf_counter()
					print (comports_list[port_num], ": time stop: ", stop_time)
					delta = stop_time - start_time
					print (comports_list[port_num], ": delta ", delta)
					print ("queue: ", que_imei.qsize())
					
					stop_thread = True
				
		print ("exit from while")
	else:
		print("close")

	

