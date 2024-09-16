#1° Forma de utilizar o while - semelhante ao FOR

contador = 1

while contador <= 5:
    print(contador)
contador = contador + 1 #o mesmo que contador  += 1

print("="*40)

#2° Forma de utilizar enquanto - loop condicional normal
valor = 0

while valor >= 0:
    valor = int(input("Informe um valor qualquer(digite um valor negativo para terminar: )"))

    print(f"Você digitou {valor}")


print("="*40)

#3° Forma de utilizar enquanto - semelhante a estrutura faça...
while True:
    senha =  input("Informe sua senha: ")
    if senha ==  "123":
        print("Parabéns, senha correta!")
        break #forma de encerrar o loop
    else:
        print("Senhas não conferem, tente novamente")


