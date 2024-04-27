import can
import time
import queue
import parser as pars


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
    pars.parse(q.get())

def take(q):
    bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
    reader = can.BufferedReader()
    bus_notifier = can.Notifier(bus, [reader]) 
    msg = reader.get_message(1)
    if msg is not None:
        q.put(msg.data)
        #print ("size: ", q.qsize())
        pars.parse(q.get())
        #print ("size: ", q.qsize())
    #else:
        #print("None")
        
def clear_buffer():
    bus = can.Bus(channel=channel, interface=interface, bitrate = 125000)
    bus.flush_tx_buffer()
    
    
    


    
    
