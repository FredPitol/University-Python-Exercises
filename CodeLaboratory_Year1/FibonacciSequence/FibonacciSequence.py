import lib

n = int(input("Digite quantos números da sequência de fibonnaci você quer somar: "))
if n < 0:    
    print("Número inválido")
elif n == 0:
    print("0")   
elif n == 1:
    print("O primeiro numero de fibonacci é 0")   
else:
    print(f"A soma dos {n} primeiros números da sequência de Fibonacci é ", end="")
    print(lib.fibo(n))
