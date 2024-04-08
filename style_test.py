from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys
import time 
import can

app = QApplication([])
app.setStyle('Fusion')
palette = QPalette()
palette.setColor(QPalette.buttonText, Qt.red)
app.setPalette(palette)
button = QPushButton('Hello, world')
button.show()
app.exec()