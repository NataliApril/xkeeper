from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QMainWindow, QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Device cheak:'
        self.left = 0
        self.top = 0
        self.width = 1000
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = ServiceList(self)
        self.setCentralWidget(self.table_widget)


        

class ServiceList(QWidget):
    
    def __init__(self, *args, **kwargs):
        super(QWidget, self).__init__(*args, **kwargs)
        self.layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        self.TableServiceList()
        self.tabs.addTab(self.tab1,"Devices")
        self.tabs.addTab(self.tab2,"Service")
        self.tab2.layout = QVBoxLayout(self)
        self.tab2.layout.addWidget(self.ServiceList)
        self.tab2.setLayout(self.tab2.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        
    def TableServiceList(self):
        self.ServiceList = QGroupBox()
        self.SpeedStatus()
        self.DirectionStatus()
        self.StepStatus()
        ServiceTab = QVBoxLayout()
        ServiceTab.addWidget(self.Step)
        ServiceTab.addWidget(self.Direction)
        ServiceTab.addWidget(self.Speed)
        self.ServiceList.setLayout(ServiceTab)

    def SpeedStatus(self):
        self.Speed = QGroupBox()
        speed = QLabel("Speed")
        button_more = QPushButton("+")
        button_less = QPushButton("-")
        curr_val = QLabel(f'Current value: {100}')
        layout_spd = QHBoxLayout()
        layout_spd.addWidget(speed)
        layout_spd.addWidget(button_less)
        layout_spd.addWidget(button_more)
        layout_spd.addWidget(curr_val)
        self.Speed.setLayout(layout_spd)

    def DirectionStatus(self):
        self.Direction = QGroupBox()
        direction = QLabel("Direction")
        button_CV = QPushButton("CV")
        button_CCV = QPushButton("CCV")
        curr_val_dir = QLabel(f'Current value: CV')
        layout_dir = QHBoxLayout()
        layout_dir.addWidget(direction)
        layout_dir.addWidget(button_CCV)
        layout_dir.addWidget(button_CV)
        layout_dir.addWidget(curr_val_dir)
        self.Direction.setLayout(layout_dir)

    def StepStatus(self):
        self.Step = QGroupBox()
        step = QLabel("Step")
        button_stp_more = QPushButton("+")
        button_stp_less = QPushButton("-")
        curr_stp_val = QLabel(f'Current value: {100}')
        layout_stp = QHBoxLayout()
        layout_stp.addWidget(step)
        layout_stp.addWidget(button_stp_more)
        layout_stp.addWidget(button_stp_less)
        layout_stp.addWidget(curr_stp_val)
        self.Step.setLayout(layout_stp)

class Device(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(Device, self).__init__(*args, **kwargs)

    def printDevice(self, id):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setWidth(40)
        pen.setColor(QtGui.QColor('red'))
        painter.setPen(pen)
        painter.drawPoint(200, 150)
        painter.end()
       

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    win = App()
    win.show()

    sys.exit(app.exec())