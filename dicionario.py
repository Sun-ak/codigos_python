#criando um dicionario, é basicamente uma lista com indice textual

pessoa = {
    "Nome":"Maria",
    "Idade":20,
    "Endereço":"Avenida 23"
}
print(pessoa)

#Exibindo as chaves utilizando o comando keys() chave = indice
print(pessoa.keys())

#Exibindo os valeores utilizando o comando values() valores = conteudo do indice
print(pessoa.values())

#Exibindo tanto a chave quanto o valor
print(pessoa.items())

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#Realizando operações com dicionário
#Adicionando dados
#Firna 1
pessoa["Peso"] = 69
print(pessoa)

# Forma 2 - usando update()
pessoa.update({"Profissão" : "Padeiro"})

#Removendo dados do dicionário
#Forma 1 - pop()
pessoa.pop("Peso")
print(pessoa)

#forma 2 - del()
del(pessoa["Endereço"])
print(pessoa)