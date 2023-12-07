import csv
from datetime import datetime
from Classes.Aluno import Aluno
from Classes.Professor import Professor
from Classes.RegistroAula import RegistroAula
from Classes.Cadeira import Cadeira
from Classes.ReconhecimentoFacial import ReconhecimentoFacial
import psycopg2
import json

# Mediator
class Controlador:
    # Singleton

    _instancia = None
    _aluno_vazio = None
    _professor_vazio = None
    _registro_aula_vazio = None
    _cadeira_vazio = None

    def __new__(cls):
        if not cls._instancia:
            cls._instancia = super(Controlador, cls).__new__(cls)
            cls._aluno_vazio = Aluno()
            cls._professor_vazio = Professor()
            cls._registro_aula_vazio = RegistroAula()
            cls._cadeira_vazio = Cadeira()
            cls._reconhecimento = ReconhecimentoFacial()
        return cls._instancia

# Permite a conexão com o banco de dados pela chave  
    @staticmethod
    def conectar_banco():
        try:
            connection = psycopg2.connect(
                host="localhost",
                database="padroesProjetoreconhecimentoFacial",
                user="postgres",
                password="sql#123"  
            )
            return connection
        except psycopg2.Error as e:
            print('Erro ao conectar ao banco de dados:', e)
            return None
        
