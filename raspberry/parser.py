from collections import namedtuple
import struct


motor_data = namedtuple('motor_data', ['id', 'acc', 'dec', 'dir', 'speed', 'step']) 
programmator = namedtuple('programmator', ['id', 'start', 'OK', 'error', 'n1', 'n2', 'n3', 'n4'])

format_string = '<BBBBHH'

def pack(list):
	packed_data = struct.pack(format_string, *list)
	return packed_data

def parse(data):
	if data[0] == 23:
		print ("motor")
	elif data[0] == 88:
		print ("move")
	elif data[0] == 89:
		print("run")
	elif data[0] == 99:
		print("stop")
	elif data[0] == 101:
		print ("programming")
	else:
		print ("unknown")
	#return 0
