'''O Sr. Manoel expandiu seus negócios para além dos negócios e agora possui uma loja de conveniências e precisa que você elabore um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente irá usar para pagar as compras, para então calcular e mostrar o valor do troco. Abaixo segue um exemplo de como deverá ser a saída:'''
print("Bem-vindo à Loja do Sr. Manoel")

valorT = 0.0
valorP = float

while valorP != 0:
    valorP = float(input("Digite o preço do item. Para finalizar digite 0: "))
    
    if valorP < 0:
        print("Valor inválido! Digite um preço positivo.")
    elif valorP > 0:
        valorT += valorP

print(f"Total da compra: R$ {valorT:.2f}")

if valorT > 0:
    while True:
        dinheiro = float(input("Digite o valor em dinheiro do pagamento: "))
        
        if dinheiro >= valorT:
            troco = dinheiro - valorT
            print(f"Troco: R$ {troco:.2f} obrigado pela compra")
            break
        elif dinheiro < valorT:
            print("Vai dar calote na mãe >:( ")
            break
        else:
            print(f"Valor insuficiente! Você precisa pagar pelo menos R$ {valorT:.2f}.")
