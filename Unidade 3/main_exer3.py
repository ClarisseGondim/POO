import funcoes3

usuario = funcoes3.Usuario()

nome_inserir = input("Digite o nome do usuário: ")
rg_inserir = input("Digite o RG: ")
cpf_inserir = input("Digite o CPF: ")
dateNascimento_inserir = input("Digite a data de Nascimento: ")
date_nascimento_formato = datetime.strptime(dateNascimento_inserir, "%d/%m/%Y")

usuario.altere_rg(rg_inserir)
usuario.altere_cpf(cpf_inserir)
usuario.altere_nome(nome_inserir)
usuario.altere_dateNascimento(date_nascimento_formato)

agencia = random.randint(0,999)
dataAbertura = datetime.now()
saldo = float(input("Digite o seu Saldo: "))

conta = Conta(agencia, usuario, dataAbertura, saldo)

print("\n--- Dados da Conta ---")
print(f"Agência: {conta.consulte_agencia()}")
print(f"Data de Abertura: {conta.consulte_dataAbertura().strftime('%d/%m/%Y %H:%M')}")
print(f"Saldo: R$ {conta.consulte_saldo():.2f}")

print("\n--- Dados do Usuário ---")
print(f"Nome: {conta.consulte_usuario().consulte_nome()}")
print(f"RG: {conta.consulte_usuario().consulte_rg()}")
print(f"CPF: {conta.consulte_usuario().consulte_cpf()}")
print(f"Data de Nascimento: {conta.consulte_usuario().consulte_dateNascimento().strftime('%d/%m/%Y')}")
