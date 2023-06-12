import numpy as np 

dset = np.load("/Users/fred/Documents/GitHub/University-Python-Exercises/CodeLaboratory_Year1/NumPy/Exercise_list_2dVector/dataset5.npy")
mediaCor, mediaCic, mediaTotal, mediaNat = 0,0,0,0


mediaColunasMean = np.mean(dset, axis=0)
mediaGeral = np.mean(dataset )


print("\nLetra A):\nExibir na Tela: Média de Tempo por Modalidade e Geral.\n")
print(f"\n\tMédia natação:{mediaColunasMean[1]: .1f} ")
print(f"\tMédia corrida  : {mediaColunasMean[2]: .1f} ")
print(f"\tMédia ciclismo : {mediaColunasMean[3]: .1f} ")

print("--------------------PAREI AQUI -> Fala média geral-----------------------")



# Média geral = soma de todas as notas / (quantidade de linhas * quantidade colunas)
print(f"\tMédia total    : {mediaTotal / (dset.shape[0] * dset.shape[1]): .1f}\n")

print("\nLetra B):\nExibir na Tela as Matrículas: Vencedor e do Lanterna por Modalidade e Geral.\n")

# Encontra o indice da linha que contem o valor minimo e máximo respectivamente 
lanternaNat = np.argmin(dset[:, 1])
lanternaCor = np.argmin(dset[:, 2])
lanternaCic = np.argmin(dset[:, 3])
vencNat = np.argmax(dset[:, 1])
vencCor = np.argmax(dset[:, 2])
venCic = np.argmax(dset[:, 3])

# Somando todas as notas e guardando em novo array


# Fatiando array para comparar todas as notas sem a matricula
todasNotas = dset[:, 1:4]
venGeral = np.argmax(todasNotas)
lanternaGeral = np.argmin(todasNotas)

# Printa os valores usando o indice da linha e qual
# coluna daquela linha queremos mostrar como argumento

print(f"\tVencedor da categoria natação : {dset[vencNat, 0]} ")
print(f"\tVencedor da categoria corrida : {dset[vencCor, 0]} ")
print(f"\tVencedor da categoria ciclismo: {dset[venCic, 0]} \n")
print(f"\tPerdedor da categoria natação : {dset[lanternaNat, 0]} ")
print(f"\tPerdedor da categoria corrida : {dset[lanternaCor, 0]}")
print(f"\tPerdedor da categoria ciclismo: {dset[lanternaCic, 0]} \n")

# Somando 3 colunas com os resultados
somaResultados = np.sum(dset[: , 1:3 ])  

print(f"\tVencedor geral: {dset[venGeral, 0]} ")
print(f"\tLanterna geral: {dset[lanternaGeral, 0]} \n")

print("\nLetra C):\nA quantidade: Absoluta e Relativa (%) de Atletas abaixo (e inclusive) dos tempos médios de prova por Modalidade e Geral\n")
print("\nLetra D):\nPesquisar e exibir todos os dados de um atleta por sua matrícula:\n")
print("\nLetra E):\nExibir uma lista com os dados completos dos 5 melhores atletas:\n")



