import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QHBoxLayout, QVBoxLayout, QGridLayout, 
                             QLabel, QGroupBox)
import time 
import can
from gpiozero import LED
import binascii

interface = 'socketcan'
channel = 'can0'

led = LED(21)
 
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()

    def click(self):
        print ("Clicked")
        producer(1)
 
    def UI(self):
        
        '''speed control'''
        Label1 = QLabel("Speed:")
        Button_spd1 = QPushButton('+')
        Button_spd2 = QPushButton('-')       

        '''direction control'''
        Label2 = QLabel("Direction:")
        Button_dir1 = QPushButton('CV')
        Button_dir1.clicked.connect(self.click)
        Button_dir2 = QPushButton('CCV')
        Button_dir2.clicked.connect(self.click)     

        '''steps control'''
        Label3 = QLabel("Step:")
        Button_step1 = QPushButton('+')
        Button_step2 = QPushButton('-')     
        widget = QGridLayout()
        widget.addWidget(Label1, 0, 0)
        widget.addWidget(Button_spd1, 0, 1)
        widget.addWidget(Button_spd2, 0, 2)
        widget.addWidget(Label2, 1, 0)
        widget.addWidget(Button_dir1, 1, 1)
        widget.addWidget(Button_dir2, 1, 2)
        widget.addWidget(Label3, 2, 0)
        widget.addWidget(Button_step1, 2, 1)
        widget.addWidget(Button_step2, 2, 2)
        self.setLayout(widget)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Device control:')
        self.show()
 

def producer(id):
    bus = can.Bus(channel=channel, interface=interface)
    for i in range(1):
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
    
def take_data():
    bus = can.Bus(channel=channel, interface=interface)
    notifier = can.Notifier(bus, [can.Printer()])
    
 
if __name__ == '__main__':
    
    take_data()
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())