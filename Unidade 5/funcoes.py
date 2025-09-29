from abc import ABC, abstractmethod

# ---------------- CARTÃO WEB ----------------

class CartaoWeb(ABC):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        pass


class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Dia dos Namorados, {self.destinatario}! Que seu dia seja cheio de amor!")


class Natal(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}! Que sua vida seja repleta de luz e paz!")


class Aniversario(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Parabéns pelo seu aniversário, {self.destinatario}! Muitas felicidades e sucesso!")


# ---------------- MÉTODO DE PAGAMENTO ----------------

class MetodoPagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass


class CartaoCredito(MetodoPagamento):
    def pagar(self):
        taxa = self.valor * 0.05
        valor_final = self.valor + taxa
        print("\n--- Pagamento com Cartão de Crédito ---")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Taxa (5%):     R$ {taxa:.2f}")
        print(f"Valor final:   R$ {valor_final:.2f}")


class BoletoBancario(MetodoPagamento):
    def pagar(self):
        desconto = self.valor * 0.02
        valor_final = self.valor - desconto
        print("\n--- Pagamento com Boleto Bancário ---")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Desconto (2%):  -R$ {desconto:.2f}")
        print(f"Valor final:    R$ {valor_final:.2f}")


class Pix(MetodoPagamento):
    def pagar(self):
        desconto = 0.0
        valor_final = self.valor - desconto
        print("\n--- Pagamento com Pix ---")
        print(f"Valor original: R$ {self.valor:.2f}")
        print(f"Desconto (0%):  -R$ {desconto:.2f}")
        print(f"Valor final:    R$ {valor_final:.2f}")

