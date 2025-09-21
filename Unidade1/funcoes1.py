# Sistema de gerenciamento de estoque 
estoque = []  

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    for item in estoque:
        if item[0] == nome:
            print("Produto já existe!")
            return
    quantidade = int(input("Digite a quantidade: "))
    estoque.append([nome, quantidade])
    print(f"Produto '{nome}' adicionado com {quantidade} unidades.")


def remover_produto():
    nome = input("Digite o nome do produto para remover: ")
    for item in estoque:
        if item[0] == nome:
            estoque.remove(item)
            print(f"Produto '{nome}' removido do estoque.")
            return
    print("Produto não encontrado.")


def atualizar_quantidade():
    nome = input("Digite o nome do produto: ")
    for item in estoque:
        if item[0] == nome:
            quantidade = int(input("Digite a nova quantidade: "))
            item[1] = quantidade
            print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
            return
    print("Produto não encontrado.")


def exibir_estoque():
    if not estoque:
        print("Estoque vazio.")
    else:
        print("\nProdutos no estoque:")
        for item in estoque:
            print(f"- {item[0]}: {item[1]} unidades")
        print()
