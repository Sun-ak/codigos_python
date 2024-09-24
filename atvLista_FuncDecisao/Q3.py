'''Crie um programa que permita ao usuário jogar "Pedra, Papel e Tesoura" contra o computador. 
O programa deve gerar uma escolha aleatória (entre 1, 2 e 3 representando pedra, papel e tesoura, respectivamente) e pedir que o usuário faça sua escolha (também entre 1, 2 e 3).
O programa deve determinar o vencedor com base nas seguintes regras:'''
import random

def jogar():
    while True:
        print("Escolha uma das opções:")
        print("1. Pedra")
        print("2. Papel")
        print("3. Tesoura")
        escolhas = ["Pedra", "Papel", "Tesoura"]
        escolha_computador = random.randint(1, 3)
        escolha_usuario = int(input("Digite o número da sua escolha: "))
        print(f"Você escolheu: {escolhas[escolha_usuario - 1]}")
        print(f"O computador escolheu: {escolhas[escolha_computador - 1]}")
        if escolha_usuario == escolha_computador:
            print("Empate!")
        elif (escolha_usuario == 1 and escolha_computador == 3) or \
             (escolha_usuario == 2 and escolha_computador == 1) or \
             (escolha_usuario == 3 and escolha_computador == 2):
            print("Você venceu!")
        else:
            print("O computador venceu!")
        jogar_novamente = input("Deseja jogar novamente? (s/n): ").lower()#Coloquei para adicionar se o jogador quer jogar dnv, lower é utilizado para converter todos os caracteres de uma string para letras minúsculas
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break
jogar()