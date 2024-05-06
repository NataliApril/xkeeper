import time
import can
import queue
import struct
from collections import namedtuple
import numpy as np

interface = 'socketcan'
channel = 'can0'
#motor_data = namedtuple('motor_data', ['id', 'acc', 'dec', 'dir', 'speed', 'step']) 
#programmator = namedtuple('programmator', ['id', 'start', 'OK', 'error', 'n1', 'n2', 'n3', 'n4'])
format_string = '<BBBBHH'

input_format = '>BHHBBB'

class CAN_communicate(): 
	
	motor =       [23, 0, 0, 0, 0, 0] 
	start_run =   [88, 0, 0, 0, 0, 0] 
	start_move =  [89, 0, 0, 0, 0, 0] 
	stop =        [99, 0, 0, 0, 0, 0]
	programming = [11, 0, 0, 0, 0, 0]
	
	#programming_pass_status = 4095
	#programming_fail_status = 4095
	
	

	''' pack data to send '''
	def pack(self, list):
		packed_data = struct.pack(format_string, *list)
		return packed_data
		
	def unpack(self, list):
		unpacked_data = struct.unpack(input_format, list)
		return unpacked_data

	''' parse data '''
	def parse(self, data):
		if data[0] == 23:
			print ("motor")
		elif data[0] == 88:
			print ("move")
		elif data[0] == 89:
			print("run")
		elif data[0] == 99:
			print("stop")
		elif data[0] == 11:
			print ("programming ")
		else:
			print ("unknown")
		#return 0
	
	''' send data '''  
	def producer(self, _str):
		bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
		match _str:
			case "motor":
				packed_data = self.pack(self.motor)
			case "start_run":
				packed_data = self.pack(self.start_run)
			case "start_move":
				packed_data = self.pack(self.start_move)
			case "stop":
				packed_data = self.pack(self.stop)
			case "programm":
				packed_data = self.pack(self.programming)
			
		#msg_queue_out.put(packed_data)
		#print ("put data")
		print ("data out:", packed_data)
		msg = can.Message(arbitration_id=0xc0ffee,
						  data=packed_data,
						  is_extended_id=False)
		bus.send(msg)
    
	''' send data packet '''
	def send_packet(self, msg_queue_in):
		bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
		if (msg_queue_in.empty()):
			print("empty")
		else:
			print ("get")
			packed_data = msg_queue_in.get(block = False)
			print ("data out:", packed_data)
			msg = can.Message(arbitration_id=0xc0ffee,
							  data=packed_data,
							  is_extended_id=False)
			bus.send(msg)

	''' print in data '''
	def print_data(self, msg):
		print ("data in:", msg.data)

	''' get data from can bus '''
	def put_data(self, q):
		bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
		message = bus.recv()
		q.put(message.data)
		print ("size: ", q.qsize())
		print ("data: ", message.data)
		parse(q.get())
		
	''' take data from can bus '''
	def take(self, in_queue):
		bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
		reader = can.BufferedReader()
		bus_notifier = can.Notifier(bus, [reader]) 
		msg = reader.get_message(1)
		if msg is not None:
			#data about programming status
			if (msg.data[0] == 12):
				result = self.unpack(msg.data)
				print ("programming ", result)
				self.programming_status(result[1], result[2], in_queue)

				
	def programming_status (self, pass_val, fail_val, in_queue):
		pass_status = [1,1,1,1,1,1,1,1,1,1,1,1]
		fail_status = [1,1,1,1,1,1,1,1,1,1,1,1]
		pass_val = np.binary_repr(int(pass_val), width=12)	
		fail_val = np.binary_repr(int(fail_val), width=12)
		print(pass_val, fail_val)
		for i in range (0, 12):
			pass_status[i] = int(pass_val) % 10
			fail_status[i] = int(fail_val) % 10
			pass_val = int(pass_val) // 10
			fail_val = int(fail_val) // 10
		pass_status.reverse()
		fail_status.reverse()
		result = [pass_status, fail_status]
		print (result)
		in_queue.put(result)
		if (in_queue.qsize()):
			print ("qsize = ", in_queue.qsize())
		#return result

	''' clear buffer ''' 
	def clear_buffer(self):
		bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
		bus.flush_tx_buffer()
		

		
    
    
	
