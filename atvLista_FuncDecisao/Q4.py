'''Crie um programa que peça ao usuário um número de segundos e realize uma contagem regressiva, mostrando o tempo restante a cada segundo até chegar a 0. 
Ao final, exiba a mensagem "Tempo esgotado!". (Pesquise pela biblioteca time e use a função time.sleep(1) para fazer a pausa de 1 segundo entre as contagens.)'''
import time

def contagem_regressiva(segundos):
    while segundos:
        print(f"Tempo restante: {segundos}s")
        time.sleep(1)
        segundos -= 1
    print(f"\nTempo esgotado!\n")

segundos = int(input("Digite o número de segundos para a contagem regressiva: "))
contagem_regressiva(segundos)