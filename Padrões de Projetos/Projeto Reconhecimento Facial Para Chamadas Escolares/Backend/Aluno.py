from copy import deepcopy

class Aluno:
    def __init__(self):
        self.nome = None
        self.matricula = None
        self.idCadeira = None
        self.foto = None

    def clone(self):
        return deepcopy(self)

    def setNome(self, nome):
        self.nome = nome

    def setMatricula(self, matricula):
        self.matricula = matricula

    def setCadeira(self, idCadeira):
        self.idCadeira = idCadeira

    def setFoto(self, foto):
        self.foto = foto

    def getNome(self):
        return self.nome

    def getMatricula(self):
        return self.matricula

    def getCadeira(self):
        return self.idCadeira

    def getFoto(self):
        return self.foto
    
    def obter_informacoes(self):
        return [self.getNome(),self.getMatricula(),self.getCadeira(),self.getFoto()]
