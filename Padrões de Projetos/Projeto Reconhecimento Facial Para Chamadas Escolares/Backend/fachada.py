import psycopg2


class Fachada:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="padroesProjetoreconhecimentoFacial",
            user="postgres",
            password="sql#123"
        )
        self.cur = self.conn.cursor()

    def criar_aluno(self, nome, matricula):
        self.cur.execute("INSERT INTO aluno (nome, matricula) VALUES (%s, %s) RETURNING *",
                         (nome, matricula))
        aluno = self.cur.fetchone()
        self.conn.commit()

        return aluno

    def criar_cadeira(self, codigo, id_professor, nome, semestre):
        self.cur.execute("INSERT INTO cadeira (codigo, id_professor, nome, semestre) VALUES (%s, %s, %s, %s) RETURNING *",
                         (codigo, id_professor, nome, semestre))
        cadeira = self.cur.fetchone()
        self.conn.commit()

        return cadeira

    def criar_professor(self, nome, matricula, senha):
        self.cur.execute("INSERT INTO professor (nome, matricula, senha) VALUES (%s, %s, %s) RETURNING *",
                         (nome, matricula, senha))
        professor = self.cur.fetchone()
        self.conn.commit()

        return professor

    def registrar_aula(self, id_professor, descricao, id_cadeira, data):
        self.cur.execute("INSERT INTO registro_aula (id_professor, descricao, id_cadeira, data) VALUES (%s, %s, %s, %s) RETURNING *",
                         (id_professor, descricao, id_cadeira, data))
        registro_aula = self.cur.fetchone()
        self.conn.commit()

        return registro_aula

    def adicionar_cadeira_aluno(self, aluno_matricula, id_cadeira):
        self.cur.execute("UPDATE aluno SET id_cadeiras = %s WHERE matricula = %s",
                         (id_cadeira, aluno_matricula))
        self.conn.commit()

    def remover_cadeira_aluno(self, aluno_matricula, id_cadeira):
        self.cur.execute("UPDATE aluno SET id_cadeiras = %s WHERE matricula = %s",
                         (id_cadeira, aluno_matricula))
        self.conn.commit()

    # Resto das funções da fachada...


# Exemplo de uso da fachada
fachada = Fachada()

# Criar um professor
professor = fachada.criar_professor("kAT", "2222", "senha123")

# Criar um aluno
aluno = fachada.criar_aluno("João Silva", "9090")

# Criar uma cadeira
cadeira = fachada.criar_cadeira("9987", "2222", "pprojeto", "2023/1")

# Adicionar a cadeira ao aluno
fachada.adicionar_cadeira_aluno("9090", "9987")

# # Registrar uma aula
# registro_aula = fachada.registrar_aula(
#     professor["2222"], "Aula de PP", cadeira["9987"], "2023-05-31")


# # Remover a cadeira do aluno
# fachada.remover_cadeira_aluno(aluno["9090"], cadeira["9987"])
