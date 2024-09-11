'''Crie um programa que receba um número inteiro n e determine se n é um número
perfeito. Um número perfeito é um número que é igual à soma de seus divisores
próprios positivos (excluindo o próprio número). Exiba uma mensagem indicando
se o número é perfeito ou não. (exemplo de número perfeito : 6, pois a soma de
seus divisores 1 +2 + 3 = 6)'''

n = int(input("Digite um número inteiro: "))

soma = 0
for i in range(1, n):
    if n % i == 0:
        soma += i

if soma == n:
    print(f"{n} é um número perfeito.")
else:
    print(f"{n} não é um número perfeito")


