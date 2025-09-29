from datetime import datetime as dt
from random import randint 
class Restaurante:
    def __init__(self, nomeRestaurante= None, tipoCozinha=None,numeroServidos=0):
        
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos = numeroServidos

    def get_nomeRestaurante(self):
        return self.nomeRestaurante
    
    def set_nomeRestaurante(self,novo_restaurante):
        self.nomeRestaurante = novo_restaurante

    def get_tipoCozinha(self):
        return self.tipoCozinha
    
    def set_tipoCozinha(self,novo_tipoCozinha):
        self.set_tipoCozinha = novo_tipoCozinha

    def get_numeroServidos(self):
        return self.numeroServidos 
     
    def set_numeroServidos(self, novo_numero):
        self.numeroServidos = novo_numero

    def get_incrementarNumeroServidos(self, incrementar):
        return self.get_incrementarNumeroServidos
    
    def set_incrementarNumeroServidos(self, incrementar_novo_numero):
        self.numeroServidos += incrementar_novo_numero
        self.set_numeroServidos(self.numeroServidos)
        
        
    def abrirRestaurante(self):
        print("\nRestaurante aberto")
    

class Cliente:
    def __init__(self,restaurante:Restaurante):
        self.numerodeCliente = randint(0, restaurante.get_numeroServidos())
        self.restaurante = restaurante
        
    def __str__(self):
        obj_str = "\n\n###### Informações do CLientes ######\n\n"
        obj_str += f"Numero: {self.numerodeCliente}\n"
        obj_str += f"Restaurante Atendido: {self.restaurante.get_nomeRestaurante()}\n"
        return obj_str
    


restaurante = Restaurante("ClaCla", "PaoDeQueijo") # Instancia de um Restaurante
restaurante1 = Restaurante("JOJO", "Filo") # Instancia de um Restaurante

restaurante.set_nomeRestaurante("Filo")

#exibindo Clientes atendidos antes da Função IncrementarCliente
print(f"\nClientes Atendidos: {restaurante.get_numeroServidos()}\n ")

#Chamando Função para incrementar Clientes Servidos
restaurante.set_incrementarNumeroServidos(10)
restaurante.set_incrementarNumeroServidos(1)

print(f"---Passado um tempo----\n")

#Clientes atendidos apos a implementação da Função 
restaurante.abrirRestaurante()
print(f"Nome do Restaurante: {restaurante1.get_nomeRestaurante()}")
print(f"Tipo de cozinha: {restaurante1.get_tipoCozinha()}")
print(f"Clientes Atendidos : {restaurante.get_numeroServidos()}")




