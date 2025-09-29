import funcoes

# ---------------- PROGRAMA PRINCIPAL ----------------
if __name__ == "__main__":
    print("\n\n=== TESTE CARTÕES WEB ===")
    referencia = funcoes.DiaDosNamorados("Ana")
    referencia.showMessage()

    referencia = funcoes.Natal("Carlos")
    referencia.showMessage()

    referencia = funcoes.Aniversario("João")
    referencia.showMessage()

    # Questão (CartaoWeb):
    # O polimorfismo ocorre porque a variável "referencia" é do tipo CartaoWeb,
    # mas pode armazenar objetos de diferentes subclasses.
    # Quando chamamos o método showMessage(), a versão correspondente a classe instanciada é executada.

    print("\n\n=== SISTEMA DE PAGAMENTOS ===")
    valor = float(input("Digite o valor da compra: R$ "))
    metodo = input("Escolha o método de pagamento (cartao / boleto / pix): ").strip().lower()

    pagamento: funcoes.MetodoPagamento

    if metodo == "cartao":
        pagamento = funcoes.CartaoCredito(valor)
    elif metodo == "boleto":
        pagamento = funcoes.BoletoBancario(valor)
    elif metodo == "pix":
        pagamento = funcoes.Pix(valor)
    else:
        print("Método inválido.")
        exit()

    pagamento.pagar()

    # Questão (MetodoPagamento):
    # O polimorfismo ocorre porque usamos a referência do tipo "MetodoPagamento"
    # para armazenar diferentes tipos de pagamento (CartaoCredito, BoletoBancario, Pix).
    # Cada classe implementa o método pagar() de forma distinta.
    # Ao chamarmos pagamento.pagar(), o Python executa a versão específica da subclasse escolhida.
