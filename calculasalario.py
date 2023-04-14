
import lib
sbruto = float(input("Digite o salário bruto: "))
ndepen = float(input("Digite o número de dependentes: "))
sminimo = float(input("Digite o valor do salário mínimo atualizado: "))
sliquido, tdescon, valiment = lib.contrac(sbruto, ndepen, sminimo)
print(f"Salário líquido: {sliquido:.2f}")
print(f"Total de descontos: {tdescon:.2f}")
print(f"Valor do vale alimentação: {valiment:.2f}")
