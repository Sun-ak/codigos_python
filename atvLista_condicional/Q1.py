#Escolha um número de 0 a 100 onde irá definir em que intervalo de número ele estará

num = int(input("Escolha um número de 0 a 100: "))

if num>=0 and num<=25:
    print(f"Seu número é {num} e está entre 0 e 25 ")

elif num>=26 and num<=50:
    print(f"Seu número é {num} e está entre 26 e 50 ")

elif num>=51 and num<=75:
    print(f"Seu número é {num} e está entre 51 e 75 ")

elif num>=76 and num<=100:
    print(f"Seu número é {num} e está entre 76 e 100 ")