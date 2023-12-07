from Classes.fachada import Menu
from PyQt5 import QtCore, QtGui, QtWidgets

class Login:
    def __init__(self):
        self.sistema = Menu()
        self.matricula = None
        self.logado = False
        self.admin = False
        
        self.app = QtWidgets.QApplication([])
        self.ui = Ui_Login()
        self.ui.setupUi()
        self.ui.pushButton_entrar.clicked.connect(self.fazer_login)
        self.ui.pushButton_CriarConta.clicked.connect(self.cadastro)
        
    def pre_cadastro(self):
        if self.logado and self.admin:
            self.sistema.pre_cadastro()
            
    def cadastro(self):
        self.sistema.cadastro()
            
    def fazer_login(self):
        matricula = self.ui.lineEdit_user.text()
        senha = self.ui.lineEdit_senha.text()
        verificado = self.sistema.verifica_login(matricula, senha)
        if verificado[0]:
            self.logado = True
            self.matricula = matricula
            self.ui.showMessage("Logado com Sucesso")
        if verificado[1]:
            self.admin = True
            self.ui.showMessage("Logado como admin")
        self.ui.lineEdit_user.clear()
        self.ui.lineEdit_senha.clear()
        
    def deslogar(self):
        self.logado = False
        self.admin = False
        self.matricula = None
        self.ui.showMessage("Deslogado com Sucesso.")
        
    def cadastrar_cadeira(self):
        if self.logado:
            self.sistema.cadastro_cadeira()
            
    def cadastrar_aluno(self):
        if self.logado:
            self.sistema.cadastro_aluno()
            
    def registrar_aula(self):
        if self.logado:
            self.sistema.registro_de_aula()

    def start(self):
        self.ui.show()
        self.app.exec_()

class Ui_Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def showMessage(self, message):
        self.frame_error.show()
        self.label_error.setText(message)
        
    def setupUi(self):
        self.setObjectName("Login")
        self.resize(1280, 740)
        self.setMinimumSize(QtCore.QSize(1280, 740))
        self.centralwidget = QtWidgets.QWidget(self)
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
"border-radius: 5px;\n.
