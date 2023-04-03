"""
Escreva um algoritmo que leia o salário em reais de vários clientes de um shopping e exiba em
porcentagem a divisão dos clientes por tipo de cartão, conforme a seguir:

✓ Cartão VIP: Maior ou igual a R$ 5.000
✓ Cartão STANDARD: Menor que R$ 5.000

Faça um Menu de opções para o usuário: 1: Cadastrar Cliente ou 0: Sair do Programa.

"""

porcentagem_vip, porcentagem_standard, opcao = 0, 0, 0
salario = input(float("Insira o valor do salário:"))
   