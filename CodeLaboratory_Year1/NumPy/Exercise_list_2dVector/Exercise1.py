import numpy as np 
dset = np.load("/Users/fred/Documents/GitHub/University-Python-Exercises/CodeLaboratory_Year1/NumPy/Exercise_list_2dVector/dataset1.npy")
print(dset[:5,:])

print(f"\n10 primeiros funcionarios: \n")
for i, f in enumerate(dset[:10]):
    print(f"Funcionario Nº:{i + 1}")
    print(f"\nMatricula: {f[0]: .0f}\t")
    print(f"Salario bruto: {f[1]: .2f}\t")
    print(f"Plano de saude [1]Sim [2]Não: {f[2]: .0f}")
    print(f"Numero de dependentes: {f[3]: .0f}\n") 
    