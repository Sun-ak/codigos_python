'''Crie um programa que receba uma lista de 8 números e exiba a quantidade de
números negativos e a soma dos números positivos.'''

numeros = [0] * 8
quantidade_negativos = 0
soma_positivos = 0

for n in range(8):
    numero = float(input(f"Digite o {n+1}º número: "))
    numeros[n] = numero
    
    if numero < 0:
        quantidade_negativos += 1
    elif numero > 0:
        soma_positivos += numero

print(f"Quantidade de números negativos: {quantidade_negativos}")
print(f"Soma dos números positivos: {soma_positivos:.2f}")