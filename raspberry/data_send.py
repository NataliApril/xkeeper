import time
import can
from gpiozero import LED
import parser as ps

interface = 'socketcan'
channel = 'can0'

led = LED(21)


motor = [23, 10, 10, 0, 100, 100]
program = [34, 10, 10, 0, 100, 100, 0, 0]

def speed(_str, val):
        if _str == "+":
            if (0 <= motor[4] < 65535):
                motor[4] += val
            else:
                motor[4] += 0
        elif _str == "-":
            if (0 < motor[4] <= 65535):
                motor[4] -= val
            else:
                motor[4] -= 0
        
    
def producer(_str):
    bus = can.Bus(channel=channel, interface=interface)
    
    match _str:
        case "CV_dir":
            print ("CV")
            #change direction
            motor[3] = 0
            packed_data = ps.parse(motor)
            
        case "CCV_dir":
            print ("CCV")
            #change direction
            motor[3] = 1
            packed_data = ps.parse(motor)
            
        case "spd_more":
            print ("SPD +")
            #add speed
            speed("+", 100)
            packed_data = ps.parse(motor)
            
        case "spd_less":
            print ("SPD -")
            #minus speed
            speed("-", 100)
            packed_data = ps.parse(motor)
            
        case "stp_more":
            print ("STEP +")
            
        case "stp_less":
            print ("STEP -")
            
        case _:
            print ("None")
    
    
    print ("data:", packed_data)
    msg = can.Message(arbitration_id=0xc0ffee,
                      data=packed_data,
                      is_extended_id=False)
    bus.send(msg)
    led.on()
    time.sleep(0.1)     
    led.off()
    time.sleep(0.1)


    time.sleep(1)

