import random

numero = random.randint(1, 10)
tentativas = 0

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número entre 1 e 10.")

while True:
    tentativa = int(input("Digite seu palpite: "))
    tentativas += 1
    if tentativa == numero:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
    else:
        print("Errado. Tente novamente.")
