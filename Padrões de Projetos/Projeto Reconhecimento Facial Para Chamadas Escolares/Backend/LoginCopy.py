from MenuCopy import Menu

class Login:
    def __init__(self):
        self.sistema = Menu()
        self.matricula = None
        self.logado = False
        self.admin = False
        
    def pre_cadastro(self):
        if self.logado and self.admin:
            self.sistema.pre_cadastro()
            
    def cadastro(self,nome, matricula, senha):
        self.sistema.cadastro(nome, matricula, senha)
            
    def fazer_login(self,matricula,senha):
        
        verificado = self.sistema.verifica_login(matricula, senha)
        if verificado[0]:
            self.logado = True
            self.matricula = matricula
            if verificado[1]:
                self.admin = True
                return "ADMIN"
            return "PADRAO"
        return False
        
    def deslogar(self):
        self.logado = False
        self.admin = False
        self.matricula = None
    
    def cadastrar_cadeira(self,codigo,nome, semestre):
        if self.logado:
            self.sistema.cadastro_cadeira(self.matricula,codigo,nome, semestre)
            
    def cadastrar_aluno(self, codigo,matricula_aluno,nome_aluno, foto):
        if self.logado:
            self.sistema.cadastro_aluno(codigo,matricula_aluno,nome_aluno, foto)
            
    def registrar_aula(self,id_cadeira,descricao, video):
        if self.logado:
            self.sistema.registrar_aula(id_cadeira,descricao, video)
    
    def deletar_cadeira(self,id_cadeira):
        if self.logado:
            self.sistema.deletar_cadeira(id_cadeira)
    
    def deletar_aluno(self,matricula,idcadeira):
        if self.logado:
            self.sistema.deletar_aluno(matricula,idcadeira)
    
    def deletar_registro(self):
        if self.logado:
            self.sistema.deletar_registro(self.matricula)

    def visualizar_cadeiras(self, matricula_prof):
        return self.sistema.visualizar_cadeiras(matricula_prof)
        
    def vizualizar_cadeira(self, id_cadeira):
        return self.sistema.vizualizar_Cadeira(id_cadeira)
    
    def encontrar_alunos(self, id_cadeira):
        return self.sistema.encontrar_alunos(id_cadeira)
    
    def encontrar_registro_aula(self, id_cadeira):
        return self.sistema.encontar_registro(id_cadeira)
