animais = ["Cachorro", "Gato", "Ovelha"]
print(type(animais))

print(animais)

#exibindo todos os itens da lista
print("-"*50)
for itens in animais:
    print(itens)

#1° Etapa: Atualizar dados
print("-"*50)
animais[0] = "Coelho"
print(animais)

#2° Etapa: Inserir dados
print("-"*50)

#Forma 1: Usando Append
animais.append("Cavalo")#Irá inserir um dado no fim da lista
print(animais)

#Forma 2: Usando insert
animais.insert(1, "Papagaio")#o Insert precisa de 2 valores, o 1° será o índice que desejo inserir o valor. O 2° é o conteudo que eu quero inserir na lista
print(animais)

#3° Etapa: Excluir dados
print("-"*50)

#Forma 1: usando pop()
animais.pop() #O pop irá excluir o último item da lista
print(animais)

#Forma 2: usando pop() como índice
animais.pop(0)#Aqui iremos escolher qual índice da lista será excluído
print(animais)

#Forma 3: Usando remove
animais.remove("ovelha")#irá remover o item pelo seu conteúdo
print(animais) 