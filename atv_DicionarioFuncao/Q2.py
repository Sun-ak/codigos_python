'''Escreva um programa que contenha um dicionário com a cotação de algumas moedas (por exemplo: dólar, euro, libra), o dicionário deverá ter no mínimo 5 tipos de moeda, por isso, faça uma pesquisa pelas cotações atuais e crie essa estrutura previamente. O programa deve pedir ao usuário uma moeda (você pode exibir um menu com as moedas e seus respectivos preços, para que o usuário consiga escolher) e um valor em reais, e então converter o valor para a moeda escolhida. Exiba o valor convertido e permita que o usuário faça outras conversões até que ele deseje parar.'''

def exibir_moedas(cotacoes):
    print("Moedas disponíveis:")
    for moeda, preco in cotacoes.items():
        print(f"{moeda}: R$ {preco:.2f}")

def converter_moeda(cotacoes):
    while True:
        exibir_moedas(cotacoes)
        moeda = input("Digite a moeda para conversão (ou 'sair' para encerrar): ").strip().lower()
        
        if moeda == 'sair':
            break
        elif moeda in cotacoes:
            valor_reais = float(input("Digite o valor em reais: "))
            valor_convertido = valor_reais / cotacoes[moeda]
            print(f"Valor convertido: {valor_convertido:.2f} {moeda.upper()}")
        else:
            print("Moeda não encontrada.")

def menu_moedas():
    cotacoes = {
        'dólar': 5.25,
        'euro': 5.73,
        'libra': 6.68,
        'iene': 0.036,
        'franco suíço': 5.74
    }
    converter_moeda(cotacoes)

menu_moedas()