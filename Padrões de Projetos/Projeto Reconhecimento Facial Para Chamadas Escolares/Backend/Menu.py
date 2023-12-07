import os
from Controlador import Controlador

class Menu:

    _instance = None
    


    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Menu, cls).__new__(cls)
            cls._instance.controle = Controlador()
        return cls._instance
    
    def encontrar_caminho_arquivo(self,nome_arquivo):
        diretorio_atual = os.getcwd()
        for root, dirs, files in os.walk(diretorio_atual):
            if nome_arquivo in files:
                caminho_arquivo = os.path.join(root, nome_arquivo)
                return caminho_arquivo
        return None
    
    def verifica_login(self,matricula,senha):
        resposta = self.controle.verificacao_login(matricula,senha)
        return resposta
    
    def visualizar_cadeiras(self,matricula):
        cadeiras = self.controle.encontrar_cadeira_do_professor(matricula)
        return cadeiras
    
    def vizualizar_Cadeira(self,id_Cadeira):
        return self.controle.encontrar_cadeira_por_id(id_Cadeira)

    def pre_cadastro(self):
        print("Digite Matrícula:")
        matricula = input()
        print("Digite True(admin) ou False:")
        admin = bool(input())
        self.controle.adicionar_pre_cadastro(matricula,admin)
        
    def cadastro(self):
        print("Digite Matrícula:")
        matricula = input()
        print("Digite o Nome do Professor:")
        nome = input()
        print("Digite Senha:")
        senha = input()
        self.controle.criar_professor(nome, matricula,senha)
    
    def cadastro_cadeira(self,matricula):
        id_professor = matricula
        print("Digite o Nome da Cadeira:")
        nome = input()
        print("Digite o Semeste:")
        semestre = input()
        codigo = input("Digite o id da cadeira:")
        self.controle.criar_cadeira(codigo, id_professor, nome, semestre)
            
    def cadastro_aluno(self,id_cadeira):
        # professor = self.controle.encontrar_cadeira_do_professor(matricula)
        nome = input("Digite o nome do aluno:")
        matricula = input("Digite a matricula do aluno:")
        foto = input("Digite a foto do aluno:")

        self.controle.criar_aluno(nome, matricula, id_cadeira,foto)
        
    def registrar_aula(self,id_cadeira):
        descricao = input("Descriçao da aula: ")
        video = input("Insira o caminho do video: ")
        print("Aguarde enquanto processamos o video ...")
        self.controle.criar_registro_aula(id_cadeira, descricao,video)

    def deletar_cadeira(self,id_cadeira):
        self.controle.remover_alunos_por_id_cadeira(id_cadeira)
        self.controle.remover_registro_aula_por_id_cadeira(id_cadeira)
        self.controle.remover_cadeira_por_id_cadeira(id_cadeira)
        
    def deletar_aluno(self,matricula,id_cadeira):
        self.controle.remover_aluno_da_cadeira(matricula,id_cadeira)
        
    def deletar_registro(self,matricula):
        print("Digite o Id do Registro de Aula:")
        codigo = input()
        self.controle.remover_registro_aula_por_codigo(codigo)

    def encontrar_alunos(self, id_cadeira):
        alunos = self.controle.encontrar_aluno_por_id_cadeira(id_cadeira)
        return alunos
    
    def encontar_registro(self, id_cadeira):
        registro = self.controle.encontrar_registro_aula_por_id_cadeira(id_cadeira)
        return registro
        
