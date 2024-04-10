import sys
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

        # self.DeviceSetup()
        self.button = QPushButton("Test button")

        self.tab1.layout = QVBoxLayout(self)
        self.tab1.layout.addWidget(self.button)
        self._bar = _Bar()
        self.tab1.layout.addWidget(self._bar)
        self._dial = QtWidgets.QDial()
        self.tab1.layout.addWidget(self._dial)
        self.tab1.setLayout(self.tab1.layout)
        self._dial.valueChanged.connect(self._bar._trigger_refresh)
        # self.tab1.setLayout(self.tab1.layout)

        self.layout.addWidget(self.tabs)
        
        
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

class _Bar(QtWidgets.QWidget):
    # pass
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )
    def _trigger_refresh(self):
        self.update()

    def sizeHint(self):
        return QtCore.QSize(40,120)

    def paintEvent(self, e):
        painter = QtGui.QPainter(self)

        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('green'))
        brush.setStyle(Qt.SolidPattern)
        rect = QtCore.QRect(0, 0, painter.device().width(), painter.device().height())
        painter.fillRect(rect, brush)

        # Get current state.
        # dial = self.parent()._dial
        # vmin, vmax = dial.minimum(), dial.maximum()
        # value = dial.value()

        vmin = 0
        vmax = 99
        value = 70

        padding = 5

        # Define our canvas.
        d_height = painter.device().height() - (padding * 2)
        d_width = painter.device().width() - (padding * 2)

        # Draw the bars.
        step_size = d_height / 5
        bar_height = step_size * 0.6
        bar_spacer = step_size * 0.4 / 2

        pc = (value - vmin) / (vmax - vmin)
        n_steps_to_draw = int(pc * 5)
        brush.setColor(QtGui.QColor('red'))
        # print (brush)
        for n in range(n_steps_to_draw):
            rect = QtCore.QRect(
                int(padding),
                int(padding + d_height - ((n+1) * step_size) + bar_spacer),
                int(d_width),
                int(bar_height)
            )
            painter.fillRect(rect, brush)

        painter.end()

# class Device(QtWidgets.QWidget):

#     def __init__(self, *args, **kwargs):
#         super(Device, self).__init__(*args, **kwargs)

#     def printDevice(self, id):
#         painter = QtGui.QPainter(self.label.pixmap())
#         pen = QtGui.QPen()
#         pen.setWidth(40)
#         pen.setColor(QtGui.QColor('red'))
#         painter.setPen(pen)
#         painter.drawPoint(200, 150)
#         painter.end()
       

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    win = App()
    # dev = Device()
    # dev.show()
    win.show()

    sys.exit(app.exec())