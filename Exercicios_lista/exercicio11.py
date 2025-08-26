#Questão 11: Criar um tabuleiro de xadrez vazio e adicionar peças

import numpy as np
tabuleiro = [["[ ]" for _ in range(8)] for _ in range(8)]
tabuleiro[0][0] = "tor"
tabuleiro[0][1] = "cav"
tabuleiro[0][2] = "bis"
tabuleiro[0][3] = "rai"
tabuleiro[0][4] = "rei"
tabuleiro[0][5] = "bis"
tabuleiro[0][6] = "cav"
tabuleiro[0][7] = "tor"
for i in range(8):
    tabuleiro[1][i] = "pea"
    tabuleiro[6][i] = "pea"
    tabuleiro[7][0] = "tor"
    tabuleiro[7][1] = "cav"
    tabuleiro[7][2] = "bis"
    tabuleiro[7][3] = "rai"
    tabuleiro[7][4] = "rei"
    tabuleiro[7][5] = "bis"
    tabuleiro[7][6] = "cav"
    tabuleiro[7][7] = "tor"
for linha in tabuleiro:
    print(" ".join(linha))