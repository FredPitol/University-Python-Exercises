"""
Frederico Pitol -- Sistemas de Informação -- Noturno -- 2022.1
---------------------------------------------------------------------------------------------
20) 
Escreva um algoritmo que leia o salário em reais de vários clientes de um shopping e exiba em
porcentagem a divisão dos clientes por tipo de cartão, conforme a seguir:
✓ Cartão VIP: Maior ou igual a R$ 5.000
✓ Cartão STANDARD: Menor que R$ 5.000
Faça um Menu de opções para o usuário: 1: Cadastrar Cliente ou 0: Sair do Programa.-
---------------------------------------------------------------------------------------------
"""
salario, opcao, qtd_vip, qtd_stan, total = 0,0,0,0,0
while True:
    opcao = int(input('Digite:\n 1 -> para cadastrar cliente\n 0 -> para encerrar o programa\n'))
    if (opcao == 0):
        print('Você saiu do programa')
        break
    elif (opcao == 1):
        salario = float(input('Digite o seu salário:\n'))
        # Tratamento de erro
        if (salario <= 0):
            print('ERRO: Entrada de dados') 
        else: 
            if (salario > 0 and salario < 5000): 
                qtd_stan += 1
                total += 1 
            else:
                qtd_vip += 1
                total += 1
        print(f'Cartões vip {(qtd_vip / total) * 100: .2f}% \nCartões standard {(qtd_stan / total) * 100: .2f}%\n')
    else:
        print('ERRO: Entrada de dados')    
print('O resultado final é:')    
print(f'Cartões vip {(qtd_vip / total) * 100: .2f}% \nCartões standard {(qtd_stan / total) * 100: .2f}%\n')





 

    
    
