#Será sorteado um número de 1 a 6 10 vezes e será mostrado quantas vezes esses números apareceram
import random

contadores = {i: 0 for i in range(1, 7)}

for _ in range(10):
    resultado = random.randint(1, 6)  
    contadores[resultado] += 1       

print("Resultados dos lançamentos:")
for numero, contagem in contadores.items():
    print(f"Número {numero} foi sorteado {contagem} vezes.")