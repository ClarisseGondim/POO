class Usuario:
    def __init__(self,nome:str,RG:int,CPF:int,DataNascimento):
        self.nome = nome # Ana Clara
        self.RG = RG # 20019443-00
        self.CPF = CPF # 960.852.369-00
        self.DataNascimento = DataNascimento # 02/08/2000

    def caracteristica_usuario(self):
        usuario_nome = f"\n Nome: {self.nome}"
        usuario_rg = f"\n RG: {self.RG}"
        usuario_cpf = f"\n CPF: {self.CPF}"
        usuario_date = f"\n Data de Nascimento: {self.DataNascimento}"
        return usuario_nome + usuario_rg + usuario_cpf + usuario_date

usuario= Usuario("Ana Clara", 102600, 20022001,"20/02/2000")
usuario_exibir = usuario.caracteristica_usuario()

print(usuario_exibir)
    
