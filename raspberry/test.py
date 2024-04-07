import sys
import data_take as dt
import ui as ui

if __name__ == '__main__':
    
    dt.take_data()
    app = ui.QApplication(sys.argv)
    ex = ui.PyQtLayout()
    sys.exit(app.exec_())
