import test_ui9 as uiii
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == "__main__":
    app = uiii.QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = uiii.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    #dt.put_data()
    #self.thread()
    sys.exit(app.exec_())
    
'''ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(show()),
         ioloop.create_task(dt.put_data())]
ioloop.run_until_complete(asyncio.wait(tasks))
ioloop.close()'''
