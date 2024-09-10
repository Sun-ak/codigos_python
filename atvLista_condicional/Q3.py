#Desenvolva um algoritmo que receba a idade de uma pessoa e classifique-a daseguinte maneira:
#a. Criança: se idade é menor que 12 anos
#b. Adolescente: se idade entre 12 e 18 anos
#c. Adulto: se idade entre 18 e 60 anos
#d. Idoso: se idade acima de 60 anos

idade = int(input("Digite a sua idade: "))
if idade < 12:
 print("Você é uma criança")
elif idade >= 12 and idade < 18:
    print("Você é adolescente")
elif idade >= 18 and idade < 60:
   print("Você é adulto")
elif idade >= 60:
   print("Você é idoso")
