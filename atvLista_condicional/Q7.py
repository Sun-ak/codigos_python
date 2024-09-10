'''Desenvolva um programa que receba a nota final e a frequência de um aluno. Se a
nota for maior ou igual a 7 e a frequência maior ou igual a 75%, o aluno é
aprovado. Caso contrário, ele é reprovado.'''

presença = int(input("Digite quantos dias o aluno frrequentou a escola: "))
frequencia = float
nota = float(input("Digite a nota de aluno: "))

frequencia = (presença/200) * 100

if frequencia>= 75 and nota>= 7:
    print(f"Aluno tem {frequencia}% de frequencia e sua nota é {nota}, o aluno está aprovado.")
else:
    print(f"Aluno tem {frequencia}% de frequencia e sua nota é {nota}, o aluno está reprovado.")