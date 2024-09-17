'''Fazer um algoritmo que preencha uma lista (pode ser valores fixos ou solicitados pelo usuário) 
com 10 elementos inteiros e verifique a existência de elementos iguais a 3, mostrando as posições(índices) em que apareceram.'''

lista = [int(input(f"Digite o {i+1}º número: ")) 
    for i in range(10)]

posicao = []
i = 0

for valor in lista:
    if valor == 3:
        posicao.append(i)
    i += 1

if posicao:
    print("O número 3 foi encontrado nas posições: {}".format(posicao))
else:
    print("O número 3 não foi encontrado na lista.")