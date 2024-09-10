'''Escreva um programa que recebe o salário de um funcionário e calcula o imposto
de renda baseado nas seguintes condições:
a. Até R$ 1.900, isento
b. De R$ 1.901 até R$ 2.800, 7.5% de imposto
c. De R$ 2.801 até R$ 3.700, 15% de imposto
d. Acima de R$ 3.700, 22.5% de imposto'''

salário = float(input("Digite o salário do funcionário: "))

if salário <= 1900:
    imposto = 0

elif salário >= 1901 and salário <= 2800:
    imposto = salário * 0.075

elif salário >= 2801 and salário <= 3700:
    imposto = salário * 0.15

elif salário > 3700:
    imposto = salário * 0.225

print(imposto)