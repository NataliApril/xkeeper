import sys
import data_take as dt
import ui as ui
import asyncio

if __name__ == '__main__':
    
    
    #dt.put_data()
    app = ui.QApplication(sys.argv)
    ex = ui.PyQtLayout()
    sys.exit(app.exec_())
