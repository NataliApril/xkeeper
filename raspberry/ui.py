from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QHBoxLayout, QVBoxLayout, QGridLayout, 
                             QLabel, QGroupBox)
                             
import data_send as ds
                             
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()

    def click(self, _str):
        print ("Clicked")
        ds.producer(_str)
 
    def UI(self):
        
        '''speed control'''
        Label1 = QLabel("Speed:")
        Button_spd1 = QPushButton('+')
        Button_spd1.clicked.connect(lambda: self.click("spd_more"))
        Button_spd2 = QPushButton('-')   
        Button_spd2.clicked.connect(lambda: self.click("spd_less"))    

        '''direction control'''
        Label2 = QLabel("Direction:")
        Button_dir1 = QPushButton('CV')
        Button_dir1.clicked.connect(lambda: self.click('CV_dir'))
        Button_dir2 = QPushButton('CCV')
        Button_dir2.clicked.connect(lambda: self.click('CCV_dir'))     

        '''steps control'''
        Label3 = QLabel("Step:")
        Button_step1 = QPushButton('+')
        Button_step1.clicked.connect(lambda: self.click("stp_more"))
        Button_step2 = QPushButton('-')   
        Button_step2.clicked.connect(lambda: self.click("spd_less")) 
        
        '''UI''' 
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
