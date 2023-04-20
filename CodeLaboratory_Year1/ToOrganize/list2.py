"""
---------------------------------------------------------------------------------------------------
2
Escrever um algoritmo para exibir os múltiplos de 11, a soma e a média 
dos múltiplos de 11, em ordem decrescente (inversa), compreendidos entre
o intervalo: [200 100].
---------------------------------------------------------------------------------------------------
"""
contador, soma, qtd = 200, 0, 0 


print(f'Os multiplos de 11 entre o intervalo de 100 a 200 de forma decrescente são:')
for contador in range (200, 100, -1):    
    if contador % 11 == 0:
        print(f'{contador} é multiplo de 11')
        soma += contador
        qtd += 1

print(f'A soma dos multiplos de 11 é: {soma}')
print(f'A média dos multiplos de 11 é: {soma/qtd: .2f}')
