# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_12.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Devices = QtWidgets.QTabWidget(self.centralwidget)
        self.Devices.setGeometry(QtCore.QRect(10, 10, 781, 561))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Devices.setFont(font)
        self.Devices.setObjectName("Devices")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.select_version = QtWidgets.QComboBox(self.tab)
        self.select_version.setGeometry(QtCore.QRect(160, 10, 161, 31))
        self.select_version.setObjectName("select_version")
        self.select_version.addItem("")
        self.select_version.addItem("")
        self.select_version.addItem("")
        self.version = QtWidgets.QLabel(self.tab)
        self.version.setGeometry(QtCore.QRect(10, 20, 151, 20))
        self.version.setObjectName("version")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab)
        self.dateTimeEdit.setGeometry(QtCore.QRect(560, 10, 194, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(20, 70, 731, 411))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget1 = dev_example(self.widget)
        self.widget1.setObjectName("widget1")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.avr = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.avr.setStyleSheet("")
        self.avr.setObjectName("avr")
        self.verticalLayout.addWidget(self.avr, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.esp.setObjectName("esp")
        self.verticalLayout.addWidget(self.esp)
        self.gsm = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.gsm.setObjectName("gsm")
        self.verticalLayout.addWidget(self.gsm)
        self.gridLayout_5.addWidget(self.widget1, 0, 0, 1, 1)
        self.widget_2 = dev_example(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.avr_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.avr_2.setStyleSheet("")
        self.avr_2.setObjectName("avr_2")
        self.verticalLayout_2.addWidget(self.avr_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.esp_2.setObjectName("esp_2")
        self.verticalLayout_2.addWidget(self.esp_2)
        self.gsm_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.gsm_2.setObjectName("gsm_2")
        self.verticalLayout_2.addWidget(self.gsm_2)
        self.gridLayout_5.addWidget(self.widget_2, 0, 1, 1, 1)
        self.widget_3 = dev_example(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.widget_3)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.avr_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.avr_3.setStyleSheet("")
        self.avr_3.setObjectName("avr_3")
        self.verticalLayout_3.addWidget(self.avr_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.esp_3.setObjectName("esp_3")
        self.verticalLayout_3.addWidget(self.esp_3)
        self.gsm_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.gsm_3.setObjectName("gsm_3")
        self.verticalLayout_3.addWidget(self.gsm_3)
        self.gridLayout_5.addWidget(self.widget_3, 0, 2, 1, 1)
        self.widget_4 = dev_example(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.widget_4)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.avr_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.avr_4.setStyleSheet("")
        self.avr_4.setObjectName("avr_4")
        self.verticalLayout_4.addWidget(self.avr_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.esp_4.setObjectName("esp_4")
        self.verticalLayout_4.addWidget(self.esp_4)
        self.gsm_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.gsm_4.setObjectName("gsm_4")
        self.verticalLayout_4.addWidget(self.gsm_4)
        self.gridLayout_5.addWidget(self.widget_4, 0, 3, 1, 1)
        self.widget_5 = dev_example(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.widget_5)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.avr_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.avr_5.setStyleSheet("")
        self.avr_5.setObjectName("avr_5")
        self.verticalLayout_5.addWidget(self.avr_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.esp_5.setObjectName("esp_5")
        self.verticalLayout_5.addWidget(self.esp_5)
        self.gsm_5 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.gsm_5.setObjectName("gsm_5")
        self.verticalLayout_5.addWidget(self.gsm_5)
        self.gridLayout_5.addWidget(self.widget_5, 1, 0, 1, 1)
        self.widget_6 = dev_example(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.widget_6)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.avr_6 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.avr_6.setStyleSheet("")
        self.avr_6.setObjectName("avr_6")
        self.verticalLayout_6.addWidget(self.avr_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_6 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.esp_6.setObjectName("esp_6")
        self.verticalLayout_6.addWidget(self.esp_6)
        self.gsm_6 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.gsm_6.setObjectName("gsm_6")
        self.verticalLayout_6.addWidget(self.gsm_6)
        self.gridLayout_5.addWidget(self.widget_6, 1, 1, 1, 1)
        self.widget_7 = dev_example(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.widget_7)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.avr_7 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.avr_7.setStyleSheet("")
        self.avr_7.setObjectName("avr_7")
        self.verticalLayout_7.addWidget(self.avr_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_7 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.esp_7.setObjectName("esp_7")
        self.verticalLayout_7.addWidget(self.esp_7)
        self.gsm_7 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.gsm_7.setObjectName("gsm_7")
        self.verticalLayout_7.addWidget(self.gsm_7)
        self.gridLayout_5.addWidget(self.widget_7, 1, 2, 1, 1)
        self.widget_8 = dev_example(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.widget_8)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(0, 0, 169, 161))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.avr_8 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.avr_8.setStyleSheet("")
        self.avr_8.setObjectName("avr_8")
        self.verticalLayout_8.addWidget(self.avr_8, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.esp_8 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.esp_8.setObjectName("esp_8")
        self.verticalLayout_8.addWidget(self.esp_8)
        self.gsm_8 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        self.gsm_8.setObjectName("gsm_8")
        self.verticalLayout_8.addWidget(self.gsm_8)
        self.gridLayout_5.addWidget(self.widget_8, 1, 3, 1, 1)
        self.Devices.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.change_value = QtWidgets.QLabel(self.tab_2)
        self.change_value.setGeometry(QtCore.QRect(140, 10, 95, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.change_value.setFont(font)
        self.change_value.setToolTipDuration(5)
        self.change_value.setAlignment(QtCore.Qt.AlignCenter)
        self.change_value.setObjectName("change_value")
        self.current_value = QtWidgets.QLabel(self.tab_2)
        self.current_value.setGeometry(QtCore.QRect(520, 10, 95, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.current_value.setFont(font)
        self.current_value.setToolTipDuration(5)
        self.current_value.setAlignment(QtCore.Qt.AlignCenter)
        self.current_value.setObjectName("current_value")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 36, 751, 471))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.ACC = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ACC.setFont(font)
        self.ACC.setAlignment(QtCore.Qt.AlignCenter)
        self.ACC.setObjectName("ACC")
        self.gridLayout_2.addWidget(self.ACC, 0, 0, 1, 1)
        self.ACC_slider = QtWidgets.QSlider(self.layoutWidget)
        self.ACC_slider.setProperty("value", 25)
        self.ACC_slider.setOrientation(QtCore.Qt.Horizontal)
        self.ACC_slider.setObjectName("ACC_slider")
        self.gridLayout_2.addWidget(self.ACC_slider, 0, 1, 1, 2)
        self.DEC = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DEC.setFont(font)
        self.DEC.setAlignment(QtCore.Qt.AlignCenter)
        self.DEC.setObjectName("DEC")
        self.gridLayout_2.addWidget(self.DEC, 1, 0, 1, 1)
        self.DEC_slider = QtWidgets.QSlider(self.layoutWidget)
        self.DEC_slider.setProperty("value", 25)
        self.DEC_slider.setOrientation(QtCore.Qt.Horizontal)
        self.DEC_slider.setObjectName("DEC_slider")
        self.gridLayout_2.addWidget(self.DEC_slider, 1, 1, 1, 2)
        self.Speed = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Speed.setFont(font)
        self.Speed.setAlignment(QtCore.Qt.AlignCenter)
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
        self.Step.setAlignment(QtCore.Qt.AlignCenter)
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
        self.irection.setAlignment(QtCore.Qt.AlignCenter)
        self.irection.setObjectName("irection")
        self.gridLayout_2.addWidget(self.irection, 4, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_2.addWidget(self.radioButton, 4, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_2.addWidget(self.radioButton_2, 4, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        self.sendButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sendButton.setFont(font)
        self.sendButton.setObjectName("sendButton")
        self.gridLayout_3.addWidget(self.sendButton, 1, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.gridLayout_3.addWidget(self.startButton, 1, 1, 1, 1)
        self.startButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startButton_2.setFont(font)
        self.startButton_2.setObjectName("startButton_2")
        self.gridLayout_3.addWidget(self.startButton_2, 1, 2, 1, 1)
        self.stepButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.stepButton.setFont(font)
        self.stepButton.setObjectName("stepButton")
        self.gridLayout_3.addWidget(self.stepButton, 1, 3, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.acc_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.acc_val.setFont(font)
        self.acc_val.setAlignment(QtCore.Qt.AlignCenter)
        self.acc_val.setObjectName("acc_val")
        self.gridLayout.addWidget(self.acc_val, 0, 0, 1, 1)
        self.dec_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dec_val.setFont(font)
        self.dec_val.setAlignment(QtCore.Qt.AlignCenter)
        self.dec_val.setObjectName("dec_val")
        self.gridLayout.addWidget(self.dec_val, 1, 0, 1, 1)
        self.speed_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.speed_val.setFont(font)
        self.speed_val.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_val.setObjectName("speed_val")
        self.gridLayout.addWidget(self.speed_val, 2, 0, 1, 1)
        self.step_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.step_val.setFont(font)
        self.step_val.setAlignment(QtCore.Qt.AlignCenter)
        self.step_val.setObjectName("step_val")
        self.gridLayout.addWidget(self.step_val, 3, 0, 1, 1)
        self.direction_val = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.direction_val.setFont(font)
        self.direction_val.setAlignment(QtCore.Qt.AlignCenter)
        self.direction_val.setObjectName("direction_val")
        self.gridLayout.addWidget(self.direction_val, 4, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 2, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 4)
        self.programming = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.programming.setFont(font)
        self.programming.setObjectName("programming")
        self.gridLayout_4.addWidget(self.programming, 1, 0, 1, 1)
        self.started = QtWidgets.QLabel(self.layoutWidget)
        self.started.setAlignment(QtCore.Qt.AlignCenter)
        self.started.setObjectName("started")
        self.gridLayout_4.addWidget(self.started, 1, 1, 1, 1)
        self.sucsess = QtWidgets.QLabel(self.layoutWidget)
        self.sucsess.setAlignment(QtCore.Qt.AlignCenter)
        self.sucsess.setObjectName("sucsess")
        self.gridLayout_4.addWidget(self.sucsess, 1, 2, 1, 1)
        self.error = QtWidgets.QLabel(self.layoutWidget)
        self.error.setAlignment(QtCore.Qt.AlignCenter)
        self.error.setObjectName("error")
        self.gridLayout_4.addWidget(self.error, 1, 3, 1, 1)
        self.Devices.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Devices.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.select_version.setItemText(0, _translate("MainWindow", "V1"))
        self.select_version.setItemText(1, _translate("MainWindow", "V2"))
        self.select_version.setItemText(2, _translate("MainWindow", "V3"))
        self.version.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.version.setText(_translate("MainWindow", "Выбор прошивки:"))
        self.widget1.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp.setText(_translate("MainWindow", "ESP:"))
        self.gsm.setText(_translate("MainWindow", "GSM:"))
        self.widget_2.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_2.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_2.setText(_translate("MainWindow", "ESP:"))
        self.gsm_2.setText(_translate("MainWindow", "GSM:"))
        self.widget_3.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_3.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_3.setText(_translate("MainWindow", "ESP:"))
        self.gsm_3.setText(_translate("MainWindow", "GSM:"))
        self.widget_4.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_4.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_4.setText(_translate("MainWindow", "ESP:"))
        self.gsm_4.setText(_translate("MainWindow", "GSM:"))
        self.widget_5.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_5.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_5.setText(_translate("MainWindow", "ESP:"))
        self.gsm_5.setText(_translate("MainWindow", "GSM:"))
        self.widget_6.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_6.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_6.setText(_translate("MainWindow", "ESP:"))
        self.gsm_6.setText(_translate("MainWindow", "GSM:"))
        self.widget_7.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_7.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_7.setText(_translate("MainWindow", "ESP:"))
        self.gsm_7.setText(_translate("MainWindow", "GSM:"))
        self.widget_8.setToolTip(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.avr_8.setText(_translate("MainWindow", "AVR:                                    "))
        self.esp_8.setText(_translate("MainWindow", "ESP:"))
        self.gsm_8.setText(_translate("MainWindow", "GSM:"))
        self.Devices.setTabText(self.Devices.indexOf(self.tab), _translate("MainWindow", "Devices"))
        self.change_value.setText(_translate("MainWindow", "Change value"))
        self.current_value.setText(_translate("MainWindow", "Current value"))
        self.ACC.setText(_translate("MainWindow", "ACC"))
        self.DEC.setText(_translate("MainWindow", "DEC"))
        self.Speed.setText(_translate("MainWindow", "Speed"))
        self.Step.setText(_translate("MainWindow", "Step"))
        self.irection.setText(_translate("MainWindow", "Direction"))
        self.radioButton.setText(_translate("MainWindow", "CV"))
        self.radioButton_2.setText(_translate("MainWindow", "CCV"))
        self.sendButton.setText(_translate("MainWindow", "Send"))
        self.startButton.setText(_translate("MainWindow", "Start (Move)"))
        self.startButton_2.setText(_translate("MainWindow", "Start (Run)"))
        self.stepButton.setText(_translate("MainWindow", "Stop"))
        self.acc_val.setText(_translate("MainWindow", "ACC val:  0"))
        self.dec_val.setText(_translate("MainWindow", "DEC val:  0"))
        self.speed_val.setText(_translate("MainWindow", "Speed val:  0"))
        self.step_val.setText(_translate("MainWindow", "Step val:  0"))
        self.direction_val.setText(_translate("MainWindow", "Direction:  CV"))
        self.programming.setText(_translate("MainWindow", "Strat programming"))
        self.started.setText(_translate("MainWindow", "Started"))
        self.sucsess.setText(_translate("MainWindow", "Sucsess"))
        self.error.setText(_translate("MainWindow", "Error"))
        self.Devices.setTabText(self.Devices.indexOf(self.tab_2), _translate("MainWindow", "Service"))
from dev_example import dev_example


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())