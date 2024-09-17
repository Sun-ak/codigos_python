numeros = []

# Solicita valores do usuário até um número negativo ser inserido
while True:
    valor = int(input("Digite um valor (0 para encerrar): "))
    if valor == 0:
        break
    numeros.append(valor)

# Exibe a lista criada
print("Lista original:", numeros)

# Remove os números pares da lista
numeros_impares = []
for numero in numeros:
    if numero % 2 != 0:
        numeros_impares.append(numero)

# Exibe a lista sem os números pares
print("Lista sem números pares:", numeros_impares)