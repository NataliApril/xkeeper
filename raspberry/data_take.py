import can
import asyncio
import queue

interface = 'socketcan'
channel = 'can0'

#bus = can.Bus(channel=channel, interface=interface)
#buffered_reader = can.BufferedReader()
#notifier = can.Notifier(bus, [buffered_reader])


def take_data():
    bus = can.Bus(channel=channel, interface=interface)
    notifier = can.Notifier(bus, [can.Printer()])
    if (can.BufferedReader() != None):
        #buffer = can.get_message()
        #print (buffer)
        #buffer = can.BufferedReader()
        #msg = buffer.get_message()s
        #print (msg)
        print ("Done!")
    else:
        print ("Error")
        
        
   
   
'''def rx_thread (self):
    msg = bus.recv(timeout=None)
    can.BufferedReader.on_message_received(msg)
    
    
def take_data(self):
    while True:
        try:
            msg = can.BufferedReader.get_message(self, timeout=0.5)
            buffered_reader.on_message_received(msg)
            print (msg)
        except queue.Empty:
            break
        
        
        
    msg = can.Message(arbitration_id = 0x0378, data=[0x00], is_extended_id=False)
    msg = buffer.on_message_received()
    print ("data in:", msg)
    return msg'''
    
    
    
    
    #async for msg in notof
    
    
