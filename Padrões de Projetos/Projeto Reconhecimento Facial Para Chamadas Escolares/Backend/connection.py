import psycopg2

# Configurações da conexão
db_host = "localhost"
db_port = "5432"
db_name = "padroesProjetoreconhecimentoFacial"
db_user = "postgres"
db_password = "sql#123"

# Conectando ao banco de dados
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    database=db_name,
    user=db_user,
    password=db_password
)

# Criando um cursor para executar consultas
cursor = conn.cursor()

try:
    # Inserir um professor
    professor_query = "INSERT INTO professor (nome, matricula, senha, admin) VALUES (%s, %s, %s, %s)"
    professor_values = ("KAT", "123456", "senha123", [False])
    cursor.execute(professor_query, professor_values)
    conn.commit()
    print("Professor inserido com sucesso!")

    # Inserir uma cadeira
    cadeira_query = "INSERT INTO cadeira (codigo, id_professor, nome, semestre) VALUES (%s, %s, %s, %s)"
    cadeira_values = ("C001", "123456", "Padroes de projeto", "2023/1")
    cursor.execute(cadeira_query, cadeira_values)
    conn.commit()
    print("Cadeira inserida com sucesso!")

    # Inserir um aluno
    aluno_query = "INSERT INTO aluno (nome, matricula, id_cadeiras, foto) VALUES (%s, %s, %s, %s)"
    aluno_values = ("Isaac", "123455", "C001", "caminho da foto")
    cursor.execute(aluno_query, aluno_values)
    conn.commit()
    print("Aluno inserido com sucesso!")

except psycopg2.Error as e:
    conn.rollback()
    print("Erro ao inserir os dados:", e)

finally:
    # Fechando o cursor e a conexão
    cursor.close()
    conn.close()
