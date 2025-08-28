#Questão 11: Criar um tabuleiro de xadrez vazio e adicionar peças

import numpy as np

# Cria um tabuleiro 8x8 vazio usando list comprehension
tabuleiro = [['[ ]' for _ in range(8)] for _ in range(8)]

# Adiciona as peças brancas e pretas nas posições iniciais

# Peças pretas
tabuleiro[0][0] = 'tor'
tabuleiro[0][1] = 'cav'
tabuleiro[0][2] = 'bis'
tabuleiro[0][3] = 'rai'
tabuleiro[0][4] = 'rei'
tabuleiro[0][5] = 'bis'
tabuleiro[0][6] = 'cav'
tabuleiro[0][7] = 'tor'
tabuleiro[1][0] = 'pea'
tabuleiro[1][1] = 'pea'
tabuleiro[1][2] = 'pea'
tabuleiro[1][3] = 'pea'
tabuleiro[1][4] = 'pea'
tabuleiro[1][5] = 'pea'
tabuleiro[1][6] = 'pea'
tabuleiro[1][7] = 'pea'

# Peças brancas
tabuleiro[7][0] = 'tor'
tabuleiro[7][1] = 'cav'
tabuleiro[7][2] = 'bis'
tabuleiro[7][3] = 'rai'
tabuleiro[7][4] = 'rei'
tabuleiro[7][5] = 'bis'
tabuleiro[7][6] = 'cav'
tabuleiro[7][7] = 'tor'
tabuleiro[6][0] = 'pea'
tabuleiro[6][1] = 'pea'
tabuleiro[6][2] = 'pea'
tabuleiro[6][3] = 'pea'
tabuleiro[6][4] = 'pea'
tabuleiro[6][5] = 'pea'
tabuleiro[6][6] = 'pea'
tabuleiro[6][7] = 'pea'

# Imprime o tabuleiro usando a biblioteca numpy
tab_xadrez = np.array(tabuleiro)
print(tab_xadrez)