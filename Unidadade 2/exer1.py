class Carro:
    def __init__(self, marca, modelo, ano, cor): 
        self.marca = marca #"Fiat"
        self.modelo = modelo #"Mobi"
        self.ano = ano #"2024" 
        self.cor = cor #"Branco"

    def caracteristicas_carro(self): 
        objeto_marca =f"\n{self.marca}"
        objeto_modelo =f"\n{self.modelo}" 
        objeto_ano =f"\n{self.ano}"
        objeto_cor =f"\n{self.cor}"

        return objeto_marca + objeto_modelo + objeto_ano + objeto_cor


carro = Carro("Fiat", "Mobi",2024, "Branco")
carro1 = Carro("Hyundai","Creta", 2025, "Cinza")

objeto_carro1= carro1.caracteristicas_carro()
objeto_carro = carro.caracteristicas_carro()
print(objeto_carro)
print(objeto_carro1)
