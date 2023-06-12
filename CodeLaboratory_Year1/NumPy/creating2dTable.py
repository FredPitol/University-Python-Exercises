"""
Col 0 - Matricula do aluno 
Col 1 - Ler notas 1 bimestre 
Col 2 - Ler notas 2 bimestre

import numpy as np
# Criando a tabela 

linhas, indice = 50, 0

dataset = numpy.zeros(linhas)

while indice < 5:
    try:
        print(f"Digite a nota do aluno {indice + 1} ")
        dataset[indice] = float(input())
        if(dataset[indice] < 0 or dataset[indice] > 10):
            print("Nota invalida insira um numero entre 0 e 10")
        else:
            indice += 1        
    except:
        print ("Erro de entrada de dados")    
print(f"Média dos alunos: {dataset.mean(): 1f} ")
"""
"""

import numpy as np

dset = np.random.randn(2,3)

data2 = [[1, 2],[3, 4], [5, 6.1]]
dset2 = np.array(data2)

print(f"dset2: {dset2}")
print(f"dset2[1]: {dset2[1]}")
print(f"dset.dtype: {dset2.dtype}")
print(f"dset.shape: {dset2.shape}")
print(f"dset.shape[0]: {dset2.shape[0]}")

"""
"""
dset = np.arange(1,5,1)

print(dset)
"""


import numpy as np 