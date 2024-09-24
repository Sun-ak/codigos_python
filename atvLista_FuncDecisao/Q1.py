'''Escreva um programa que pergunte ao usuário o valor de uma conta em um restaurante e o percentual de gorjeta que ele deseja dar (por exemplo, 10%, 15% ou 20%). O programa deve calcular e exibir o valor da gorjeta e o valor total da conta com a gorjeta incluída.'''

def calcular_gorjeta(valor_conta, percentual_gorjeta):
    if percentual_gorjeta == 10:
        return valor_conta * 0.10
    elif percentual_gorjeta == 15:
        return valor_conta * 0.15
    elif percentual_gorjeta == 20:
        return valor_conta * 0.20
    else:
        return None
# Entrada do usuário
valor_conta = float(input("Informe o valor da conta: R$ "))
percentual_gorjeta = int(input("Informe o percentual de gorjeta (10, 15, 20): "))

# Chamada da função
gorjeta = calcular_gorjeta(valor_conta, percentual_gorjeta)

# Verificar e exibir o resultado
if gorjeta is not None:
    total = valor_conta + gorjeta
    print(f"Gorjeta: R$ {gorjeta:.2f}")
    print(f"Total: R$ {total:.2f}")
else:
    print("Percentual inválido.")