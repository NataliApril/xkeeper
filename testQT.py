from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys
import time


def clickMethod():
    print ("Click")

app = QApplication([])
app.setStyle('Fusion')

win = QMainWindow()
win.setWindowTitle('Title')
win.setGeometry(400, 200, 1000, 600)

label = QLabel('text')
label.move(20, 0)

button = QPushButton('hello, world', win)
button.move(20,40)
'''button.clicked.connect(clickMethod())'''

win.show()

sys.exit(app.exec())
