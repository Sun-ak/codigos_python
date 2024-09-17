objetos = ("lápis", "borracha", "caderno")
print(objetos[1]) #Irei exibir o item na posição 1, tendo em vista que toda coleção se inicia em 0

print(type(objetos)) #irá mostrar o tipo da variável

print(objetos) #exibindo todos os itens de uma só vez

print("-"*50)

for item in range (0,3):
    print(objetos[item], end=", ")

#Exibindo todos os itens da tupla sem a função range
print("")
print("-"*50)
for elementos in  objetos:
    print(elementos)
