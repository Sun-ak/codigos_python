'''Faça um programa de inscrição em um concurso no qual o candidato só poderá se inscrever somente se tiver 18 anos ou mais, assim o sistema deverá considerar o ano atual e solicitar, somente, do candidato seu ano de nascimento. Assim, o sistema ficará solicitando o ano de nascimento até que algum candidato possua idade suficiente (Pesquise a biblioteca datetime e date).'''

import datetime

ano_atual = datetime.date.today().year
while True:
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        print('Você está apto a se inscrever no concurso!')
        break
    else:
        print('Você não está apto a se inscrever no concurso, pois ainda não tem 18 anos.')