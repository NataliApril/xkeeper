from collections import namedtuple
import struct

motor_data = namedtuple('motor_data', ['id', 'acc', 'dec', 'dir', 'speed', 'step']) 
programmator = namedtuple('programmator', ['id', 'start', 'OK', 'error', 'n1', 'n2', 'n3', 'n4'])

motor_format_string = '<BBBBHH'
#program_format_string = '<BBBBBBBB'
#emergency_format_string = '<BBBBBBBB'

def pack(list):
	packed_data = struct.pack(motor_format_string, *list)
	return packed_data


def parse():
	
	return 0
