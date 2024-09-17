'''Crie um jogo da adivinhação em que o computador escolhe um número aleatório entre 1 e 100 e o usuário tenta adivinhar. O programa deve informar se o número digitado é maior, menor ou igual ao número secreto. O usuário terá apenas 5 tentativas, à medida que o usuário for informando os valores diga quantas tentativas restam.(Você irá precisar utilizar a biblioteca randint).'''

import random

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Número de tentativas
tentativas_restantes = 5

print("Bem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

# Laço while que vai até que as tentativas acabem ou o usuário acerte
while tentativas_restantes > 0:
    # Entrada do usuário
    palpite = int(input("Digite seu palpite: "))
    
    # Verifica se o palpite está correto
    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
    
    # Reduz o número de tentativas restantes
    tentativas_restantes -= 1
    
    if tentativas_restantes > 0:
        print(f"Você ainda tem {tentativas_restantes} tentativas.")
    else:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
