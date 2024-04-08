from collections import namedtuple
import struct

motor_data = namedtuple('motor_data', ['id', 'acc', 'dec', 'dir', 'speed', 'step']) 
programmator = namedtuple('programmator', ['id', 'start', 'OK', 'error', 'n1', 'n2', 'n3', 'n4'])

format_string = '<BBBBHH'

def pack(list):
	packed_data = struct.pack(format_string, *list)
	return packed_data

def parse():
	
	return 0
