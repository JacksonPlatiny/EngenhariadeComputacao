from Login import Login

class Interface:

    def __init__(self):
        self.login = Login()

    def exibir_menu_principal(self):
        print(" ")
        print("=== MENU PRINCIPAL ===")
        print("1. Cadastro")
        print("2. Login")
        print("0. Sair")

    def exibir_menu_logado(self):
        print(" ")

        print("=== MENU ===")
        print("1. Cadastrar Cadeira")
        print("2. Vizualizar cadeiras")
        print("0. Deslogar")

    def exibir_abrir_cadeiras(self):
        print(" ")
        print("=== MENU Cadeira ===")
        print("1. Abrir uma cadeira")
        print("2. Deletar Cadeira")
        print("0. Voltar")
    
    def exibir_manipular_cadeiras(self):
        print(" ")
        print("1. Adicionar Aluno")
        print("2. Deletar Aluno")
        print("3. Fazer reconhecimento e contabilizar presença")
        print("4. Visualizar registros de aula")
        print("5. Deletar registro de aula")
        print("0. Voltar")

    def iniciar(self):
        while True:
            self.exibir_menu_principal()
            print(" ")
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.login.cadastro()

            elif opcao == "2":
                login = self.login.fazer_login()
    
                if login:
                    if login == "ADMIN":
                        print("Você é admin")
                        print(" ")
                        self.menu_logado()
                        
                    else:
                        print("Você é user padrão")
                        print(" ")
                        self.menu_logado()
                        
                print("Erro ao logar tente novamente")
                print(" ")


            elif opcao == "0":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida!")

    def menu_cadeira(self,codigo):
        
        while True:

            print("Cadeira - ",self.login.vizualizar_cadeira(codigo).nome)
            self.exibir_manipular_cadeiras()
            opcao = input("Digite a opção desejada: ")
            print(" ")
            if(opcao == '1'):
                self.login.cadastrar_aluno(codigo)
                print("aluno adicionado")

            elif(opcao == "2"):
                print(" ")
                print("Alunos na cadeira:")
                alunos = self.login.encontrar_alunos(codigo)
                matriculas = []
                for linha in alunos:
                    matricula = linha[1]
                    matriculas.append(matricula)

                if(len(alunos)>0):
                    for aluno in alunos:
                        print("Nome:",aluno[0], " Matricula:", aluno[1])    
                else:
                    print("Cadeira não possui alunos")

                matricula = input("Informe a matricula do aluno: ")

                if(matricula not in matriculas):
                    print("O aluno nao existe")
                else:
                    self.login.deletar_aluno(matricula,codigo)

            elif(opcao == "3"):
                alunos = self.login.encontrar_alunos(codigo)
                matriculas = []
                for linha in alunos:
                    matricula = linha[1]
                    matriculas.append(matricula)

                if(len(alunos)>0):
                    for aluno in alunos:
                        print("Nome:",aluno[0], " Matricula:", aluno[1])
                    self.login.registrar_aula(codigo)   
                    print("Aula registrada")    
                else:
                    print("Cadeira não possui alunos")

            elif(opcao == "4"):
                if(len(self.login.encontrar_registro_aula(codigo))):
                    for registro in self.login.encontrar_registro_aula(codigo):
                        print("Data:",registro[5],"Descriçao:",registro[1],"Presentes:",registro[2],"Ausentes",registro[3])
                else:
                    print("----------------------------")
                    print("Ainda não possui registro")
            
            elif(opcao == "5"):
                if(len(self.login.encontrar_registro_aula(codigo))):
                    for registro in self.login.encontrar_registro_aula(codigo):
                        print("Data:",registro[5],"Descriçao:",registro[1])
                    self.login.deletar_registro()
                else:
                    print("----------------------------")
                    print("Ainda não possui registro")
                
            elif(opcao == "0"):
                break
            else:
                print("Opção Inválida.")

    def menu_logado(self):

        while self.login.logado:
            self.exibir_menu_logado()
            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.login.cadastrar_cadeira()


            elif opcao == "2":
                self.login.visualizar_cadeiras(self.login.matricula)
                primeiros_elementos = []
                for linha in self.login.visualizar_cadeiras(self.login.matricula,1):
                    primeiro_elemento = linha[0]
                    primeiros_elementos.append(primeiro_elemento)

                while True:
                    if len(primeiros_elementos)> 0:
                        self.exibir_abrir_cadeiras()
                        opcaoCadeira = input("Digite a opção desejada: ")

                        if(opcaoCadeira == "1"):
                            codigoCadeira = input("Digite o codigo da cadeira: ")
                            if(codigoCadeira not in primeiros_elementos):
                                print(" ")
                                print(" - - - Codigo Invalido - - - ")
                                print(" ")
                            else:
                                self.menu_cadeira(codigoCadeira)

                        elif opcaoCadeira == "2":
                            codigoCadeira = input("Digite o codigo da cadeira: ")
                            if(codigoCadeira not in primeiros_elementos):
                                print(" ")
                                print(" - - - Codigo Invalido - - - ")
                                print(" ")
                            else:
                                self.login.deletar_cadeira(codigoCadeira)
                                break

                            
                        elif opcaoCadeira == "0":
                            break
                        else:
                            print("Opção Inválida")

                    else:
                        print("---------------------------")
                        print("Ainda não possui disciplina")
                        break


            elif opcao == "0":
                self.login.deslogar()
            else:
                print("Opção inválida!")
                        
        
interface = Interface()
interface.iniciar()
