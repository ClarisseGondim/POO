alunos = {
    "Ana": [8.5, 7.0, 9.2, 6.8],
    "Carlos": [5.5, 6.0, 7.5, 8.0],
    "Mariana": [9.0, 8.5, 10.0, 9.8],
    "Lucas": [6.5, 7.2, 5.8, 6.9],
    "Fernanda": [7.8, 8.2, 7.0, 8.5]
}


def adicionar_aluno():
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        print("Aluno já cadastrado! ")
    else:
        notas = []
        for i in range(1, 5):
            nota = float(input(f"Digite a nota N{i}: "))
            notas.append(nota)
        alunos[nome] = notas
        print(f"Aluno {nome} cadastrado com sucesso!")


def atualizar_notas():
    nome = input("Digite o nome do aluno para atualizar: ")
    if nome in alunos:
        notas = []
        for i in range(1, 5):
            nota = float(input(f"Digite a nova nota N{i}: "))
            notas.append(nota)
        alunos[nome] = notas
        print(f"Notas do aluno {nome} atualizadas com sucesso!")
    else:
        print("Aluno não encontrado.")


def remover_aluno():
    nome = input("Digite o nome do aluno a remover: ")
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido do cadastro.")
    else:
        print("Aluno não encontrado.")


def exibir_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Alunos e Notas ---")
        for nome, notas in alunos.items():
            print(f"{nome}: {notas}")
        print()


def exibir_medias():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n--- Médias dos Alunos ---")
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            print(f"{nome}: média = {media:.2f}")
        print()
