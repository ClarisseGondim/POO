tarefas = []  

def adicionar_tarefa():
    titulo = input("Digite o título da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "status": "Pendente"
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{titulo}' adicionada com sucesso!")


def concluir_tarefa():
    titulo = input("Digite o título da tarefa concluida: ")
    for tarefa in tarefas:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = "Concluída"
            print(f"Tarefa '{titulo}' marcada como concluída!")
            return
    print("Tarefa não encontrada.")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- Tarefas Pendentes ---")
    for tarefa in tarefas:
        if tarefa["status"] == "Pendente":
            print(f"Título: {tarefa['titulo']} | Descrição: {tarefa['descricao']}")

    print("\n--- Tarefas Concluídas ---")
    for tarefa in tarefas:
        if tarefa["status"] == "Concluída":
            print(f"Título: {tarefa['titulo']} | Descrição: {tarefa['descricao']}")
    print()    
