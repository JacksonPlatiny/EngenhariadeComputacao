pecaPreta = 'P'
pecaBranca = 'B'
espacoVazio = '*'
damaPreta = 'DP'
damaBranca = 'DB'
dicionarioCoordenadas = {"A": 0, "a": 0, "B": 1, "b": 1, "C": 2, "c": 2, "D": 3, "d": 3,
                         "E": 4, "e": 4, "F": 5, "f": 5, "G": 6, "g": 6, "H": 7, "h": 7}
# Variáveis úteis
# Dicionário para receber as letras da coluna e converter em valores para a coluna da matriz do tabuleiro

def cria_tabuleiro():  # Cria a matriz do tabuleiro.
    '''
    tabuleiro = [[pecaPreta, espacoVazio, pecaPreta, espacoVazio, pecaPreta, espacoVazio, pecaPreta, espacoVazio],
                 [espacoVazio, pecaPreta, espacoVazio, pecaPreta, espacoVazio, pecaPreta, espacoVazio, pecaPreta],
                 [pecaPreta, espacoVazio, pecaPreta, espacoVazio, pecaPreta, espacoVazio, pecaPreta, espacoVazio],
                 [espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio],
                 [espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio, espacoVazio],
                 [espacoVazio, pecaBranca, espacoVazio, pecaBranca, espacoVazio, pecaBranca, espacoVazio, pecaBranca],
                 [pecaBranca, espacoVazio, pecaBranca, espacoVazio, pecaBranca, espacoVazio, pecaBranca, espacoVazio],
                 [espacoVazio, pecaBranca, espacoVazio, pecaBranca, espacoVazio, pecaBranca, espacoVazio, pecaBranca]]
                 ou ao contrário (brancas em cima mantendo o padrão)
    '''
    tabuleiro = [[], [], [], [], [], [], [], []]
    for i in range(len(tabuleiro)):
        for e in range(len(tabuleiro)):
            if ((i == 0) or (i == 2)) and (e % 2 == 0):
                tabuleiro[i].append(pecaBranca)
            elif (i == 1) and (e % 2 != 0):
                tabuleiro[i].append(pecaBranca)
            elif (i == 5 or i == 7) and (e % 2 != 0):
                tabuleiro[i].append(pecaPreta)
            elif (i == 6) and (e % 2 == 0):
                tabuleiro[i].append(pecaPreta)
            else:
                tabuleiro[i].append(espacoVazio)
    return tabuleiro


def exibe_tabuleiro(m):  # Formata a matriz para parecer um tabuleiro 8x8.
    lateral = '|'
    inferior = '_'
    print('   A  ' ' B  ' ' C  ' ' D  ' ' E  ' ' F  ' ' G  ' ' H')
    for i in range(len(m)):
        print('  ' + inferior * 31)
        print(i + 1, end='')
        for j in range(len(m[i])):
            if j == len(m[i])-1:
                print(lateral, m[i][j], lateral + str(i+1),  end='\n')
            else:
                print(lateral, m[i][j], end=' ')
    print('  ' + inferior * 31)
    print('   A  ' ' B  ' ' C  ' ' D  ' ' E  ' ' F  ' ' G  ' ' H')


def movimento_das_pecas():  # Recebe os valores das posições desejadas para movimentação.
    linhaAtualY = (input("Digite o número da linha atual:"))
    while linhaAtualY.isdigit() != True:
        linhaAtualY = input("Não digitou um número válido. Digite o número da linha atual:")
    linhaAtualY = int(linhaAtualY)
    linhaAtualPadraoTabuleiro = linhaAtualY - 1  # Para impedir erros de interpretação na posição da linha.
    colunaAtualX = input("Digite a letra da coluna atual:")
    linhaFuturaY = input("Digite o número da linha futura:")
    while linhaFuturaY.isdigit() != True:
        linhaFuturaY = input("Não digitou um número válido. Digite o número da linha futura:")
    linhaFuturaY = int(linhaFuturaY)
    linhaFuturaPadraoTabuleiro = linhaFuturaY - 1  # Para impedir erros de interpretação na posição da linha.
    colunaFuturaX = input("Digite a letra da coluna futura:")
    return linhaAtualPadraoTabuleiro, colunaAtualX, linhaFuturaPadraoTabuleiro, colunaFuturaX


