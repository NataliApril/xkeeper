import time
import can
from gpiozero import LED
import parser as ps

interface = 'socketcan'
channel = 'can0'

led = LED(21)

motor = [23, 10, 10, 0, 0, 0] 
start = [89, 0, 0, 0, 0, 0] 
stop = [99, 0, 0, 0, 0, 0]
        
def producer(_str):
    bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
    match _str:
        case "motor":
            packed_data = ps.pack(motor)
        case "start":
            packed_data = ps.pack(start)
        case "stop":
            packed_data = ps.pack(stop)
            
    print ("data out:", packed_data)
    msg = can.Message(arbitration_id=0xc0ffee,
                      data=packed_data,
                      is_extended_id=False)
    bus.send(msg)

