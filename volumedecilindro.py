
import lib

raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
volume = lib.vcilindro(raio, altura)
print(f"O volume do cilindro é de {volume:.2f} metros cubicos")
