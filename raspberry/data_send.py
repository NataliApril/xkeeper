import time
import can
from gpiozero import LED
from collections import namedtuple
import struct

interface = 'socketcan'
channel = 'can0'

led = LED(21)

motor_data = namedtuple('motor_data', ['id', 'acc', 'dec', 'dir', 'speed', 'step']) 
programmator = namedtuple('programmator', ['id', 'start', 'OK', 'error', 'n1', 'n2', 'n3', 'n4'])

motor_format_string = '<BBBBHH'
program_format_string = 'BBBBBBBB'


def producer(msg):
    bus = can.Bus(channel=channel, interface=interface)
    
    if msg == "dir":
        print ("dir")
    elif msg == "step":
        print ("step")
    elif msg == "speed":
        print ("speed")
    else:
        print ("None")
    
    motor = [23, 10, 10, 0, 100, 100]
    packed_data = struct.pack(motor_format_string, *motor)
    print ("data:", packed_data)
    msg = can.Message(arbitration_id=0xc0ffee,
                      data=packed_data,
                      is_extended_id=False)
    bus.send(msg)
    led.on()
    time.sleep(0.1)     
    led.off()
    time.sleep(0.1)


    time.sleep(1)

