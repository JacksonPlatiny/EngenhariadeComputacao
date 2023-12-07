# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login_certo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import typing
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget

    


class Ui_Login(object):
    
    def checkFields(self):
        textUser = ""
        textSenha = ""

        def showMessage(message):
                self.frame_error.show()
                self.label_error.setText(message)

        #CHECK USUARIO
        if not self.lineEdit_user.text():
            textUser = "Matricula vazia"
        else:
            textUser = ""

        #CHECK SENHA
        if not self.lineEdit_senha.text():
            textSenha= " Senha vazia"
        else: textSenha = ""

        #CHECK FIELDS
        if textUser + textSenha != '':
            text= textUser + textSenha
            
        else:
            text = "Login Ok"
        
        
        showMessage(text)


    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(1280, 740)
        Login.setMinimumSize(QtCore.QSize(1280, 740))
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_botton = QtWidgets.QFrame(self.centralwidget)
        self.top_botton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.top_botton.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.top_botton.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_botton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_botton.setObjectName("top_botton")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.top_botton)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_error = QtWidgets.QFrame(self.top_botton)
        self.frame_error.setMinimumSize(QtCore.QSize(1000, 0))
        self.frame_error.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_error.setStyleSheet("background-color: rgb(255, 66, 53);\n"
"border-radius: 5px;\n"
"")
        self.frame_error.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_error.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error.setObjectName("frame_error")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_error = QtWidgets.QLabel(self.frame_error)
        self.label_error.setMinimumSize(QtCore.QSize(0, 0))
        self.label_error.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error.setObjectName("label_error")
        self.horizontalLayout_3.addWidget(self.label_error)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_error)
        self.pushButton_close.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_close.setStyleSheet("QPushButton{\n"
"    \n"
"    background-image: url(:/close/cil-x.png);\n"
"    border-radius: 5px;\n"
"    background-position:center;\n"
"    background-color: rgb(255, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(50, 50, 50, 50);\n"
"    \n"
"    color: rgba(200, 200, 200, 200);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: rgba(35, 35, 35, 35);\n"
"    \n"
"    color: rgba(200, 200, 200, 200);\n"
"}\n"
"")
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_3.addWidget(self.pushButton_close)
        self.horizontalLayout_2.addWidget(self.frame_error)
        self.verticalLayout.addWidget(self.top_botton)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("\n"
"background-color: rgb(51, 51, 51);")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QFrame(self.content)
        self.login.setMinimumSize(QtCore.QSize(1000, 566))
        self.login.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.login.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.login.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        self.logo = QtWidgets.QFrame(self.login)
        self.logo.setGeometry(QtCore.QRect(40, 110, 391, 401))
        self.logo.setStyleSheet("background-image: url(:/logo/teste.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.lineEdit_user = QtWidgets.QLineEdit(self.login)
        self.lineEdit_user.setGeometry(QtCore.QRect(510, 240, 320, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_user.setFont(font)
        self.lineEdit_user.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_user.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45,45)\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30,30,30,30);\n"
"    rgba(100, 100, 100, 100)\n"
"\n"
"}\n"
"\n"
"")
        self.lineEdit_user.setObjectName("lineEdit_user")
        self.lineEdit_senha = QtWidgets.QLineEdit(self.login)
        self.lineEdit_senha.setGeometry(QtCore.QRect(510, 290, 320, 45))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_senha.setFont(font)
        self.lineEdit_senha.setStyleSheet("QLineEdit{\n"
"    border: 2px solid rgb(45,45,45,45)\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    background-color: rgb(30,30,30,30);\n"
"    rgba(100, 100, 100, 100)\n"
"\n"
"}\n"
"\n"
"")
        self.lineEdit_senha.setMaxLength(16)
        self.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_senha.setObjectName("lineEdit_senha")
        self.pushButton_entrar = QtWidgets.QPushButton(self.login)
        self.pushButton_entrar.setGeometry(QtCore.QRect(510, 370, 320, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_entrar.setFont(font)
        self.pushButton_entrar.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(51, 51, 51);\n"
"    border: 2px solid rgb(60,60,60);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60,60,60);\n"
"    border: 2px solid rgb(70,70,70);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(120,120,120);\n"
"    border: 2px solid rgb(90,90,90);\n"
"}\n"
"")
        self.pushButton_entrar.setObjectName("pushButton_entrar")
        self.label = QtWidgets.QLabel(self.login)
        self.label.setGeometry(QtCore.QRect(630, 120, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.login)
        self.label_2.setGeometry(QtCore.QRect(620, 160, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_CriarConta = QtWidgets.QPushButton(self.login)
        self.pushButton_CriarConta.setGeometry(QtCore.QRect(510, 440, 320, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_CriarConta.setFont(font)
        self.pushButton_CriarConta.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(120,120,120);\n"
"    border: 2px solid rgb(100,100,100);\n"
"    border-radius: 5px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(51, 51, 51);\n"
"    border: 2px solid rgb(60,60,60);\n"
"}\n"
"")
        self.pushButton_CriarConta.setObjectName("pushButton_CriarConta")
        self.horizontalLayout.addWidget(self.login)
        self.verticalLayout.addWidget(self.content)
        self.botton = QtWidgets.QFrame(self.centralwidget)
        self.botton.setMaximumSize(QtCore.QSize(16777215, 35))
        self.botton.setStyleSheet("background-color: rgb(51, 51, 51);")
        self.botton.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.botton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botton.setObjectName("botton")
        self.verticalLayout.addWidget(self.botton)
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        
    def teste(self):
        #super().__init__()
        #self.setWindowTitle("Main Window")
        self.pushButton_entrar.clicked.connect(lambda: self.open_second_window())
        self.pushButton_entrar.clicked.connect(self.checkFields)

    def open_second_window(self):
        second_window = QMainWindow()
        second_window.show()




        #Fechar Pop-up
        self.pushButton_close.clicked.connect(lambda: self.frame_error.hide())

        #hide error
        self.frame_error.hide()

        #Chamada erros Login
        self.pushButton_entrar.clicked.connect(self.checkFields)



    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label_error.setText(_translate("Login", "ERROR"))
        self.lineEdit_user.setPlaceholderText(_translate("Login", "Matrícula"))
        self.lineEdit_senha.setPlaceholderText(_translate("Login", "Senha"))
        self.pushButton_entrar.setText(_translate("Login", "Entrar"))
        self.label.setText(_translate("Login", "Login"))
        self.label_2.setText(_translate("Login", "Entre na sua conta"))
        self.pushButton_CriarConta.setText(_translate("Login", "Criar uma conta"))
import files


'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())'''
