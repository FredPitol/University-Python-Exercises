import math

def fibo(n):
    # Calcula a soma de n numeros da seqûencia de fibonacci
    a, b, soma = 0, 1, 0
    for l in range(n):
        soma += a
        a, b = b, a+b
    return soma
# ------------------------------------------------------------
# Recebe o salário bruto numero de dependentes e salário minimo,
# Retorna o salário liquido, total de descontos e valor do vale alimentacao
#-------------------------------------------------------------
def contrac(sbruto, ndepen, sminimo=1100 ):
    inss = sbruto * 0.11
    psaude = sbruto * 0.02
    valiment = sminimo + (sbruto * 0.05 * ndepen)
    tdescon = inss + psaude
    sliquido = sbruto - tdescon
    return sliquido, tdescon, valiment
# ------------------------------------------------------------
# ------------------------------------------------------------
def areacirculo(raio):
    return math.pi * raio**2
# ------------------------------------------------------------
# ------------------------------------------------------------
def vcilindro(raio, altura):
    return areacirculo(raio) * altura 
# ------------------------------------------------------------
