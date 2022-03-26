from curses import window
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


class MyUI(QtWidgets.QMainWindow):
    
    def __init__(self, root):
        super(MyUI, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window =  MyUI(app)
    sys.exit(app.exec())

if __name__ == '__main__':
    main()