from datetime import datetime as dt
from random import randint 

class Usuario:
     def __init__(self, rg= None , cpf= None , nome= None, datanascimento= dt(2002,9,5)):
        self.rg = rg
        self.cpf = cpf
        self.nome = nome
        self.datanascimento = datanascimento

     def get_rg(self):
        return self.rg
     
     def set_rg (self, novo_rg):
        self.rg = novo_rg

     def get_cpf(self):
        return self.cpf
     
     def set_cpf(self, novo_cpf):
        self.cpf= novo_cpf

     def get_nome(self):
        return self.nome
     
     def set_nome(self, novo_nome):
        self.nome= novo_nome

     def get_datanascimento(self):
        return self.datanascimento
     
     def set_datanascimento(self, dia, mes, ano):
        self.datanascimento=dt(ano, mes, dia)



class Conta:
    def __init__(self,usuario:Usuario): 
           self.agencia = randint(888,999)
           self.usuario = usuario
           self.data_abertura = dt.now()
           self.saldo = 0
    def consultar_saldo(self):
        print(f"Saldo da Conta: R${self.saldo}\n\n")

    def depositar(self,valor_deposito):  
         self.saldo += valor_deposito
         print(f"\n\n O deposito de R${valor_deposito} foi realizado com sucesso.\n\n")

    def sacar(self, valor_saque):
          if valor_saque>self.saldo:
           print(f"\nSaque não realizado. \nVocê pode sacar até R${self.saldo}\n")
          else:
           self.saldo -= valor_saque
           print(f"\nSaque de R${valor_saque} realizado com sucesso.\n")

    def transferir(self, valor_stransferencia):
          if valor_stransferencia>self.saldo:
           print(f"\nTransferência não realizado. \nVocê pode transferir até R${self.saldo}\n")
          else:
           self.saldo -= valor_stransferencia

    def __str__(self):
        obj_str = "\n\n###### Dados da Conta ######\n\n"
        obj_str += f"Agência:{self.agencia}\n"
        obj_str += f"Data de Abertura:{self.data_abertura.strftime('%d/%m/%y')}\n"
        obj_str += f"Saldo:R${self.saldo}\n"
        obj_str += f"Nome do usuário:{self.usuario.get_nome()}\n"
        obj_str += f"RG:{self.usuario.get_rg()}\n"
        obj_str += f"CPF:{self.usuario.get_cpf()}\n"
        obj_str += f"data de nascimento:{self.usuario.get_datanascimento().strftime('%d/%m/%y')}\n"
        return obj_str
    

class ContaPoupanca(Conta):
   def __str__(self):
    obj_str = "\n\n###### Dados da Conta Poupanca ######\n\n"
    obj_str += f"Agência:{self.agencia}\n"
    obj_str += f"Data de Abertura:{self.data_abertura.strftime('%d/%m/%y')}\n"
    obj_str += f"Saldo:R${self.saldo}\n"
    obj_str += f"Nome do usuário:{self.usuario.get_nome()}\n"
    obj_str += f"RG:{self.usuario.get_rg()}\n"
    obj_str += f"CPF:{self.usuario.get_cpf()}\n"
    obj_str += f"data de nascimento:{self.usuario.get_datanascimento().strftime('%d/%m/%y')}\n"
    return obj_str
   

class ContaCorrente(Conta):
   pass


class ContaEspecial(ContaCorrente):
   def __init__(self, Usuario, saldo_especial=0):
      def sacar(self, valor_saque):
       if valor_saque>self.saldo+self.saldo_especial:
         print(f"\nSaque não realizado. \nVocê pode sacar até R${self.saldo+saldo_especial}\n")
       else:
         self.sacar -= valor_saque
         print(f"\nSaque de R${valor_saque} realizado com sucesso.\n")



usuario1 = Usuario() #Instanciar com valor padrão
usuario2 = Usuario() #Instanciar com valor padrão



#Solicitação de dados

#nome_usuario1= input("Digite seu nome completo:")
#rg_usuario1= int(input("Digite seu RG:"))
#cpf_usuario1= int(input("Digite seu CPF:"))
#dia_nascimento= int(input("Digite seu dia de nascimento:"))
#mes_nascimento= int(input("Digite seu mes de nascimento:"))
#ano_nascimento= int(input("Digite seu ano de nascimento:"))


usuario1.set_nome("Maria Clara")
usuario1.set_rg(77788899)
usuario1.set_cpf(555666444)
usuario1.set_datanascimento(12,5,2000)


usuario2.set_nome("Carlos Pinto")
usuario2.set_rg(222555111)
usuario2.set_cpf(6664448888)
usuario2.set_datanascimento(17,8,1995)


conta_usuario1 = Conta(usuario1)
conta_usuario2 = ContaPoupanca(usuario2)



print(conta_usuario1)
print(conta_usuario2)





