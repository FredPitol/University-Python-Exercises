"""
Modelagem do problema:
EXEMPLO DE TABELA - MATRIZ:
-> COLUNA 0: Matrícula do Aluno (20200000 + 4 dígitos - 1000 - 9999): Por simulação 
-> COLUNA 1: Ler notas [0, 10] dos 50 Alunos:
-> COLUNA 2: Ler notas [0, 10] dos 50 Alunos:
"""

import numpy as np 




linhas, colunas = 50, 3
dset = np.zeros((linhas, colunas))

# Todas as linhas da coluna 0
dset[:, 0] = 20200000 + np.random.choice(np.arange(1000, 10000), linhas, replace=False))
# Toda=s as linhas da coluna 1
dset[:, 1] = np.random.normal(7.0, 1.3, linhas)
dset[:, 2] = np.random.choice(5.0, 1.8, linhas)

print(dset[:,0])
print(dset[:,1])
print(dset[:,2])