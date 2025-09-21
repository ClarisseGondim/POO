import funcoes3

# Menu principal
def menu():
    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1 - Adicionar tarefa")
        print("2 - Concluir tarefa")
        print("3 - Listar tarefas")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes3.adicionar_tarefa()
        elif opcao == "2":
            funcoes3.concluir_tarefa()
        elif opcao == "3":
            funcoes3.listar_tarefas()
        elif opcao == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")

menu()
