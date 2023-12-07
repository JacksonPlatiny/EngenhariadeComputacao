import os
import tkinter as tk
from tkinter import messagebox
import tkinter.filedialog as filedialog
from LoginCopy import Login

class InterfaceGrafica:
    def __init__(self):
        self.login = Login()
        self.janela_atual = None
        self.entry_descricao = None
        self.root = tk.Tk()
        self.root.title("Sistema de Cadeiras")

        # Configura a largura e altura da janela
        self.width = 350
        self.height = 250

        # Obtém a resolução da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calcula a posição x e y para centralizar a janela na tela
        self.x = (screen_width // 2) - (self.width // 2)
        self.y = (screen_height // 2) - (self.height // 2)

        # Define a posição da janela
        self.root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")


        self.btn_cadastrar = tk.Button(self.root, text="Cadastrar", command=self.abrir_tela_cadastro)
        self.btn_cadastrar.pack(pady=20)

        self.btn_login = tk.Button(self.root, text="Login", command=self.abrir_tela_login)
        self.btn_login.pack(pady=10)

        self.btn_sair = tk.Button(self.root, text="Sair", command=self.root.quit)
        self.btn_sair.pack(pady=10)

    def fechar_janela_atual(self):
        if self.janela_atual:
            self.janela_atual.destroy()
            self.janela_atual = None

    def voltar_ao_menu(self):
        self.fechar_janela_atual()
        self.exibir_menu()

    def abrir_tela_cadastro(self):
        self.fechar_janela_atual()
        self.root.withdraw()  # Esconde a janela principal

        # Cria a nova janela de cadastro
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Cadastro de Professor")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.label_nome = tk.Label(self.janela_atual, text="Nome:")
        self.label_nome.pack()

        self.entry_nome = tk.Entry(self.janela_atual)
        self.entry_nome.pack()

        self.label_matricula = tk.Label(self.janela_atual, text="Matrícula:")
        self.label_matricula.pack()

        self.entry_matricula = tk.Entry(self.janela_atual)
        self.entry_matricula.pack()

        self.label_senha = tk.Label(self.janela_atual, text="Senha:")
        self.label_senha.pack()

        self.entry_senha = tk.Entry(self.janela_atual, show="*")
        self.entry_senha.pack()

        self.btn_confirmar = tk.Button(self.janela_atual, text="Confirmar", command=self.cadastrar_professor)
        self.btn_confirmar.pack(pady=10)

        btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=self.deslogar)
        btn_voltar.pack(pady=10)

    def cadastrar_professor(self):
        nome = self.entry_nome.get()
        matricula = self.entry_matricula.get()
        senha = self.entry_senha.get()
        self.login.cadastro(nome, matricula, senha)
        messagebox.showinfo("Sucesso", "Professor cadastrado com sucesso.")

        self.abrir_tela_login()

    def abrir_tela_login(self):
        self.fechar_janela_atual()
        self.root.withdraw()  # Esconde a janela principal

        # Cria a nova janela de login
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Login")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.label_matricula = tk.Label(self.janela_atual, text="Matrícula:")
        self.label_matricula.pack()

        self.entry_matricula = tk.Entry(self.janela_atual)
        self.entry_matricula.pack()

        self.label_senha = tk.Label(self.janela_atual, text="Senha:")
        self.label_senha.pack()

        self.entry_senha = tk.Entry(self.janela_atual, show="*")
        self.entry_senha.pack()

        self.btn_entrar = tk.Button(self.janela_atual, text="Entrar", command=self.efetuar_login)
        self.btn_entrar.pack(pady=10)

        btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=self.deslogar)
        btn_voltar.pack(pady=10)

        self.janela_atual.protocol("WM_DELETE_WINDOW", self.fechar_tela_login)  # Trata o fechamento da janela

    def efetuar_login(self):
        matricula = self.entry_matricula.get()
        senha = self.entry_senha.get()

        if self.login.fazer_login(matricula, senha):
            self.fechar_janela_atual()
            self.exibir_menu()
        else:
            messagebox.showerror("Erro", "Matrícula ou senha incorretas.")

    def exibir_menu(self):
        self.fechar_janela_atual()
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Menu")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.label_titulo = tk.Label(self.janela_atual, text="MENU")
        self.label_titulo.pack(pady=20)

        self.btn_visualizar_disciplinas = tk.Button(self.janela_atual, text="Visualizar Disciplinas", command=self.visualizar_disciplinas)
        self.btn_visualizar_disciplinas.pack(pady=10)

        self.btn_cadastrar_disciplinas = tk.Button(self.janela_atual, text="Cadastrar Disciplinas", command=self.abrir_tela_cadastrar_disciplinas)
        self.btn_cadastrar_disciplinas.pack(pady=10)

        self.btn_deslogar = tk.Button(self.janela_atual, text="Deslogar", command=self.deslogar)
        self.btn_deslogar.pack(pady=10)

    def visualizar_disciplinas(self):
        self.fechar_janela_atual()
        disciplinas = self.login.visualizar_cadeiras(self.login.matricula)

        # Cria uma nova janela para exibir as disciplinas
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Disciplinas")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        if len(disciplinas)>0:
            for disciplina in disciplinas:
                btn_disciplina = tk.Button(self.janela_atual, text=disciplina[1], command=lambda d=disciplina: self.exibir_detalhes_disciplina(d))
                btn_disciplina.pack(pady=5)
            btn_deletar = tk.Button(self.janela_atual, text="Deletar disciplina", command=self.deletar_disciplina)
            btn_deletar.pack(pady=10)
        else:
            self.label_titulo = tk.Label(self.janela_atual, text="Não possui disciplinas")
            self.label_titulo.pack(pady=20)
            btn_cadastrar = tk.Button(self.janela_atual, text="Cadastrar disciplina", command=self.abrir_tela_cadastrar_disciplinas)
            btn_cadastrar.pack(pady=10)
            
        btn_voltar = tk.Button(self.janela_atual, text="Voltar ao Menu", command=self.voltar_ao_menu)
        btn_voltar.pack(pady=10)

    def exibir_detalhes_disciplina(self, disciplina):
        self.fechar_janela_atual()

        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Detalhes da Disciplina")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        btn_adicionar_aluno = tk.Button(self.janela_atual, text="Adicionar Aluno", command=lambda: self.abrir_tela_adicionar_aluno(disciplina))
        btn_adicionar_aluno.pack(pady=10)

        btn_registrar_aula = tk.Button(self.janela_atual, text="Fazer Reconhecimento e Contabilizar Presença", command=lambda: self.registrar_aula(disciplina))
        btn_registrar_aula.pack(pady=10)
        btn_vizualizar_registro = tk.Button(self.janela_atual, text="Vizualizar Registro de Aula", command=lambda: self.vizualizar_registro(disciplina))
        btn_vizualizar_registro.pack(pady=10)

        btn_deletar_aluno = tk.Button(self.janela_atual, text="Deletar aluno", command=lambda: self.deletar_aluno(disciplina))
        btn_deletar_aluno.pack(pady=10)


        btn_voltar = tk.Button(self.janela_atual, text="Voltar à Lista de Disciplinas", command=self.visualizar_disciplinas)
        btn_voltar.pack(pady=10)

    def abrir_tela_adicionar_aluno(self, disciplina):
        self.fechar_janela_atual()
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Adicionar Aluno")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.label_nome_aluno = tk.Label(self.janela_atual, text="Nome do Aluno:")
        self.label_nome_aluno.pack()
        self.entry_nome_aluno = tk.Entry(self.janela_atual)
        self.entry_nome_aluno.pack()

        self.label_matricula_aluno = tk.Label(self.janela_atual, text="Matrícula do Aluno:")
        self.label_matricula_aluno.pack()
        self.entry_matricula_aluno = tk.Entry(self.janela_atual)
        self.entry_matricula_aluno.pack()

        btn_selecionar_foto = tk.Button(self.janela_atual, text="Selecionar Foto", command=lambda: self.selecionar_foto(disciplina))
        btn_selecionar_foto.pack(pady=10)

        self.label_foto_status = tk.Label(self.janela_atual, text="")
        self.label_foto_status.pack()

        btn_confirmar = tk.Button(self.janela_atual, text="Confirmar", command=lambda: self.adicionar_aluno(disciplina, self.entry_matricula_aluno.get(), self.entry_nome_aluno.get(), self.foto_path))
        btn_confirmar.pack(pady=5)

        btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
        btn_voltar.pack(pady=10)

    def selecionar_foto(self, disciplina):
        self.foto_path = filedialog.askopenfilename(title="Selecionar Foto", filetypes=(("Arquivos de Imagem", "*.jpg;*.jpeg;*.png"), ("Todos os Arquivos", "*.*")))
        if self.foto_path:
            self.label_foto_status.config(text="Foto selecionada", fg="green")
        else:
            self.label_foto_status.config(text="")

    def adicionar_aluno(self, disciplina, matricula_aluno, nome_aluno, foto):
        self.login.cadastrar_aluno(disciplina[0], matricula_aluno, nome_aluno, foto)
        self.exibir_detalhes_disciplina(disciplina)
        messagebox.showinfo("Sucesso", "Aluno adicionado com sucesso.")


    def registrar_aula(self, disciplina):
        self.fechar_janela_atual()
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Fazer Reconhecimento e Contabilizar Presença")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        alunos = self.login.encontrar_alunos(disciplina[0])

        if(len(alunos)>0):
            self.label_descricao = tk.Label(self.janela_atual, text="Descrição:")
            self.label_descricao.pack()

            self.entry_descricao = tk.Entry(self.janela_atual)
            self.entry_descricao.pack()

            self.btn_selecionar_video = tk.Button(self.janela_atual, text="Selecionar Video", command=lambda: self.selecionar_video(disciplina))
            self.btn_selecionar_video.pack(pady=10)
            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
            btn_voltar.pack(pady=10)
        else:
            self.label_titulo = tk.Label(self.janela_atual, text="Não possui aluno para contabilizar presença")
            self.label_titulo.pack(pady=20)
            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
            btn_voltar.pack(pady=10)

    def selecionar_video(self, disciplina):
        video_path = filedialog.askopenfilename(title="Selecionar Video", filetypes=(("Arquivos de Vídeo", "*.mp4"), ("Todos os Arquivos", "*.*")))
        if video_path:
            descricao = self.entry_descricao.get()
            confirmation = messagebox.askquestion("Confirmação", "Deseja registrar a aula com a descrição: {}".format(descricao))
            if confirmation == 'yes':
                self.registrar_aula_confirmada(disciplina, descricao, video_path)

    def registrar_aula_confirmada(self, disciplina, descricao, video_path):
        self.login.registrar_aula(disciplina[0], descricao, video_path)
        messagebox.showinfo("Sucesso", "Reconhecimento facial e contabilização de presença realizados com sucesso.")
        self.visualizar_disciplinas()

    def vizualizar_registro(self, disciplina):
        registros = self.login.encontrar_registro_aula(disciplina[0])

        self.fechar_janela_atual()

        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Registro de Aula")

        window_width = 500
        window_height = 300
        screen_width = self.janela_atual.winfo_screenwidth()
        screen_height = self.janela_atual.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.janela_atual.geometry(f"{window_width}x{window_height}+{x}+{y}")

        if len(registros) > 0:
            # Create column headers
            label_data_header = tk.Label(self.janela_atual, text="Data")
            label_data_header.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

            label_descricao_header = tk.Label(self.janela_atual, text="Descrição")
            label_descricao_header.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

            label_csv_header = tk.Label(self.janela_atual, text="Arquivo CSV")
            label_csv_header.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")

            # Create rows with data
            for index, registro in enumerate(registros, start=1):
                label_data = tk.Label(self.janela_atual, text=registro[5])
                label_data.grid(row=index, column=0, padx=5, pady=5, sticky="nsew")

                label_descricao = tk.Label(self.janela_atual, text=registro[1])
                label_descricao.grid(row=index, column=1, padx=5, pady=5, sticky="nsew")

                btn_csv = tk.Button(
                    self.janela_atual,
                    text="Visualizar CSV",
                    command=lambda csv_file=registro[6]: self.abrir_csv(csv_file)
                )
                btn_csv.grid(row=index, column=2, padx=5, pady=5, sticky="nsew")

            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
            btn_voltar.grid(row=len(registros) + 1, column=1, pady=5, sticky="nsew")

            
        else:
            self.label_titulo = tk.Label(self.janela_atual, text="Não possui registro")
            self.label_titulo.grid(row=1, column=0, columnspan=3, pady=20)
            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
            btn_voltar.grid(row=len(registros) + 2, column=1, pady=10, sticky="nsew")

        # Configure grid weights to center content
        self.janela_atual.grid_rowconfigure(0, weight=1)
        self.janela_atual.grid_columnconfigure((0, 1, 2), weight=1)

    def deletar_aluno(self, disciplina):
        alunos = self.login.encontrar_alunos(disciplina[0])

        self.fechar_janela_atual()

        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Deletar Aluno")

        window_width = 500
        window_height = 300
        screen_width = self.janela_atual.winfo_screenwidth()
        screen_height = self.janela_atual.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.janela_atual.geometry(f"{window_width}x{window_height}+{x}+{y}")

        if len(alunos) > 0:
            # Create column headers
            label_nome_header = tk.Label(self.janela_atual, text="Nome")
            label_nome_header.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

            label_matricula_header = tk.Label(self.janela_atual, text="Matricula")
            label_matricula_header.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

            # Create rows with data
            for index, aluno in enumerate(alunos, start=1):
                label_nome = tk.Label(self.janela_atual, text=aluno[0])
                label_nome.grid(row=index, column=0, padx=5, pady=5, sticky="nsew")

                label_matricula = tk.Label(self.janela_atual, text=aluno[1])
                label_matricula.grid(row=index, column=1, padx=5, pady=5, sticky="nsew")

                btn_deletar = tk.Button(
                    self.janela_atual,
                    text="Deletar",
                    command=lambda matricula=aluno[1]: self.confirmar_delecao_aluno(matricula, disciplina[0],alunos)
                )
                btn_deletar.grid(row=index, column=2, padx=5, pady=5, sticky="nsew")

            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
            btn_voltar.grid(row=len(alunos) + 1, column=1, pady=5, sticky="nsew")
        else:
            self.label_titulo = tk.Label(self.janela_atual, text="Não possui alunos")
            self.label_titulo.grid(row=1, column=0, columnspan=3, pady=20)
            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=lambda: self.exibir_detalhes_disciplina(disciplina))
            btn_voltar.grid(row=len(alunos) + 2, column=1, pady=10, sticky="nsew")

        # Configure grid weights to center content
        self.janela_atual.grid_rowconfigure(0, weight=1)
        self.janela_atual.grid_columnconfigure((0, 1, 2), weight=1)

    def confirmar_delecao_aluno(self, matricula, disciplina,alunos):
        resposta = messagebox.askyesno("Confirmar Deleção", "Deseja deletar o aluno com a matrícula {}?".format(matricula))
        if resposta:
            self.login.deletar_aluno(matricula,disciplina)
            self.exibir_detalhes_disciplina(disciplina)


    def deletar_disciplina(self):
        self.fechar_janela_atual()
        disciplinas = self.login.visualizar_cadeiras(self.login.matricula)


        self.fechar_janela_atual()

        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Deletar disciplina")

        window_width = 500
        window_height = 300
        screen_width = self.janela_atual.winfo_screenwidth()
        screen_height = self.janela_atual.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        self.janela_atual.geometry(f"{window_width}x{window_height}+{x}+{y}")

        if len(disciplinas) > 0:
            # Create column headers
            label_nome_header = tk.Label(self.janela_atual, text="Nome")
            label_nome_header.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

            label_matricula_header = tk.Label(self.janela_atual, text="Codigo")
            label_matricula_header.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

            # Create rows with data
            for index, disciplina in enumerate(disciplinas, start=1):
                label_nome = tk.Label(self.janela_atual, text=disciplina[1])
                label_nome.grid(row=index, column=0, padx=5, pady=5, sticky="nsew")

                label_matricula = tk.Label(self.janela_atual, text=disciplina[0])
                label_matricula.grid(row=index, column=1, padx=5, pady=5, sticky="nsew")

                btn_deletar = tk.Button(
                    self.janela_atual,
                    text="Deletar",
                    command=lambda matricula=disciplina[1]: self.confirmar_delecao_disciplina(disciplina)
                )
                btn_deletar.grid(row=index, column=2, padx=5, pady=5, sticky="nsew")

            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=self.visualizar_disciplinas)
            btn_voltar.grid(row=len(disciplinas) + 1, column=1, pady=5, sticky="nsew")
        else:
            self.label_titulo = tk.Label(self.janela_atual, text="Não possui alunos")
            self.label_titulo.grid(row=1, column=0, columnspan=3, pady=20)
            btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=self.visualizar_disciplinas)
            btn_voltar.grid(row=len(disciplinas) + 2, column=1, pady=10, sticky="nsew")

        # Configure grid weights to center content
        self.janela_atual.grid_rowconfigure(0, weight=1)
        self.janela_atual.grid_columnconfigure((0, 1, 2), weight=1)

    def confirmar_delecao_disciplina(self,disciplina):
        resposta = messagebox.askyesno("Confirmar Deleção", "Deseja deletar a disciplina {}?".format(disciplina[1]))
        if resposta:
            self.login.deletar_cadeira(disciplina[0])
            self.visualizar_disciplinas()

    def abrir_csv(self, csv_file):
        if os.path.exists(csv_file):
            os.system(csv_file)
        else:
            messagebox.showerror("Erro", "O arquivo CSV não existe.")

    def abrir_tela_cadastrar_disciplinas(self):
        self.fechar_janela_atual()
        self.janela_atual = tk.Toplevel()
        self.janela_atual.title("Cadastrar Disciplinas")
        self.janela_atual.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.label_nome_disciplina = tk.Label(self.janela_atual, text="Nome da Disciplina:")
        self.label_nome_disciplina.pack()

        self.entry_nome_disciplina = tk.Entry(self.janela_atual)
        self.entry_nome_disciplina.pack()

        self.label_codigo_disciplina = tk.Label(self.janela_atual, text="Codigo da Disciplina:")
        self.label_codigo_disciplina.pack()

        self.entry_codigo_disciplina = tk.Entry(self.janela_atual)
        self.entry_codigo_disciplina.pack()

        self.label_semestre_disciplina = tk.Label(self.janela_atual, text="Semestre:")
        self.label_semestre_disciplina.pack()

        self.entry_semestre_disciplina = tk.Entry(self.janela_atual)
        self.entry_semestre_disciplina.pack()

        btn_confirmar = tk.Button(self.janela_atual, text="Confirmar", command=self.cadastrar_disciplina)
        btn_confirmar.pack(pady=10)

        btn_voltar = tk.Button(self.janela_atual, text="Voltar", command=self.voltar_ao_menu)
        btn_voltar.pack(pady=10)


    def cadastrar_disciplina(self):
        nome_disciplina = self.entry_nome_disciplina.get()
        codigo = self.entry_codigo_disciplina.get()
        semestre = self.entry_semestre_disciplina.get()
        self.login.cadastrar_cadeira(codigo,nome_disciplina, semestre)
        self.exibir_menu()
        messagebox.showinfo("Sucesso", "Disciplina cadastrada com sucesso.")

    def deslogar(self):
        self.login.deslogar()
        self.fechar_janela_atual()
        self.root.deiconify()  # Mostra novamente a janela principal

    def fechar_tela_login(self):
        self.fechar_janela_atual()
        self.root.quit()

    def iniciar(self):
        self.root.mainloop()

if __name__ == "__main__":
    interface = InterfaceGrafica()
    interface.iniciar()
