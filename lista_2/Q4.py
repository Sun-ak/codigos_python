'''Crie um jogo em que uma lista de palavras é apresentada ao usuário, em seguida essa lista será embaralhada e não será mais mostrada ao usuário. Após isso, o programa deverá escolher uma palavra aleatória da lista, exibir essa palavra e perguntar ao usuário em qual posição se encontra essa palavra, o usuário terá 3 chances para acertar, caso o usuário erre exiba uma mensagem que ele errou e diga quantas tentativas restam, se terminar as tentativas e o usuário não acertar informe a posição, caso acerte exiba uma mensagem de parabéns. Em qualquer das situações, ao terminar o jogo exiba a lista embaralhada. (Não esqueça de informar o usuário que a lista começa com a posição 0 e vai até 14, pois a lista possui 15 itens)

Sugestão de listas de palavras que poderão ser usadas
animais = [ 'leão', 'tigre', 'elefante', 'girafa', 'zebra', 'macaco', 'panda', 'hipopotamo', 'leopardo', 'canguru', 'urso', 'coelho', 'cavalo', 'pinguim', 'lobo' ]
frutas = [ 'maçã', 'banana', 'laranja', 'morango', 'uva', 'abacaxi', 'kiwi', 'manga', 'pera', 'melancia', 'framboesa', 'nectarina', 'carambola', 'figo', 'amora' ]
paises = [ 'Brasil', 'Canadá', 'Japão', 'Austrália', 'França', 'Índia', 'México', 'Itália', 'Egito', 'Argentina', 'Alemanha', 'China', 'Itália', 'Reino Unido', 'Noruega' ]
cores = [ 'vermelho', 'azul', 'verde', 'amarelo', 'laranja', 'roxo', 'rosa', 'marrom', 'preto', 'branco', 'cinza', 'turquesa', 'bege', 'lilás', 'prata' ] 
esportes = [ 'futebol', 'basquete', 'natação', 'tênis', 'vôlei', 'corrida', 'rugby', 'golfe', 'ciclismo', 'boxe', 'esgrima', 'handebol', 'karate', 'skate', 'surfe' ]

Funções que serão usadas no algoritmo:
Para embaralhar uma palavra use a função shuffle da biblioteca random.
Para escolher uma palavra aleatória use a função choice da biblioteca random.
Para pegar o índice da palavra aleatória escolhida, use a função index usada em listas.'''

import random

def misturar_palavras(lista_palavras):
    random.shuffle(lista_palavras)
    return lista_palavras

def iniciar_jogo(lista_opcoes):
    lista_misturada = misturar_palavras(lista_opcoes[:])  # Cópia da lista
    palavra_escolhida = random.choice(lista_misturada)
    posicao_correta = lista_misturada.index(palavra_escolhida)

    print(f"Tente adivinhar a posição da palavra '{palavra_escolhida}' na lista.")
    print("A lista vai de 0 a 14.")
    
    tentativas_restantes = 3
    while tentativas_restantes > 0:
        try:
            resposta_usuario = int(input("Digite a posição: "))
            if resposta_usuario == posicao_correta:
                print("Parabéns, você acertou!")
                break
            else:
                tentativas_restantes -= 1
                print(f"Erro! Tentativas restantes: {tentativas_restantes}")
        except ValueError:
            print("Insira um número válido.")
    
    if tentativas_restantes == 0:
        print(f"As tentativas acabaram! A palavra estava na posição {posicao_correta}.")
    
    print("Lista embaralhada:", lista_misturada)

def jogar_palavras():
    frutas = ['maçã', 'banana', 'laranja', 'morango', 'uva', 'abacaxi', 'kiwi', 'manga', 'pera', 'melancia',
              'framboesa', 'nectarina', 'carambola', 'figo', 'amora']
    iniciar_jogo(frutas)

jogar_palavras()