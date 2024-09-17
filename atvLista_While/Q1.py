'''Faça um programa que solicite do usuário um valor inteiro qualquer, e mostre o quadrado desse número se ele for maior que 10, mostre o cubo se for maior que 5 e mostre a mensagem “limite excedido” para valores maiores que 100, o programa termina assim que for digitado um valor negativo.'''

while True:
    valor = int(input("Digite um valor: "))
    if valor > 100:
        print("O limite foi excedido")

    elif valor > 5 and valor <10:
        valor = valor ** 3
        print(f"O resultado é {valor}")

    elif valor> 10:
        valor = valor**2 
        print(f"O resultado é {valor}")

    elif valor<= 0:
       print("Programa encerrado")
    break