# Adicionar e Remove as classes ao banco de dados
# Adição do Objeto de todas as classes
  
    def adicionar_registro_aula(self, registro):
      connection = self.conectar_banco()
      if connection:
        try:
            cursor = connection.cursor()
            query = "INSERT INTO registro_aula (codigo, faltantes, presentes,descricao,idcadeira,data,csv) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (registro.codigo, registro.idFaltantes, registro.idPresentes, registro.descricao,registro.idCadeira,registro.data,registro.csv))
            connection.commit()
            cursor.close()
            connection.close()
        except psycopg2.Error as e:
            print('Erro ao adicionar registro de aula:', e)

    def adicionar_aluno(self, aluno, foto):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO aluno (nome, matricula,id_cadeiras, foto) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (aluno.nome, aluno.matricula,aluno.idCadeira,foto))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao adicionar aluno:', e)

    def adicionar_professor(self, professor):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                # Verificar se a matrícula está na tabela CadastroProfessor
                query_verificar = "SELECT COUNT(*) FROM cadastroprofessor WHERE matricula = %s"
                cursor.execute(query_verificar, (professor.matricula,))
                result = cursor.fetchone()

                # if result[0] > 0:  # Se a matrícula existir na tabela CadastroProfessor
                queryIsAdmin = "SELECT admin FROM cadastroprofessor WHERE matricula = %s"
                cursor.execute(queryIsAdmin, (professor.matricula,))
                result = cursor.fetchone()
                professor.is_admin = result
                query = "INSERT INTO professor (matricula, senha, nome, admin) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (professor.matricula, professor.senha, professor.nome, "True"))
                connection.commit()
                print("Professor adicionado com sucesso!")
                # else:
                #     print("Matrícula não encontrada na tabela CadastroProfessor. Não é possível adicionar o professor.")
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao adicionar professor:', e)


    def adicionar_pre_cadastro(self, matricula,admin):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO cadastroprofessor (admin,matricula) VALUES (%s, %s)"
                cursor.execute(query, (admin,matricula))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao adicionar pre cadastro:', e)

    def adicionar_cadeira(self, cadeira):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "INSERT INTO cadeira (codigo, id_professor, nome, semestre) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (cadeira.codigo, cadeira.idProfessor, cadeira.nome, cadeira.semestre))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao adicionar cadeira:', e)
    
  # Remoção de um Aluno de um Cadeira
    def remover_aluno_da_cadeira(self, matricula_aluno, id_cadeira):
      connection = self.conectar_banco()
      if connection:
        try:
            cursor = connection.cursor()
            query = "DELETE FROM aluno WHERE matricula = %s AND id_cadeiras = %s"
            cursor.execute(query, (matricula_aluno, id_cadeira))
            connection.commit()
            cursor.close()
            connection.close()
        except psycopg2.Error as e:
            print('Erro ao remover aluno:', e)
          
  # Remoção de um Aluno do sistema
    def remover_aluno_por_matricula(self, matricula_aluno):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM aluno WHERE matricula = %s"
                cursor.execute(query, (matricula_aluno,))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao remover aluno:', e)

  # Remoção de todos os Alunos de uma Cadeira
    def remover_alunos_por_id_cadeira(self, id_cadeira):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM aluno WHERE id_cadeiras = %s"
                cursor.execute(query, (id_cadeira,))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao remover aluno por ID de cadeira:', e)
         
    def remover_cadeira_por_id_cadeira(self, id_cadeira):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM cadeira WHERE codigo = %s"
                cursor.execute(query, (id_cadeira,))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao remover aluno por ID de cadeira:', e)

  # Remoção de um Registro específico
    def remover_registro_aula_por_codigo(self, codigo_aula):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM registro_aula WHERE codigo = %s"
                cursor.execute(query, (codigo_aula,))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao remover registro de aula por código:', e)

  # Remoção de todos os registros de uma Cadeira
    def remover_registro_aula_por_id_cadeira(self, id_cadeira):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM registro_aula WHERE idcadeira = %s"
                cursor.execute(query, (id_cadeira,))
                connection.commit()
                cursor.close()
                connection.close()
            except psycopg2.Error as e:
                print('Erro ao remover registro de aula por ID de cadeira:', e)
              
  # Remoção de um Professor
    def remover_professor(self,matricula):return 0
      
    # Instancia as Classes em um primeiro momento de forma vazia, para depois serem completadas por outras chamadas de funções 

    def criar_aluno(self, nome, matricula, id_cadeira, foto = None):
        # Criação de uma cópia com os atributos vazios
        aluno = self._aluno_vazio.clone()
        aluno.setNome(nome)
        aluno.setMatricula(matricula)
        aluno.setCadeira(id_cadeira)
        self.adicionar_aluno(aluno,foto)
        
    def criar_professor(self, nome, matricula_professor, senha):
        # Criação de uma cópia com os atributos vazios
        professor = self._professor_vazio.clone()
        professor.setNome(nome)
        professor.setMatricula(matricula_professor)
        professor.setSenha(senha)
        self.adicionar_professor(professor)

    def criar_registro_aula(self,id_cadeira, descricao,video,codigo = None, data = datetime.now().strftime("%Y-%m-%d") ):
        # Criação de uma cópia com os atributos vazios

        rec = self._reconhecimento
        alunos = self.encontrar_aluno_por_id_cadeira(id_cadeira)
        registro = rec.reconhecimento_facial(alunos,video)
        codigo = descricao+"-"+str(data)+"-"+id_cadeira

        registro_aula = self._registro_aula_vazio.clone()
        registro_aula.setCodigo(codigo)
        registro_aula.setIdCadeira(id_cadeira)
        registro_aula.setDescricao(descricao)
        registro_aula.setData(data)
        registro_aula.setIdPresentes(registro[0])
        registro_aula.setIdFaltantes(registro[1])
        registro_aula.setCSV(registro[2])
        self.adicionar_registro_aula(registro_aula)

    def criar_cadeira(self, codigo, id_professor, nome, semestre):
        # Criação de uma cópia com os atributos vazios
        cadeira = self._cadeira_vazio.clone()
        cadeira.setCodigo(codigo)
        cadeira.setIdProfessor(id_professor)
        cadeira.setNome(nome)
        cadeira.setSemestre(semestre)
        self.adicionar_cadeira(cadeira)

