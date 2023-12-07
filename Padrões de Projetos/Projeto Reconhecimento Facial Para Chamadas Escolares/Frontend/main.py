import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_Login
from cadastrar_turma import SecondWindow

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    window1 = Ui_Login()
    window1.setupUi(Login)
    
    window1.show()
    
    
    window2 = SecondWindow()
    window2.show()

    sys.exit(app.exec_())



