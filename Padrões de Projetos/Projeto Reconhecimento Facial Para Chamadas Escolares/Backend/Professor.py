from copy import deepcopy

class Professor():
    def __init__(self):
        self.nome = None
        self.matricula = None
        self.senha = None
        self.is_admin = False
        
    def clone(self):
        return deepcopy(self)
    
    def setNome(self, nome):
        self.nome = nome

    def setMatricula(self, matricula):
        self.matricula = matricula

    def setSenha(self, senha):
        self.senha = senha

    def setAdmin(self, is_admin):
        self.is_admin = is_admin

    def getAdmin(self):
        return self.is_admin   

    def getNome(self):
        return self.nome
        
    def getSenha(self):
        return self.senha

    def getMatricula(self):
        return self.matricula

    def obter_informacoes(self):
        return [self.nome, self.matricula]
