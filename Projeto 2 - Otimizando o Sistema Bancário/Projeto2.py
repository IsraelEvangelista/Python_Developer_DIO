# Lista para armazenar os usuários e contas
usuarios = []
contas = []

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        
def listar_contas():
    cpf = input("Digite o CPF do usuário para listar as contas (apenas números): ")
    usuario = None
    for usr in usuarios:
        if usr.cpf == cpf:
            usuario = usr
            break
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return
    print(f"Contas do usuário {usuario.nome}:")
    for conta in contas:
        if conta.usuario == usuario:
            print(f"Agência: {conta.agencia}, Número da conta: {conta.numero}")

def criar_usuario():
    global usuarios
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    cpf = input("Digite o CPF do usuário (apenas números): ")
    endereco = input("Digite o endereço do usuário (formato: logadouro, nro - bairro - cidade/sigla estado): ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("Erro: Já existe um usuário com este CPF.")
            return
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

class Conta:
    def __init__(self, agencia, numero, usuario, saldo=0):
        self.agencia = agencia
        self.numero = numero
        self.usuario = usuario
        self.saldo = saldo
        self.extrato = []

def criar_conta():
    global contas
    agencia = "0001"
    cpf = input("Digite o CPF do usuário para criar a conta (apenas números): ")
    usuario = None
    for usr in usuarios:
        if usr.cpf == cpf:
            usuario = usr
            break
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return
    numero = len(contas) + 1
    nova_conta = Conta(agencia, numero, usuario)
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Número da conta: {numero}")

def depositar():
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do depósito: "))
    for conta in contas:
        if conta.numero == numero:
            if valor <= 0:
                print("Valor inválido")
                return
            conta.saldo += valor
            conta.extrato.append(("Depósito", valor))
            print("Depósito realizado com sucesso!")
            return
    print("Conta não encontrada")

def sacar():
    numero = int(input("Digite o número da conta: "))
    valor = float(input("Digite o valor do saque: "))
    for conta in contas:
        if conta.numero == numero:
            if valor <= 0:
                print("Valor inválido")
                return
            if len([op for op, _ in conta.extrato if op == "Saque"]) >= 3:
                print("Limite de saques diários atingido")
                return
            if valor > 500:
                print("Valor máximo para saque diário é R$ 500,00")
                return
            if valor > conta.saldo:
                print("Saldo insuficiente")
                return
            conta.saldo -= valor
            conta.extrato.append(("Saque", valor))
            print("Saque realizado com sucesso!")
            return
    print("Conta não encontrada")

def extrato():
    numero = int(input("Digite o número da conta: "))
    for conta in contas:
        if conta.numero == numero:
            print(f"{'Operação':<10}{'Valor':<15}{'Saldo':<15}")
            print("=" * 40)
            saldo = 0
            for operacao, valor in conta.extrato:
                if operacao == "Depósito":
                    saldo += valor
                    print(f"{operacao:<10}R$ {valor:>7.2f}{' ':<8}R$ {saldo:>7.2f}")
                elif operacao == "Saque":
                    saldo -= valor
                    print(f"{operacao:<10}R$ {valor:>7.2f}{' ':<8}R$ {saldo:>7.2f}")
            print("=" * 40)
            print(f"{'Saldo atual:':<25}R$ {conta.saldo:>7.2f}")
            return
    print("Conta não encontrada")

# Programa principal
opcao = -1
print("Bem vindo ao banco Python!")
while opcao != 0:
    print('''
============== Menu ==============
[1] Criar usuário
[2] Criar conta
[3] Saldo 
[4] Sacar 
[5] Depositar 
[6] Extrato 
[7] Listar contas
[0] Sair 
==================================''')
    opcao = int(input())
    if opcao == 1:
        criar_usuario()
    elif opcao == 2:
        criar_conta()
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        sacar()
    elif opcao == 5:
        depositar()
    elif opcao == 6:
        extrato()
    elif opcao == 7:
        listar_contas()
else:
    print(f"Obrigado por usar nosso sistema bancário.")
