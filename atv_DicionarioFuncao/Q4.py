'''Escreva uma função chamada gerar_numeros_aleatorios que receba dois números, inicio e fim, e retorne um número aleatório entre esses dois valores. O programa deve solicitar os limites ao usuário e exibir o número aleatório gerado. O resultado obtido da função deverá ser armazenado em uma lista, e no final de tudo a lista deverá ser exibida com todos os valores. O usuário deverá realizar essa operação 5 vezes. (Utilize o método randint da biblioteca random)'''

import random

def gerar_numeros_aleatorios(inicio, fim):
    return random.randint(inicio, fim)

def menu_numeros_aleatorios():
    numeros_gerados = []
    for _ in range(5):
        inicio = int(input("Digite o limite inferior: "))
        fim = int(input("Digite o limite superior: "))
        numero = gerar_numeros_aleatorios(inicio, fim)
        numeros_gerados.append(numero)
        print(f"Número aleatório gerado: {numero}")
    print("Números gerados:", numeros_gerados)

menu_numeros_aleatorios()