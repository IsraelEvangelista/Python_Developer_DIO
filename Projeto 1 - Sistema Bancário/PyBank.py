class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo
        self.historico = []

    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        self._saldo += valor
        self.historico.append(("Depósito", valor))
        print("Depósito realizado com sucesso!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        if len(self.historico) - self.historico.count("Saque") >= 3:
            print("Limite de saques diários atingido")
            return
        if valor > 500:
            print("Valor máximo para saque diário é R$ 500,00")
            return
        if valor > self._saldo:
            print("Saldo insuficiente")
            return
        self._saldo -= valor
        self.historico.append(("Saque", valor))
        print("Saque realizado com sucesso!")

    def mostrar_saldo(self):
        return self._saldo

    def extrato(self):
        print(f"{'Operação':<10}{'Valor':<15}{'Saldo':<15}")
        print("=" * 40)
        saldo = 0
        for operacao, valor in self.historico:
            if operacao == "Depósito":
                saldo += valor
                print(f"{operacao:<10}R$ {valor:>7.2f}{' ':<8}R$ {saldo:>7.2f}")
            elif operacao == "Saque":
                saldo -= valor
                print(f"{operacao:<10}R$ {valor:>7.2f}{' ':<8}R$ {saldo:>7.2f}")
        print("=" * 40)
        print(f"{'Saldo atual:':<25}R$ {self._saldo:>7.2f}")

conta = Conta(saldo=2500)
opcao = -1
print("Bem vindo ao banco Python!")
while opcao != 0:
    opcao = int(input(f'''
============== Menu ==============
[1] Saldo 
[2] Sacar 
[3] Depositar 
[4] Extrato 
[0] Sair 
=================================='''))
    if opcao == 1:
        print(f"Saldo disponível: R$ {conta.mostrar_saldo():.2f}")
    elif opcao == 2:
        print("Quanto gostaria de sacar?")
        conta.sacar(float(input()))
    elif opcao == 3:
        print("Quanto gostaria de depositar?")
        conta.depositar(float(input()))
    elif opcao == 4:
        conta.extrato()
else:
    print(f"Obrigado por usar nosso sistema bancário.")
