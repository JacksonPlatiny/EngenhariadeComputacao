from copy import deepcopy

class RegistroAula:
    def __init__(self):
        self.idPresentes = []
        self.idFaltantes = []
        self.descricao = None
        self.idCadeira = None
        self.data = None
        self.csv = None
        self.codigo = None
        
    def clone(self):
        return deepcopy(self)

    def setIdPresentes(self, idPresentes):
        self.idPresentes = idPresentes

    def setCSV(self, csv):
        self.csv = csv


    def setIdFaltantes(self, idFaltantes):
        self.idFaltantes = idFaltantes

    def setDescricao(self, novaDescricao):
        self.descricao = novaDescricao

    def setIdCadeira(self, idCadeira):
        self.idCadeira = idCadeira

    def setData(self, data):
        self.data = data

    def setCodigo(self, codigo):
        self.codigo = codigo

    def getIdPresentes(self):
        return self.idPresentes

    def getIdFaltantes(self):
        return self.idFaltantes

    def getDescricao(self):
        return self.descricao

    def getIdCadeira(self):
        return self.idCadeira

    def getData(self):
        return self.data
    
    def getCSV(self):
        return self.csv
    
    def getCodigo(self):
            return self.codigo
    def obter_informacoes(self):
        return [self.codigo,self.descricao,self.idPresentes,self.idFaltantes, self.idCadeira, self.data,self.csv]

    # Função para adicionar um ID de aluno à lista de presentes

    def adicionar_presente(self, id_aluno):
        if id_aluno in self.idFaltantes:
            self.idFaltantes.remove(id_aluno)
            self.idPresentes.append(id_aluno)

    # Função para remover um ID de aluno da lista de presentes

    def remover_presente(self, id_aluno):
        if id_aluno in self.idPresentes:
            self.idFaltantes.append(id_aluno)
            self.idPresentes.remove(id_aluno)
