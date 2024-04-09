import can
import time
import queue


interface = 'socketcan'
channel = 'can0'

def put_data(q):
    bus = can.ThreadSafeBus(channel=channel, interface=interface, bitrate = 125000)
    
    message = bus.recv(1)
    q.put(message)
    #for msg in bus:
        #q.put(msg.data)

    


    
    
