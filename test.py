import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, 
                             QHBoxLayout, QVBoxLayout, QGridLayout, QLabel)
 
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
        '''speed control'''
        Label1 = QLabel("Speed:")
        Button_spd1 = QPushButton('+')
        Button_spd2 = QPushButton('-')       
        vbox_1 = QVBoxLayout()
        vbox_1.addWidget(Label1)
        vbox_1.addWidget(Button_spd1)
        vbox_1.addWidget(Button_spd2)

        '''direction control'''
        Label2 = QLabel("Direction:")
        Button_dir1 = QPushButton('+')
        Button_dir2 = QPushButton('-')     
        vbox_2 = QVBoxLayout()
        vbox_2.addWidget(Label2)
        vbox_2.addWidget(Button_dir1)
        vbox_2.addWidget(Button_dir2)

        '''steps control'''
        Label3 = QLabel("Step:")
        Button_step1 = QPushButton('+')
        Button_step2 = QPushButton('-')     
        vbox_3 = QVBoxLayout()
        vbox_3.addWidget(Label3)
        vbox_3.addWidget(Button_step1)
        vbox_3.addWidget(Button_step2)
 
        self.setLayout(vbox_1 | vbox_2 | vbox_3)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyQt5 Layout')
        self.show()
 
def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()