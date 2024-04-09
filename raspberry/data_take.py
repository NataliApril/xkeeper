import can
import time
import queue


interface = 'socketcan'
channel = 'can0'

def print_data(msg):
    print ("data in:", msg.data)
    
def put_data(q):
    bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
    message = bus.recv()
    q.put(message.data)
    print ("size: ", q.qsize())
    print ("data: ", message.data)
    q.get()

def take():
    bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
    reader = can.BufferedReader()
    bus_notifier = can.Notifier(bus, [reader]) 
    messages = []
    msg = reader.get_message(1)
    if msg is None:
        #break
        print("None")
    messages.append(msg)
    print ("data in take: ", msg.data)
    
    


    
    
