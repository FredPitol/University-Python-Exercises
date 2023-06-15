import numpy as np 

dset = np.load("/Users/fred/Downloads/dataset.npy")
dset.sort()
print(f"Tamanho do dset: {len(dset)}")
subdset = dset[:50]
print(f"Tamanho do subdset: {len(subdset)}")
quartil1 = subdset[:len(subdset)//4]
q1 = (np.quantile(subdset, 1/4))
print(f"1 quartil {q1:.1f}")
print(subdset)