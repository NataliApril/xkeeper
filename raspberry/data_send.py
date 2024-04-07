import time
import can
from gpiozero import LED
import parser as ps

interface = 'socketcan'
channel = 'can0'

led = LED(21)


motor = [23, 10, 10, 0, 10, 10]
program = [34, 0, 0, 0, 0, 0, 0, 0]
emergency = [99, 0, 0, 0, 0, 0, 0, 0]

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
                
def direction(_str):
        if _str == "CV":
            motor[3] = 0
        elif _str == "CCV":
            motor[3] = 1
            
def step(_str, val):
        if _str == "+":
            if (0 <= motor[5] < 65535):
                motor[5] += val
            else:
                motor[5] += 0
        elif _str == "-":
            if (0 < motor[5] <= 65535):
                motor[5] -= val
            else:
                motor[5] -= 0
        
        
def producer(_str):
    bus = can.Bus(channel=channel, interface=interface)
    
    match _str:
        case "CV_dir":
            print ("CV")
            #change direction
            direction("CV")
            packed_data = ps.pack(motor)
            
        case "CCV_dir":
            print ("CCV")
            #change direction
            direction("CCV")
            packed_data = ps.pack(motor)
            
        case "spd_more":
            print ("SPD +")
            #add speed
            speed("+", 10)
            packed_data = ps.pack(motor)
            
        case "spd_less":
            print ("SPD -")
            #minus speed
            speed("-", 10)
            packed_data = ps.pack(motor)
            
        case "stp_more":
            print ("STEP +")
            #add step
            step("+", 10)
            packed_data = ps.pack(motor)
            
        case "stp_less":
            print ("STEP -")
            #minus step
            step("-", 10)
            packed_data = ps.pack(motor)
            
        case "boot":
            print ("Boot")
            #boot program
            packed_data = ps.pack(program)
            
        case "stop":
            print ("Stop")
            #stop motor
            packed_data = ps.pack(emergency)
            
        case _:
            print ("None")
    
    
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

