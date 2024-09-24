'''Desenvolva um programa que leia uma lista de eventos agendados para o mês e permita ao usuário adicionar novos eventos e remover eventos existentes. Exiba a lista atualizada de eventos. Exemplo de saída:'''

def exibir_menu(eventos):
    print("\nMenu de Eventos")
    for i, evento in enumerate(eventos, 1):
        print(f"{i}. {evento}")
    
    print("\n1. Adicionar um novo evento")
    print("2. Remover um evento")
    print("3. Sair")

def adicionar_evento(eventos):
    novo_evento = input("\nDigite o nome do novo evento: ")
    eventos.append(novo_evento)
    print(f"Evento '{novo_evento}' adicionado com sucesso.")

def remover_evento(eventos):
    try:
        posicao = int(input("\nQual a posição do evento a ser removido? "))
        if 1 <= posicao <= len(eventos):
            evento_removido = eventos.pop(posicao - 1)
            print(f"Evento '{evento_removido}' removido com sucesso.")
        else:
            print("Posição inválida.")
    except ValueError:
        print("Por favor, digite um número válido.")

def gerenciar_eventos():
    eventos = ["Ir para a escola."]

    while True:
        exibir_menu(eventos)
        try:
            opcao = int(input("\nEscolha uma opção (1-3): "))
            if opcao == 1:
                adicionar_evento(eventos)
            elif opcao == 2:
                remover_evento(eventos)
            elif opcao == 3:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

gerenciar_eventos()

