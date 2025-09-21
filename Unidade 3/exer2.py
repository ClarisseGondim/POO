class Conta:
    def __init__(self, agencia:int, usuario, dataAbertura, saldo:float):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def caracteristica_canta(self):  
        conta_agencia = f"\n Agencia: {self.agencia}"
        conta_usuario = f"\n Usuario: {self.usuario}"
        conta_dataAbertura = f"\n Data de abertura: {self.dataAbertura}"
        conta_saldo = f"\n Saldo: {self.saldo}"

        return conta_agencia + conta_usuario + conta_dataAbertura + conta_saldo
    
conta= Conta(105, "Maria do Vale","10/06/2008", 500 )
conta_exibir= conta.caracteristica_canta()
print(conta_exibir)
