"Desenvolva um programa que leia duas listas de números inteiros fornecidas pelo usuário e encontre a interseção entre elas (ou seja, os números que aparecem em ambas as listas). Exiba a lista de números comuns, em ordem crescente."

def obter_numeros():
    numeros = list(map(int, input("Informe os números separados por espaço: ").split()))
    return numeros

def encontrar_intersecao(lista_a, lista_b):
    intersecao = sorted(list(set(lista_a) & set(lista_b)))
    return intersecao

def executar_programa():
    print("Forneça a primeira lista de números:")
    lista_a = obter_numeros()
    print("Forneça a segunda lista de números:")
    lista_b = obter_numeros()
    resultado_intersecao = encontrar_intersecao(lista_a, lista_b)
    print("Números comuns em ordem crescente:", resultado_intersecao)

executar_programa()