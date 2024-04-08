import time
import can
from gpiozero import LED
import parser as ps

interface = 'socketcan'
channel = 'can0'

led = LED(21)

motor = [23, 10, 10, 0, 0, 0]  
        
def producer():
    bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
    
    packed_data = ps.pack(motor)
    print ("data out:", packed_data)
    msg = can.Message(arbitration_id=0xc0ffee,
                      data=packed_data,
                      is_extended_id=False)
    bus.send(msg)
    '''led.on()
    time.sleep(0.1)     
    led.off()
    time.sleep(0.1)
    time.sleep(1)'''

