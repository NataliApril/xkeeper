from collections import namedtuple
import struct

motor_data = namedtuple('motor_data', ['id', 'acc', 'dec', 'dir', 'speed', 'step']) 
programmator = namedtuple('programmator', ['id', 'start', 'OK', 'error', 'n1', 'n2', 'n3', 'n4'])

motor_format_string = '<BBBBHH'
#program_format_string = '<BBBBBBBB'
#emergency_format_string = '<BBBBBBBB'

def pack(list):
	match list[0]:
		case 23:
			packed_data = struct.pack(motor_format_string, *list)
		'''case 34:
			packed_data = struct.pack(program_format_string, *list)
		case 99:
			packed_data = struct.pack(emergency_format_string, *list)
		case _:
			print ("unknown")
			packed_data = [0, 0, 0, 0, 0, 0, 0, 0]'''
	return packed_data


def parse():
	
	return 0
