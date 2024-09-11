'''Escreva um programa que receba 5 números inteiros, um de cada vez, e, ao final,
exiba o maior número informado.'''

maior_numero = None

for contador in range(5):
    numero = int(input(f"Digite o {contador+1}º número: "))
    
    if maior_numero is None or numero > maior_numero:
        maior_numero = numero

print(f"O maior número informado foi: {maior_numero}")