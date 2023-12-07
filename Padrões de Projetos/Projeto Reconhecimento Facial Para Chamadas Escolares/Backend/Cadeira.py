from copy import deepcopy

class Cadeira():
    def __init__(self):
        self.codigo = None
        self.idProfessor = None
        self.nome = None
        self.semestre = None
      
    def clone(self):
        return deepcopy(self)

    def setCodigo(self, codigo):
        self.codigo = codigo

    def setIdProfessor(self, idProfessor):
        self.idProfessor = idProfessor

    def setNome(self, nome):
        self.nome = nome

    def setSemestre(self, semestre):
        self.semestre = semestre

    def getCodigo(self):
        return self.codigo

    def getIdProfessor(self):
        return self.idProfessor

    def getNome(self):
        return self.nome

    def getSemestre(self):
        return self.semestre

    def obter_informacoes(self):
        return [self.codigo,self.nome,self.semestre, self.idProfessor]

    def modificar_professor(self, id_professor):
        self.setIdProfessor(id_professor)
