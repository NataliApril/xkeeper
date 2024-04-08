from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.originalPalette = QApplication.palette() 
        self.setWindowTitle("Device Cheak:")
        self.setGeometry(400, 200, 1000, 600)

        self.SpeedStatus()
        self.DirectionStatus()
        self.StepStatus()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.Step)
        mainLayout.addWidget(self.Direction)
        mainLayout.addWidget(self.Speed)
        # mainLayout.rowCount(3)
        # mainLayout.setRowStretch(3, 1)
        # mainLayout.setColumnStretch(0, 1)
        # mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)
        
        
    
        # self.Speed = QTabWidget()
        # self.Speed.setSizePolicy(QSizePolicy.Policy.Preferred,
        #         QSizePolicy.Policy.Ignored)

        # tab1 = QWidget()
        # tableWidget1 = QTableWidget(2, 4)
        # tableWidget2 = QLabel("Test")

        # tab1grid = QGridLayout()
        # tab1grid.setContentsMargins(5, 5, 5, 5)
        # tab1grid.addWidget(tableWidget1)
        # tab1grid.addWidget(tableWidget1)
        # tab1grid.addWidget(tableWidget2)
        # tab1.setLayout(tab1grid)

        # self.Speed.addTab(tab1, "Devices")
        # self.Speed.addTab(tab2, "Service")

    def SpeedStatus(self):
        self.Speed = QGroupBox()
        speed = QLabel("Speed")
        button_more = QPushButton("+")
        button_less = QPushButton("-")
        curr_val = QLabel(f'Current value: {100}')
        layout_spd = QHBoxLayout()
        # layout_spd.setContentsMargins(5, 5, 5, 5)
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
        # layout_dir.setContentsMargins(5, 5, 5, 5)
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
        # layout_stp.setContentsMargins(5, 5, 5, 5)
        layout_stp.addWidget(step)
        layout_stp.addWidget(button_stp_more)
        layout_stp.addWidget(button_stp_less)
        layout_stp.addWidget(curr_stp_val)
        self.Step.setLayout(layout_stp)



