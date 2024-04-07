import can
import asyncio

interface = 'socketcan'
channel = 'can0'

def take_data():
    bus = can.Bus(channel=channel, interface=interface)
    notifier = can.Notifier(bus, [can.Printer()])
    if (can.BufferedReader() != None):
        #buffer = can.BufferedReader.on_message_received()
        #buffer = can.BufferedReader()
        #msg = buffer.get_message()
        #print (msg)
        print ("Done!")
    else:
        print ("Error")
    
    
    #async for msg in notof
    
    
