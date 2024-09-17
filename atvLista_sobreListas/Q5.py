numeros = []

# Solicita 5 números ao usuário e armazena na lista
for itens in range(5):
    valor = int(input(f"Digite o {itens+1}º número: "))
    numeros.append(valor)

# Exibe a lista completa
print("Lista completa:", numeros)

# Mostra apenas os números divisíveis por 3
divisiveis_por_3 = []
for numero in numeros:
    if numero % 3 == 0:
        divisiveis_por_3.append(numero)

# Exibe os números divisíveis por 3
print("Números divisíveis por 3:", divisiveis_por_3)