class DeviceCheak():
    def __init__(self):
        super().__init__()
        self.vision()

    def vision(self):

        button = QPushButton('test')
        # self.bottomLeftTabWidget = QTabWidget()
        # self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Policy.Preferred,
        #         QSizePolicy.Policy.Ignored)

        # tab1 = QWidget()
        # tableWidget = QTableWidget(10, 10)

        # tab1hbox = QHBoxLayout()
        # tab1hbox.setContentsMargins(5, 5, 5, 5)
        # tab1hbox.addWidget(tableWidget)
        # tab1.setLayout(tab1hbox)

        # tab2 = QWidget()
        # textEdit = QTextEdit()

        # textEdit.setPlainText("Twinkle, twinkle, little star,\n"
        #                         "How I wonder what you are.\n" 
        #                         "Up above the world so high,\n"
        #                         "Like a diamond in the sky.\n"
        #                         "Twinkle, twinkle, little star,\n" 
        #                         "How I wonder what you are!\n")

        # tab2hbox = QHBoxLayout()
        # tab2hbox.setContentsMargins(5, 5, 5, 5)
        # tab2hbox.addWidget(textEdit)
        # tab2.setLayout(tab2hbox)

        # self.bottomLeftTabWidget.addTab(tab1, "&Table")
        # self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")
        
    
    

    # def vision(self):
    #     mainLayout = QGridLayout()
    #     mainLayout.addWidget(self.DeviceStatus(100), 0, 1)



    # def DeviceStatus(val):
    #     speed = QLabel(f'Speed {val}')

    #     slider = QSlider(Qt.Orientation.Horizontal)
    #     slider.setValue(40)
        

  

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        styleLabel = QLabel("&Style:")
        # styleLabel.setBuddy(styleComboBox)

        self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
        self.useStylePaletteCheckBox.setChecked(True)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()
        '''self.createProgressBar()'''

        # styleComboBox.textActivated.connect(self.changeStyle)
        # self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

        topLayout = QHBoxLayout()
        topLayout.addWidget(styleLabel)
        topLayout.addWidget(styleComboBox)
        topLayout.addStretch(1)
        topLayout.addWidget(self.useStylePaletteCheckBox)
        topLayout.addWidget(disableWidgetsCheckBox)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 1)
        mainLayout.addWidget(self.topLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        '''mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)'''
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

        self.setWindowTitle("Styles")
        # self.changeStyle('Windows')

    # def changeStyle(self, styleName):
    #     QApplication.setStyle(QStyleFactory.create(styleName))
    #     self.changePalette()

    # def changePalette(self):
    #     if (self.useStylePaletteCheckBox.isChecked()):
    #         QApplication.setPalette(QApplication.style().standardPalette())
    #     else:
    #         QApplication.setPalette(self.originalPalette)

    # def advanceProgressBar(self):
    #     curVal = self.progressBar.value()
    #     maxVal = self.progressBar.maximum()
    #     self.progressBar.setValue(curVal + (maxVal - curVal) // 100)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Group 1")

        radioButton1 = QRadioButton("Radio button 1")
        radioButton2 = QRadioButton("Radio button 2")
        radioButton3 = QRadioButton("Radio button 3")
        radioButton1.setChecked(True)

        checkBox = QCheckBox("Tri-state check box")
        checkBox.setTristate(True)
        checkBox.setCheckState(Qt.CheckState.PartiallyChecked)

        layout = QVBoxLayout()
        layout.addWidget(radioButton1)
        layout.addWidget(radioButton2)
        layout.addWidget(radioButton3)
        layout.addWidget(checkBox)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Group 2")

        defaultPushButton = QPushButton("Default Push Button")
        defaultPushButton.setDefault(True)

        togglePushButton = QPushButton("Toggle Push Button")
        togglePushButton.setCheckable(True)
        togglePushButton.setChecked(True)

        flatPushButton = QPushButton("Flat Push Button")
        flatPushButton.setFlat(True)

        layout = QVBoxLayout()
        layout.addWidget(defaultPushButton)
        layout.addWidget(togglePushButton)
        layout.addWidget(flatPushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(10, 10)

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        tab2 = QWidget()
        textEdit = QTextEdit()

        textEdit.setPlainText("Twinkle, twinkle, little star,\n"
                              "How I wonder what you are.\n" 
                              "Up above the world so high,\n"
                              "Like a diamond in the sky.\n"
                              "Twinkle, twinkle, little star,\n" 
                              "How I wonder what you are!\n")

        tab2hbox = QHBoxLayout()
        tab2hbox.setContentsMargins(5, 5, 5, 5)
        tab2hbox.addWidget(textEdit)
        tab2.setLayout(tab2hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")
        self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Group 3")
        self.bottomRightGroupBox.setCheckable(True)
        self.bottomRightGroupBox.setChecked(True)

        # lineEdit = QLineEdit('s3cRe7')
        # lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        # spinBox = QSpinBox(self.bottomRightGroupBox)
        # spinBox.setValue(50)

        # dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
        # dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        # slider = QSlider(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
        # slider.setValue(40)

        # scrollBar = QScrollBar(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
        # scrollBar.setValue(60)

        # dial = QDial(self.bottomRightGroupBox)
        # dial.setValue(30)
        # dial.setNotchesVisible(True)

        # layout = QGridLayout()
        # layout.addWidget(lineEdit, 0, 0, 1, 2)
        # layout.addWidget(spinBox, 1, 0, 1, 2)
        # layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
        # layout.addWidget(slider, 3, 0)
        # layout.addWidget(scrollBar, 4, 0)
        # layout.addWidget(dial, 3, 1, 2, 1)
        # layout.setRowStretch(5, 1)
        # self.bottomRightGroupBox.setLayout(layout)

    '''def createProgressBar(self):
        self.progressBar = QProgressBar()
        self.progressBar.setRange(0, 10000)
        self.progressBar.setValue(0)

        timer = QTimer(self)
        timer.timeout.connect(self.advanceProgressBar)
        timer.start(1000)'''


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    win = Window()
    win.show()
    # gallery = WidgetGallery()
    # gallery.show()
    sys.exit(app.exec())