def jogo_de_damas():  # Roda o jogo conjuntamente utilizando as demais funções criadas.
    x_matar = 0
    y_matar = 0
    futuro_b_linha = 0
    futuro_b_coluna = 0

    contador = 1
    pecasPretasComidas = 0
    PecasBrancasComidas = 0
    while ((pecasPretasComidas != 12) or (PecasBrancasComidas != 12)):  # Condição de jogo rolando.

        exibe_tabuleiro(tabuleiro)
        print()
        print("Pontuações dos jogadores")
        print("Jogador Branco: %d" % pecasPretasComidas)
        print("Jogador Preto: %d" % PecasBrancasComidas)
        # OS DOIS IFs SÃO PARA DIZER QUEM JOGARÁ PRIMEIRO
        if (contador % 2 != 0):
            print()
            print("Vez do Jogador Branco.")
            print()

            atual_linha, atual_coluna, futura_linha, futura_coluna = (movimento_das_pecas())
            coluna_atual = (dicionarioCoordenadas["%s" % atual_coluna])
            coluna_atual = int(coluna_atual)
            coluna_futura = (dicionarioCoordenadas["%s" % futura_coluna])
            coluna_futura = int(coluna_futura)
            #
            futura_linha_branco = atual_linha + 1  # PARA TESTAR LINHA
            futura_coluna_branco = coluna_atual + 1  # PARA TESTAR COLUNAS
            futura_coluna_branco2 = coluna_atual - 1
            #
            futura_possivel_linha_branco = futura_linha_branco + 1
            futura_possivel_coluna_branco = futura_coluna_branco + 1
            futura_possivel_coluna_branco2 = futura_possivel_coluna_branco - 1

        if (contador % 2 == 0):
            print()
            print("Vez do Jogador Preto.")
            print()

            # PARA FAZER OS MOVIMENTOS DOS DOIS JOGADORES SÓ COM UMA FUNÇÃO
            atual_linha, atual_coluna, futura_linha, futura_coluna = (movimento_das_pecas())
            coluna_atual = (dicionarioCoordenadas["%s" % atual_coluna])  # PUXA O VALOR DO DICIONARIO
            # TRANSFORMA OS VALORES
            coluna_atual = int(coluna_atual)
            coluna_futura = (dicionarioCoordenadas["%s" % futura_coluna])
            coluna_futura = int(coluna_futura)
            #
            futura_linha_preto = atual_linha - 1  # PARA TESTAR SE PODE IR PARA A DIOGONAL POR EXEMPLO (3,1)
            futura_coluna_preto = coluna_atual + 1  # PARA TESTAR A LINHA
            futura_coluna_preto2 = coluna_atual - 1
            #
            futura_possivel_linha_preto = futura_linha_preto - 1
            futura_possivel_coluna_preto = futura_coluna_preto + 1
            futura_possivel_coluna_preto2 = futura_possivel_coluna_preto - 1
        for i in ((tabuleiro)):  # ESSE FOR É PARA LER O TABULEIRO PARA FAZER AS JOGADAS ABAIXO

            if ((atual_linha % 2 == 0) and (
                    coluna_atual % 2 == 0)):  # ESSE IF É PARA PRIMEIRA JOGADA DE B, MAS IRÁ VIRAR PARA P
                if ((futura_linha % 2 == 1) and (coluna_futura % 2 == 1)):  # FUTURA CASA QUE IRÁ

                    if ((tabuleiro[atual_linha][coluna_atual]) == pecaBranca) and (contador % 2 != 0):  # VEZ DEPENDE DO CONTADOR E SÓ UMA JOGADA

                        if ((tabuleiro[futuro_b_linha][futuro_b_coluna]) != pecaPreta):
                            if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]) and (
                                    atual_linha < futura_linha):
                                if (tabuleiro[futura_linha][coluna_futura] != pecaPreta):
                                    tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                    tabuleiro[futura_linha][coluna_futura] = pecaBranca
                                    contador += 1
                                    if ((futura_linha) == 7):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                        (tabuleiro[futura_linha][coluna_futura]) = damaBranca
                                elif (tabuleiro[futura_linha][coluna_futura] == pecaPreta or (
                                        futura_linha == atual_linha)):  # SE O B JOGAR ERRADO
                                    atual_linha, atual_coluna, futura_linha, futura_coluna = (
                                        movimento_das_pecas())  # PEDE AS INFORMAÇÕES PARA JOGAR NOVAMENTE


                    elif ((tabuleiro[atual_linha][coluna_atual]) == pecaPreta) and (contador % 2 == 0):
                        if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]) and (
                                atual_linha > futura_linha):
                            if (tabuleiro[futura_linha][coluna_futura] != pecaBranca):
                                tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                tabuleiro[futura_linha][coluna_futura] = pecaPreta
                                contador += 1
                                if ((futura_linha) == 0):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                    (tabuleiro[futura_linha][coluna_futura]) = damaPreta
                            elif (tabuleiro[futura_linha][coluna_futura] == pecaBranca) or (atual_linha == futura_linha):
                                atual_linha, atual_coluna, futura_linha, futura_coluna = (movimento_das_pecas())

                if ((futura_linha % 2 == 0) and (coluna_futura % 2 == 0)):  # PARA PULAR DUAS CASAS PARA MATAR

                    if coluna_futura - coluna_atual < 0 and tabuleiro[atual_linha][coluna_atual] == pecaPreta:
                        x_matar = atual_linha - 1
                        y_matar = coluna_atual - 1
                    elif coluna_futura - coluna_atual > 0 and tabuleiro[atual_linha][coluna_atual] == pecaPreta:
                        x_matar = atual_linha - 1
                        y_matar = coluna_atual + 1

                    elif coluna_futura - coluna_atual < 0 and tabuleiro[atual_linha][coluna_atual] == pecaBranca:
                        x_matar = atual_linha + 1
                        y_matar = coluna_atual - 1
                    elif coluna_futura - coluna_atual > 0 and tabuleiro[atual_linha][coluna_atual] == pecaBranca:
                        x_matar = atual_linha + 1
                        y_matar = coluna_atual + 1

                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura - 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura - 1

                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura - 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura - 1

                    else:
                        x_matar = atual_linha - 1
                        y_matar = coluna_atual + 1

                    if (tabuleiro[atual_linha][coluna_atual]) == pecaPreta and (contador % 2 == 0):  # PARA MATAR

                        if ((tabuleiro[x_matar][y_matar]) == pecaBranca):  # SABER SE É B
                            if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]):
                                if (tabuleiro[futura_linha][coluna_futura] != pecaBranca):
                                    tabuleiro[x_matar][y_matar] = espacoVazio
                                    tabuleiro[futura_linha][coluna_futura] = pecaPreta
                                    tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                    PecasBrancasComidas += 1
                                    contador += 1
                                    if ((futura_linha) == 0):  # JOGADA DE MATAR EM QUE A PEÇA VIRA RAINHA
                                        (tabuleiro[futura_linha][coluna_futura]) = damaPreta

                    if (tabuleiro[atual_linha][coluna_atual]) == pecaBranca and (contador % 2 != 0):
                        if coluna_futura - coluna_atual < 0:
                            x_matar = atual_linha - 1
                            y_matar = coluna_atual - 1

                        if coluna_futura - coluna_atual > 0:  # PARA O JOGADOR B VOLTAR PARA MATAR
                            x_matar = atual_linha + 1
                            y_matar = coluna_atual + 1
                        if ((tabuleiro[x_matar][y_matar]) == pecaPreta) and (
                                y_matar < 7):  # QUANDO EU TIVER EM UMA POSIÇÃO PAR E MINHA PEÇA PRECISAR COMER PARA TRÁS
                            if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]):
                                if (tabuleiro[futura_linha][coluna_futura] != pecaPreta):
                                    tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                    tabuleiro[futura_linha][coluna_futura] = pecaBranca
                                    tabuleiro[x_matar][y_matar] = espacoVazio
                                    pecasPretasComidas += 1
                                    contador += 1


            # ENTRADA Do Preto ou do Branco
            elif ((atual_linha % 2 == 1) and (coluna_atual % 2 == 1)):  # QUANDO O JOGO COMAÇAR O P VAI SER IMPAR E O B PAR
                if ((futura_linha % 2 == 0) and (coluna_futura % 2 == 0)):  # UMA JOGADA POR VEZ

                    if (tabuleiro[atual_linha][coluna_atual]) == pecaPreta and (contador % 2 == 0):  # JOGADA DE P INICIAL
                        if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]) and (
                                atual_linha > futura_linha):
                            if (tabuleiro[futura_linha][coluna_futura] != pecaBranca):
                                tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                tabuleiro[futura_linha][coluna_futura] = pecaPreta
                                contador += 1
                                if ((futura_linha) == 0):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                    (tabuleiro[futura_linha][coluna_futura]) = damaPreta
                            elif (tabuleiro[futura_linha][coluna_futura] == pecaBranca) or (
                                    atual_linha == futura_linha):  # SE P JOGAR ERRADO
                                atual_linha, atual_coluna, futura_linha, futura_coluna = (movimento_das_pecas())

                    elif (tabuleiro[atual_linha][coluna_atual]) == pecaBranca and (contador % 2 != 0):
                        if ((tabuleiro[atual_linha][coluna_atual]) == pecaBranca) and (
                                contador % 2 != 0):  # VEZ DEPENDE DO CONTADOR
                            if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]) and (
                                    atual_linha < futura_linha):
                                if (tabuleiro[futura_linha][coluna_futura] != pecaPreta):
                                    tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                    tabuleiro[futura_linha][coluna_futura] = pecaBranca
                                    contador += 1
                                    if ((futura_linha) == 7):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                        (tabuleiro[futura_linha][coluna_futura]) = damaBranca
                                elif (tabuleiro[futura_linha][coluna_futura] == pecaPreta) or (
                                        atual_linha == futura_linha):  # SE O B JOGAR ERRADO
                                    atual_linha, atual_coluna, futura_linha, futura_coluna = (
                                        movimento_das_pecas())  # PEDE AS INFORMAÇÕES PARA JOGAR NOVAMENTE

                elif ((futura_linha % 2 == 1) and (coluna_futura % 2 == 1)):  # PARA PULAR DUAS CASAS PARA MATAR E MOVIMENTOS DE MATAR DAS DAMAS (SOMA DOS MOVIMENTOS DE AMBAS AS PEÇAS)


                    if coluna_futura - coluna_atual < 0 and tabuleiro[atual_linha][coluna_atual] == pecaPreta:
                        x_matar = atual_linha - 1
                        y_matar = coluna_atual - 1
                    elif coluna_futura - coluna_atual > 0 and tabuleiro[atual_linha][coluna_atual] == pecaPreta:
                        x_matar = atual_linha - 1
                        y_matar = coluna_atual + 1

                    elif coluna_futura - coluna_atual < 0 and tabuleiro[atual_linha][coluna_atual] == pecaBranca:
                        x_matar = atual_linha + 1
                        y_matar = coluna_atual - 1
                    elif coluna_futura - coluna_atual > 0 and tabuleiro[atual_linha][coluna_atual] == pecaBranca:
                        x_matar = atual_linha + 1
                        y_matar = coluna_atual + 1

                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura - 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaPreta:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura - 1

                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual < 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura + 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha < 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha + 1
                        y_matar = coluna_futura - 1
                    elif coluna_futura - coluna_atual > 0 and futura_linha - atual_linha > 0 and tabuleiro[atual_linha][coluna_atual] == damaBranca:
                        x_matar = futura_linha - 1
                        y_matar = coluna_futura - 1

                    else:
                        x_matar = atual_linha + 1
                        y_matar = coluna_atual + 1

                    if (tabuleiro[atual_linha][coluna_atual]) == pecaBranca and (contador % 2 != 0):

                        if ((tabuleiro[x_matar][y_matar]) == pecaPreta) and (y_matar < 7):
                            if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]):
                                if (tabuleiro[futura_linha][coluna_futura] != pecaPreta):
                                    tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                    tabuleiro[futura_linha][coluna_futura] = pecaBranca
                                    tabuleiro[x_matar][y_matar] = espacoVazio
                                    pecasPretasComidas += 1
                                    contador += 1
                                    if ((futura_linha) == 7):  # JOGADA DE MATAR EM QUE A PEÇA VIRA DAMA
                                        (tabuleiro[futura_linha][coluna_futura]) = damaBranca
                    if (tabuleiro[atual_linha][coluna_atual]) == pecaPreta and (
                            contador % 2 == 0):  # JOGADA PARA MATAR NA VOLTA DA PEÇA
                        if coluna_futura - coluna_atual < 0:
                            x_matar = atual_linha + 1
                            y_matar = coluna_atual + 1

                        else:
                            x_matar = atual_linha + 1
                            y_matar = coluna_atual + 1

                        if (tabuleiro[atual_linha][coluna_atual]) == pecaPreta and (contador % 2 == 0):  # PARA MATAR

                            if ((tabuleiro[x_matar][y_matar]) == pecaBranca):  # SABER SE É B
                                if (tabuleiro[atual_linha][coluna_atual]) != (tabuleiro[futura_linha][coluna_futura]):
                                    if (tabuleiro[futura_linha][coluna_futura] != pecaBranca):
                                        tabuleiro[x_matar][y_matar] = espacoVazio
                                        tabuleiro[futura_linha][coluna_futura] = pecaPreta
                                        tabuleiro[atual_linha][coluna_atual] = espacoVazio
                                        PecasBrancasComidas += 1
                                        contador += 1

    if (pecasPretasComidas) < (PecasBrancasComidas):
        print("O Vencedor é o Jogador Branco!")
        print("Pontuação: ", pecasPretasComidas)
        print("O P PERDEU!")
        print("PONTUAÇÃO: ", PecasBrancasComidas)

    elif (pecasPretasComidas) < (PecasBrancasComidas):
        print("O Vencedor é o Jogador Preto!")
        print("Pontuação: ", PecasBrancasComidas)
        print("O Jogador Branco Perdeu!")
        print("Pontuação: ", pecasPretasComidas)


tabuleiro = cria_tabuleiro()
jogo_de_damas()
