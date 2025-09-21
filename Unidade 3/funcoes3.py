from datetime import datetime
import random


class Usuario:
    def __init__(self, nome:str ="Sem nome", rg:int = 000000-0, cpf:int = 0000000.0, dateNascimento = None):
        self.nome = nome
        self.rg = rg
        self.cpf = cpf
        self.dateNascimento = dateNascimento if dateNascimento else datetime.now()


    def consulte_nome(self):
      return self.nome
    
    def consulte_rg(self):
        return self.rg
    
    def consulte_cpf(self):
        return self.cpf
    
    def consulte_dateNascimento(self):
        return self.dateNascimento

    def altere_rg(self, rg):
        self.rg = rg
    def altere_cpf(self, cpf):
        self.cpf = cpf
    def altere_nome(self, nome):
        self.nome = nome
    def altere_dateNascimento(self, dateNascimento):
        self.dateNascimento = dateNascimento

    
class Conta:

    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    # Getters
    def consulte_agencia(self):
        return self.agencia

    def consulte_usuario(self):
        return self.usuario

    def consulte_dataAbertura(self):
        return self.dataAbertura

    def consulte_saldo(self):
        return self.saldo
