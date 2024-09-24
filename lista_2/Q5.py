'''Você irá criar uma lista contendo dois valores: “Cara” e “Coroa” Utilizando a biblioteca random e função choice, crie um programa que simule o lançamento de uma moeda. O programa deve sortear entre "cara" e "coroa" exibir o resultado e armazenar esse resultado em uma outra lista. Pergunte ao usuário se ele deseja lançar a moeda novamente, em caso afirmativo refaça as etapas anteriores, em caso negativo, encerre exibindo a lista com todos os resultados'''

import random

def jogar_moeda():
    return random.choice(["Cara", "Coroa"])

def executar_simulador():
    resultados_lancamentos = []
    while True:
        resultado_moeda = jogar_moeda()
        print(f"Resultado: {resultado_moeda}")
        resultados_lancamentos.append(resultado_moeda)

        continuar = input("Deseja lançar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            break
    
    print("Resultados acumulados:", resultados_lancamentos)

executar_simulador()
