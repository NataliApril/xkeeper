import time 
import can
from gpiozero import LED

interface = 'socketcan'
channel = 'can0'

led = LED(21)

def producer(id):
    bus = can.Bus(channel=channel, interface=interface)
    for i in range(10):
        msg = can.Message(arbitration_id=0xc0ffee,
                          data= [id, i, 0, 1, 2, 3, 4, 5],
                          is_extended_id=False)
        '''bus.send(msg)
        led.on()
        time.sleep(1)     
        led.off()
        time.sleep(1)
        print ("send", i)'''
        
        notifier = can.Notifier(bus, [can.Printer()])
        
    time.sleep(1)
    
producer(10)