import can
import time


interface = 'socketcan'
channel = 'can0'



#bus = can.Bus(channel=channel, interface=interface)
#buffered_reader = can.BufferedReader()
#notifier = can.Notifier(bus, [buffered_reader])

'''def print_message (msg: can.Message) -> None:
    print (msg)'''

def put_data():
    bus = can.ThreadSafeBus(channel=channel, interface=interface, bitrate = 125000)
    time.sleep(1)
    for msg in bus:
        print ("data in: ", msg.data)
    
    #reader = can.BufferedReader()   
    #notifier = can.Notifier(bus, [reader])
    #q.put(reader.get_message())
    #print ("data in: ", reader.get_message())
    #time.sleep(1)
    
'''def get_data():
    if (q.empty() != True):
        temp = q.get_nowait()
        print (temp)
    
threading.Thread(target=put_data, daemon=True).start()


    
        
reader = can.AsyncBufferedReader()
    listeners: List[MessageRecipient] = [print_message, reader]
    
    loop = asyncio.get_running_loop()
    notifier = can.Notifier(bus, listeners, loop=loop)
    msg = await reader.get_message()'''
    #print (msg)
    
    
    
    #buffered_reader = can.BufferedReader()
    
    #notifier = can.Notifier(bus, [buffered_reader])
    
    #msg = bus.recv(None)
    
    #print (msg)
    #buffered_reader.on_message_received(msg)
    #notifier = can.Notifier(bus, [can.Printer()])
    #msg = bus.recv()
    
    #print ("data in: ", buffered_reader.get_message(timeout=0.1))

    
    
