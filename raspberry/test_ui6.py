# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_8.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import data_send as ds

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Devices = QtWidgets.QTabWidget(self.centralwidget)
        self.Devices.setGeometry(QtCore.QRect(10, 0, 781, 551))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Devices.setFont(font)
        self.Devices.setObjectName("Devices")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Devices.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(2, 2, 761, 511))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ACC = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ACC.setFont(font)
        self.ACC.setObjectName("ACC")
        self.gridLayout_2.addWidget(self.ACC, 0, 0, 1, 1)
        self.ACC_slider = QtWidgets.QSlider(self.layoutWidget)
        self.ACC_slider.setProperty("value", 10)
        self.ACC_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ACC_slider.setObjectName("ACC_slider")
        self.gridLayout_2.addWidget(self.ACC_slider, 0, 1, 1, 2)
        self.DEC = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DEC.setFont(font)
        self.DEC.setObjectName("DEC")
        self.gridLayout_2.addWidget(self.DEC, 1, 0, 1, 1)
        self.DEC_slider = QtWidgets.QSlider(self.layoutWidget)
        self.DEC_slider.setProperty("value", 10)
        self.DEC_slider.setOrientation(QtCore.Qt.Horizontal)
        self.DEC_slider.setObjectName("DEC_slider")
        self.gridLayout_2.addWidget(self.DEC_slider, 1, 1, 1, 2)
        self.Speed = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Speed.setFont(font)
        self.Speed.setObjectName("Speed")
        self.gridLayout_2.addWidget(self.Speed, 2, 0, 1, 1)
        self.Speed_slider = QtWidgets.QSlider(self.layoutWidget)
        self.Speed_slider.setProperty("value", 25)
        self.Speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Speed_slider.setObjectName("Speed_slider")
        self.gridLayout_2.addWidget(self.Speed_slider, 2, 1, 1, 2)
        self.Step = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Step.setFont(font)
        self.Step.setObjectName("Step")
        self.gridLayout_2.addWidget(self.Step, 3, 0, 1, 1)
        self.Step_slider = QtWidgets.QSlider(self.layoutWidget)
        self.Step_slider.setProperty("value", 35)
        self.Step_slider.setOrientation(QtCore.Qt.Horizontal)
        self.Step_slider.setObjectName("Step_slider")
        self.gridLayout_2.addWidget(self.Step_slider, 3, 1, 1, 2)
        self.irection = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.irection.setFont(font)
        self.irection.setObjectName("irection")
        self.gridLayout_2.addWidget(self.irection, 4, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 4, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 4, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.current_value = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_value.setFont(font)
        self.current_value.setToolTipDuration(5)
        self.current_value.setObjectName("current_value")
        self.gridLayout.addWidget(self.current_value, 0, 0, 1, 1)
        self.acc_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_val.setFont(font)
        self.acc_val.setObjectName("acc_val")
        self.gridLayout.addWidget(self.acc_val, 1, 0, 1, 1)
        self.dec_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dec_val.setFont(font)
        self.dec_val.setObjectName("dec_val")
        self.gridLayout.addWidget(self.dec_val, 2, 0, 1, 1)
        self.speed_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speed_val.setFont(font)
        self.speed_val.setObjectName("speed_val")
        self.gridLayout.addWidget(self.speed_val, 3, 0, 1, 1)
        self.step_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.step_val.setFont(font)
        self.step_val.setObjectName("step_val")
        self.gridLayout.addWidget(self.step_val, 4, 0, 1, 1)
        self.direction_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.direction_val.setFont(font)
        self.direction_val.setObjectName("direction_val")
        self.gridLayout.addWidget(self.direction_val, 5, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 6, 0, 1, 1)
        self.stepButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stepButton.setFont(font)
        self.stepButton.setObjectName("stepButton")
        self.gridLayout.addWidget(self.stepButton, 7, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 1, 2, 1)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.gridLayout_4.addWidget(self.sendButton, 1, 0, 1, 1)
        self.Devices.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        value =  self.Speed_slider.value()
        self.speed_val.setText("Speed val: " + str(value))
        ds.motor[4] = value
        
        value =  self.Step_slider.value()
        self.step_val.setText("Step val: " + str(value))
        ds.motor[5] = value
        
        value =  self.ACC_slider.value()
        self.acc_val.setText("ACC val: " + str(value))
        ds.motor[1] = value
        
        value =  self.DEC_slider.value()
        self.dec_val.setText("DEC val: " + str(value))
        ds.motor[2] = value
        
        self.sendButton.clicked.connect(lambda: ds.producer("motor"))
        self.startButton.clicked.connect(lambda: ds.producer("start"))
        self.stepButton.clicked.connect(lambda: ds.producer("stop"))
        self.Step_slider.sliderMoved.connect(lambda: self.update_data("step"))
        self.Speed_slider.sliderMoved.connect(lambda: self.update_data("speed"))
        self.ACC_slider.sliderMoved.connect(lambda: self.update_data("acc"))
        self.DEC_slider.sliderMoved.connect(lambda: self.update_data("dec"))
        self.radioButton.clicked.connect(lambda: self.cheak_direction("CV"))
        self.radioButton_2.clicked.connect(lambda: self.cheak_direction("CCV"))
        
        if self.radioButton.isChecked():
            self.direction_val.setText("Direction: CV")
            ds.motor[3] = 0
        else:
            self.direction_val.setText("Direction: CCV")
            ds.motor[3] = 1
            
        self.retranslateUi(MainWindow)
        self.Devices.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Devices.setTabText(self.Devices.indexOf(self.tab), _translate("MainWindow", "Devices"))
        self.ACC.setText(_translate("MainWindow", "ACC"))
        self.DEC.setText(_translate("MainWindow", "DEC"))
        self.Speed.setText(_translate("MainWindow", "Speed"))
        self.Step.setText(_translate("MainWindow", "Step"))
        self.irection.setText(_translate("MainWindow", "Direction"))
        self.radioButton.setText(_translate("MainWindow", "CV"))
        self.radioButton_2.setText(_translate("MainWindow", "CCV"))
        self.current_value.setText(_translate("MainWindow", "Current value"))
        #self.acc_val.setText(_translate("MainWindow", "ACC val:  0"))
        #self.dec_val.setText(_translate("MainWindow", "DEC val:  0"))
        #self.speed_val.setText(_translate("MainWindow", "Speed val:  0"))
        #self.step_val.setText(_translate("MainWindow", "Step val:  0"))
        #self.direction_val.setText(_translate("MainWindow", "Direction:  CV"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stepButton.setText(_translate("MainWindow", "Stop"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.Devices.setTabText(self.Devices.indexOf(self.tab_2), _translate("MainWindow", "Service"))

    def update_data(self, _str):
        match _str:
            case "speed":
                value_spd =  self.Speed_slider.value()
                self.speed_val .setText("Speed val: " + str(value_spd))
                ds.motor[4] = value_spd
            case "step":
                value_stp =  self.Step_slider.value()
                self.step_val .setText("Step val: " + str(value_stp))
                ds.motor[5] = value_stp
            case "acc":
                value_acc = self.ACC_slider.value()
                self.acc_val.setText("ACC val: " + str(value_acc))
                ds.motor[1] = value_acc
            case "dec":
                value_dec = self.DEC_slider.value()
                self.dec_val.setText("DEC val: " + str(value_dec))
                ds.motor[2] = value_dec
                
    def cheak_direction(self, _str):
        match _str:
            case "CV":
                if self.radioButton.isChecked():
                    self.direction_val.setText("Direction: CV")
                    ds.motor[3] = 0
                                    
            case "CCV":
                if self.radioButton_2.isChecked():
                    self.direction_val.setText("Direction: CCV")
                    ds.motor[3] = 1

