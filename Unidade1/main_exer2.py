import funcoes2

# Menu_principal
def menu():
    while True:
        print("\n--- Sistema de Cadastro de Alunos ---")
        print("1 - Adicionar aluno")
        print("2 - Atualizar notas de um aluno")
        print("3 - Remover aluno")
        print("4 - Exibir todos os alunos e suas notas")
        print("5 - Calcular e exibir médias")
        print("6 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcoes2.adicionar_aluno()
        elif opcao == "2":
            funcoes2.atualizar_notas()
        elif opcao == "3":
            funcoes2.remover_aluno()
        elif opcao == "4":
            funcoes2.exibir_alunos()
        elif opcao == "5":
            funcoes2.exibir_medias()
        elif opcao == "6":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


menu()