# Aqui são feitas as buscas das classes através dos identificadores correspondentes dentro das listas. 

  #Busca por cadeira
    def encontrar_cadeira_por_id(self, id_cadeira):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM cadeira WHERE codigo = %s"
                cursor.execute(query, (id_cadeira,))
                result = cursor.fetchone()
                if result is not None:
                    cadeira_encontrada = self._cadeira_vazio.clone()
                    cadeira_encontrada.codigo = result[0]
                    cadeira_encontrada.idProfessor = result[1]
                    cadeira_encontrada.nome = result[2]
                    cadeira_encontrada.semestre = result[3]
                    return cadeira_encontrada
                else:
                    return None
            except psycopg2.Error as e:
                print('Erro ao encontrar cadeira:', e)
            finally:
                cursor.close()
                connection.close()
        else:
            return None

    def encontrar_cadeira_do_professor(self, matricula):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM cadeira WHERE id_professor = %s"
                cursor.execute(query, (matricula,))
                results = cursor.fetchall()
                cadeiras = []
                if results is None :
                    return None
                for result in results:
                    cadeira = self._cadeira_vazio.clone()
                    cadeira.setCodigo(result[0])
                    cadeira.setIdProfessor(result[1])
                    cadeira.setNome(result[2])
                    cadeira.setSemestre(result[3])
                    
                    cadeiras.append(cadeira.obter_informacoes())
                return cadeiras
            except psycopg2.Error as e:
                print('Erro ao encontrar cadeira:', e)
            finally:
                cursor.close()
                connection.close()
        else:
            return None
        
  #Busca por um Aluno específico em uma cadeira
    def encontrar_aluno_na_cadeira(self, matricula_aluno, id_cadeira):
      connection = self.conectar_banco()
      if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM aluno WHERE matricula = %s AND id_cadeiras = %s"
            cursor.execute(query, (matricula_aluno, id_cadeira))
            aluno = cursor.fetchone()
            cursor.close()
            connection.close()
            
            if  aluno is not None:
                    aluno_encontrado = self._aluno_vazio.clone()
                    aluno_encontrado.setMatricula(aluno[1])
                    aluno_encontrado.setNome(aluno[2])
                    aluno_encontrado.setCadeira(aluno[3])
                    aluno_encontrado.setFoto(aluno[4])
                    return aluno_encontrado
            else:
                return None
        except psycopg2.Error as e:
            print('Erro ao encontrar aluno:', e)

  #busca por um Aluno e suas cadeiras     fazer logica para cadeiras ficar como lista     
          
    def encontrar_aluno_por_matricula(self, matricula_aluno):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT dados FROM aluno WHERE matricula = %s"
                cursor.execute(query, (matricula_aluno,))
                results = cursor.fetchall()
                alunos_encontrados = []
                if results is None :
                    return None 
                for result in results:
                    dados_aluno = json.loads(result)
                    aluno_encontrado = Aluno(dados_aluno)
                    alunos_encontrados.append(aluno_encontrado)
                return alunos_encontrados
            except psycopg2.Error as e:
                print('Erro ao encontrar aluno:', e)
            finally:
                cursor.close()
                connection.close()
        else:
            return None

  #Busca por Alunos de uma Cadeira
    def encontrar_aluno_por_id_cadeira(self, id_cadeira):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM aluno WHERE id_cadeiras = %s"
                cursor.execute(query, (id_cadeira,))
                results = cursor.fetchall()
                Alunos = []
                if results is None:
                    return None
                for result in results:
                    aluno_encontrado = self._aluno_vazio.clone()
                    aluno_encontrado.setMatricula(result[1])
                    aluno_encontrado.setNome(result[2])
                    aluno_encontrado.setCadeira(result[3])
                    aluno_encontrado.setFoto(result[4])
                    Alunos.append(aluno_encontrado.obter_informacoes())
                return Alunos
            except psycopg2.Error as e:
                print('Erro ao encontrar aluno por ID de cadeira:', e)
            finally:
                cursor.close()
                connection.close()
        else:
            return None   

  #Busca por Professor
    def encontrar_professor_por_matricula(self, matricula_professor):
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM professor WHERE matricula = %s"
                cursor.execute(query, (matricula_professor,))
                result = cursor.fetchone()
                if result is not None:
                    professor_encontrado = self._professor_vazio.clone()
                    professor_encontrado.nome = result[0]
                    professor_encontrado.matricula = result[1]
                    professor_encontrado.senha = result[2]
                    professor_encontrado.is_admin = bool(result[3])
                    return professor_encontrado
                else:
                    return None
            except psycopg2.Error as e:
                print('Erro ao encontrar professor:', e)
            finally:
                cursor.close()
                connection.close()
        else:
            return None

  #Busca por um Registro
    def encontrar_registro_aula_por_codigo(self, codigo_aula): # codigo da aula sempre vai ser data no formato americado ano-mes-dia + codigo da disicplina, exmplo 2023-06-05-2999 sendo 2999 o cod disciplina
        connection = self.conectar_banco()
        if connection:
            try:
                cursor = connection.cursor()
                query = "SELECT * FROM registro_aula WHERE codigo = %s"
                cursor.execute(query, (codigo_aula,))
                result = cursor.fetchone()
                if result is not None:
                    registro_aula_encontrado = self._registro_aula_vazio.clone()
                    registro_aula_encontrado.codigo = result[0]
                    registro_aula_encontrado.idFaltantes =  result[1][1:-1].split(',')
                    registro_aula_encontrado.idPresentes =  result[2][1:-1].split(',')
                    registro_aula_encontrado.descricao = result[3]
                    registro_aula_encontrado.idCadeira = result[4]
                    registro_aula_encontrado.data = result[5]
                    registro_aula_encontrado.csv = result[6]
                    return registro_aula_encontrado.obter_informacoes()
                else:
                    return None
            except psycopg2.Error as e:
                print('Erro ao encontrar registro de aula:', e)
            finally:
                cursor.close()
                connection.close()
        else:
            return None

  #Busca por Registros de uma Cadeira
    def encontrar_registro_aula_por_id_cadeira(self, id_cadeira):
      connection = self.conectar_banco()
      if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM registro_aula WHERE idcadeira = %s"
            cursor.execute(query, (id_cadeira,))
            results = cursor.fetchall()
            registros_aula_encontrados = []
            if results is None :
                    return None
            for result in results:
                registro_aula_encontrado = self._registro_aula_vazio.clone()
                registro_aula_encontrado.codigo = result[0]
                registro_aula_encontrado.idFaltantes =  result[1]
                registro_aula_encontrado.idPresentes =  result[2]
                registro_aula_encontrado.descricao = result[3]
                registro_aula_encontrado.idCadeira = result[4]
                registro_aula_encontrado.data = result[5]
                registro_aula_encontrado.csv = result[6]

                registros_aula_encontrados.append(registro_aula_encontrado.obter_informacoes())
            return registros_aula_encontrados
        except psycopg2.Error as e:
            print('Erro ao encontrar registros de aula por código de cadeira:', e)
        finally:
            cursor.close()
            connection.close()
      else:
        return []

    def verificacao_login(self,matricula,senha):
       professor = self.encontrar_professor_por_matricula(matricula)
       resposta =[False,False]
       if professor is None:
           return resposta
       if professor.getSenha() == senha :
           resposta[0] = True
       if professor.getAdmin():
           resposta[1] = True       	  
       return resposta
