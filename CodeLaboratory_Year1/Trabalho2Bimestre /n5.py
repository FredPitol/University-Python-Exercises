import numpy as np 

dset = np.load("/Users/fred/Documents/GitHub/University-Python-Exercises/CodeLaboratory_Year1/Trabalho2Bimestre /dataset5.npy")

print(len(dset))
"""
Letra A)
Exibir na Tela (Precisão de uma (1) casa decimal: .1f):
Média de Tempo por Modalidade e Geral.

"""
medias = np.mean(dset, axis = 0) 
colunas = dset[:, 1:4]

print (f"Média natação:{medias[1]: .1f} ")
print (f"Média corrida:{medias[2]: .1f} ")
print (f"Média ciclismo:{medias[3]: .1f} ")
print (f"Média geral: {np.mean(colunas): .1f}")
""""
Letra B)
Exibir na Tela as Matrículas:
Vencedor e do Lanterna por Modalidade e Geral.

"""

# Encontra indice da linha
indexMinNat = np.argmin(dset[:,  1])
indexMinCor = np.argmin(dset[:,  2])
indexMinCic = np.argmin(dset[:,  3])
indexMinGeral = np.argmin(colunas)

indexMaxNat = np.argmax(dset[:,  1])
indexMaxCor = np.argmax(dset[:,  2])
indexMaxCic = np.argmax(dset[:,  3])
indexMaxGeral = np.argmax(colunas)

print(f"Natação o atleta com o menor tempo foi, Matricula: {dset[indexMinNat, 0]} ")
print(f"Corrida o atleta com o menor tempo foi, Matricula: {dset[indexMinCor, 0]} ")
print(f"Ciclismo o atleta com o menor tempo foi, Matricula: {dset[indexMinCic, 0]} ")
print(f"Atleta com menor tempo geral {dset[indexMinGeral, 0]}")

print(f"Natação: o atleta com o maior tempo foi, Matricula: {dset[indexMaxNat, 0]} ")
print(f"Corrida: o atleta com o maior tempo foi, Matricula: {dset[indexMaxCor, 0]} ")
print(f"Ciclismo: o atleta com o maior tempo foi, Matricula: {dset[indexMaxCic, 0]} ")
print(f"Atleta com Maior tempo geral {dset[indexMaxGeral, 0]}")


""""

Letra C)
A quantidade: Absoluta e Relativa (%) de Atletas abaixo 
(e inclusive) dos tempos médios de prova por Modalidade e Geral.

"""
# Cria um novo array com valores booleanos respondendo a condicional
abaixoMedNat = dset[:, 1] <= medias[1]
abaixoMedCor = dset[:, 2] <= medias[2]
abaixoMedCic = dset[:, 3] <= medias[3]
abaixoMedGeral = np.sum(abaixoMedCic) + np.sumabaixoMedCor + abaixoMedNat
print(abaixoMedGeral)

print(f"Quantidade absoluta de nadadores a baixo da média: {np.sum(abaixoMedNat)}\nQuantidade relativa: {np.sum(abaixoMedNat) / dset.shape[0] * 100: .2f}% ")
print(f"Quantidade absoluta de corredores a baixo da média: {np.sum(abaixoMedCor)}\nQuantidade relativa: {np.sum(abaixoMedCor) / dset.shape[0] * 100: .2f}% ")
print(f"Quantidade absoluta de ciclistas a baixo da média: {np.sum(abaixoMedCic)}\nQuantidade relativa: {np.sum(abaixoMedCic) / dset.shape[0] * 100: .2f}% ")



# Agora tenho um array com varios zeros e uns basta operá-lo
