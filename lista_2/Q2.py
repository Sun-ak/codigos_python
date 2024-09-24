'''Escreva um programa que solicite as notas de um aluno e armazene em uma lista (será preciso digitar zero para terminar), após isso, determine quantos alunos ficaram com a nota acima da média (no caso seria 7). Exiba a quantidade de alunos que tiveram notas acima da média da turma.'''

def receber_notas():
    notas_aluno = []
    while True:
        nota_atual = float(input("Informe a nota (ou 0 para finalizar): "))
        if nota_atual == 0:
            break
        notas_aluno.append(nota_atual)
    return notas_aluno

def contar_acima_media(notas_aluno, valor_media=7):
    acima_media = len([nota for nota in notas_aluno if nota > valor_media])
    return acima_media

def rodar_programa():
    lista_notas = receber_notas()
    acima_da_media = contar_acima_media(lista_notas)
    print(f"Quantidade de alunos com nota acima de 7: {acima_da_media}")

rodar_programa()