#Operações de edição de dados

  #Faz verificação e modifica senha do professor
    def modificar_senha_professor(self, id_professor, senha_atual, nova_senha):
      connection = self.conectar_banco()
      if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT senha FROM professor WHERE matricula = %s"
            cursor.execute(query, (id_professor,))
            senha_armazenada = cursor.fetchone()
            if senha_armazenada is not None and senha_armazenada[0] == senha_atual:
                update_query = "UPDATE professor SET senha = %s WHERE matricula = %s"
                cursor.execute(update_query, (nova_senha, id_professor))
                connection.commit()
                print("Senha do professor atualizada com sucesso!")
            else:
                print("Senha atual fornecida não corresponde à senha armazenada no banco.")
            cursor.close()
            connection.close()
        except psycopg2.Error as e:
            print('Erro ao trocar senha do professor:', e)

  #Modificar Registro de aula coloca aluno presente como faltante
    def modificar_presente_para_faltante(self, codigo_registro, matricula_aluno):
        registro = self.encontrar_registro_aula_por_codigo(codigo_registro)
        if registro is not None:
            self.remover_registro_aula_por_codigo(codigo_registro)
            registro.remover_presente(matricula_aluno)
            registro.adicionar_faltante(matricula_aluno)
            self.adicionar_registro(registro)
        else:
            print("Registro não encontrado.")
          
  #Modificar Registro de aula coloca aluno faltante como presente
    def modificar_faltante_para_presente(self, codigo_registro, matricula_aluno):
        registro = self.encontrar_registro_por_codigo(codigo_registro)
        if registro is not None:
            self.remover_registro_por_codigo(codigo_registro)
            registro.remover_faltante(matricula_aluno)
            registro.adicionar_presente(matricula_aluno)
            self.adicionar_registro(registro)
        else:
              print("Registro não encontrado.")

  #reconehciennto facial contabilziando presença
    def contabilizar_presenca(self,id_cadeira,video = None):
        rec = self._reconhecimento
        alunos = self.encontrar_aluno_por_id_cadeira(id_cadeira)
        presenca = rec.reconhecimento_facial(alunos)
        with open(presenca[2], 'r') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                print(linha) # imprimi  csv so para verificar como veio
