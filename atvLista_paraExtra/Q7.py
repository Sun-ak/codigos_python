# O usuário irá digitar dois valores inteiros positivos onde será ditos quantos deles são multiplos simultaneos de 7 e 11

A = int(input("Digite um número positivo: "))
B = int(input("Digite mais um número positivo: "))
rFinal = 0

for intervalo in range (A ,B +1):
    if intervalo % 7 == 0 and intervalo % 11 == 0:
     rFinal = rFinal +1
print(f"Existe(em) {rFinal} número(os) qua são multiplos simultaneos de 7 e 11")