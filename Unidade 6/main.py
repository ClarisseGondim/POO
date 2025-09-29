import funcoes

# ================== Programa Principal ==================

if __name__ == "__main__":
    # Criar veículos
    v1 = funcoes.Veiculo("ABC-1234", "Toyota Corolla", 150.0)
    v2 = funcoes.Veiculo("XYZ-5678", "Honda Civic", 180.0)

    # Alugar veículo
    v1.alugar()
    v1.status()

    # Devolver veículo
    v1.devolver()
    v1.status()

    # Testar encapsulamento da placa
    print("Placa do veículo:", v1.placa)
    v1.placa = "NOV-0000"  # Tentativa de modificar

    # Exibir total de veículos
    funcoes.Veiculo.mostrar_total_veiculos()

    # Preço do aluguel
    dias = 5
    valor = funcoes.Veiculo.calcular_preco_aluguel(dias, v2.diaria)
    print(f"\nO valor do aluguel do {v2.modelo} por {dias} dias é: R${valor:.2f}")

()
