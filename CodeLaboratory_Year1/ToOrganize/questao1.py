import math

def calcula(n):
  f1=math.pi/n+math.pi
  f2=(math.pi**n)-math.pi/(math.e*n)
  return f1,f2

n = int(input("Digite o valor de n: "))
resultado1,resultado2=calcula(n)

print(f'Resultado da func :{resultado1}')
print(f'Resultado da func :{resultado2}')


