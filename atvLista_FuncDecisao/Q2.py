'''Escreva um programa que calcule quantas calorias uma pessoa queimou em uma atividade física. 
O programa deve pedir o tipo de atividade (caminhada, corrida ou ciclismo) e o tempo em minutos. Considere as seguintes taxas de calorias queimadas por minuto:'''

def calcular_calorias(atividade, tempo):
    if atividade == "caminhada":
        return tempo * 5
    elif atividade == "corrida":
        return tempo * 10
    elif atividade == "ciclismo":
        return tempo * 8
    else:
        return None
# Entrada do usuário
atividade = input("Informe o tipo de atividade (caminhada, corrida ou ciclismo): ").lower()
tempo = int(input("Informe o tempo em minutos: "))

# Chamada da função
calorias_queimadas = calcular_calorias(atividade, tempo)

# Verificar e exibir o resultado
if calorias_queimadas is not None:
    print(f"Você queimou {calorias_queimadas} calorias durante {tempo} minutos de {atividade}.")
else:
    print("Atividade inválida.")