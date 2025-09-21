class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def descreverRestaurante(self):
        
        return f"\n{self.nomeRestaurante}" + f"\n{self.tipoCozinha}"

    def abrirRestaurante(self):
        
        return print(f"\n Restaurante aberto")
    
    def __str__(self):
       return f"\n {self.nomeRestaurante}\n{self.tipoCozinha}"
    


objeto_restaurante = Restaurante("Dochefe", "DonaRaimunda")
objeto_restaurante1 = Restaurante("Dcasa", "DonaFofa")
objeto_restaurante2 = Restaurante("DonaMaria", "DonaLara")
                                 
obj_exibir = objeto_restaurante.descreverRestaurante()
obj1_exibir = objeto_restaurante1.descreverRestaurante()
obj2_exibir = objeto_restaurante2.abrirRestaurante()


#print(obj_exibir)
#print(obj1_exibir)
#print(obj2_exibir)

print(objeto_restaurante)
print(objeto_restaurante1)
print(objeto_restaurante2)


