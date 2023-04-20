def fibonacci(n):
    a, b, soma = 0, 1, 0

    for l in range(n):
        soma += a
        a, b = b, a+b

    #print(f"A soma dos {n} primeiros números da sequência de Fibonacci é: {soma}")
    return soma