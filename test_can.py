import time 
import can
from gpiozero import LED
import binascii

interface = 'socketcan'
channel = 'can0'

led = LED(21)

def producer(id):
    bus = can.Bus(channel=channel, interface=interface)
    for i in range(10):
        temp = binascii.unhexlify('4142434445464748')
        msg = can.Message(arbitration_id=0xc0ffee,
                          data=temp,
                          is_extended_id=False)
        bus.send(msg)
        led.on()
        time.sleep(1)     
        led.off()
        time.sleep(1)
        print ("send", i)
        
    time.sleep(1)
    
producer(10)
    
