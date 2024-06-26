import serial
import serial.tools.list_ports
import time
import queue 
import tty
import db_connect as db

command = "ATI+CGSN\r\n"
start_line = "+CGSN:"

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
	
	#open serial conection NON Block (timeout = 0)
	serial_port = serial.Serial(port_num, baudrate, timeout = 0)
	
	if serial_port:
		#open com-port
		print ("open port: ", port_num)
		
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
			
			#connect to DB
			data_base = db.DB_actions()
    
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
					#print ("imei:", line)
					to_print = line[7: len(line)-2]
					print ("imei: ", to_print)
					que_imei.put(to_print)
					
					#print to data-base
					data_base.connect_DB(to_print, port_num)
					
					#close com-port
					serial_port.close()
					
					#debug info
					print (port_num, ": conection close")
					stop_time = time.perf_counter()
					print (port_num, ": time stop: ", stop_time)
					delta = stop_time - start_time
					print (port_num, ": delta ", delta)
					print ("queue: ", que_imei.qsize())
					
					stop_thread = True
				
		print ("Thread ", port_num, " close")
	else:
		print("close")

	

