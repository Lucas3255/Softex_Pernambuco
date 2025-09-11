''' 6. Crie uma classe ContaBancaria com os atributos titular e saldo. 
Adicione um método depositar(valor) que aumenta o saldo e um método 
sacar(valor) que diminui o saldo (se houver saldo suficiente). Teste 
com depósitos e saques.'''

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

conta = ContaBancaria("Carlo Eduardo", 2560.15)

while True:
    valor = 0
    try:
        escolha = int(input("""\n=== Conta Bancaria ===\n
                            1. Depositar Money.\n
                            2. Sacar Money.\n
                            3. Ver Saldo.\n\n >> 
                            """))
        if escolha == 1:
            valor = float(input("\nQuanto você gostaria de Depositar: "))
            conta.saldo += valor
            print("Deposito Realizado!")
            print(f"Saldo Atual: {conta.saldo}")

        elif escolha == 2:
            valor = float(input("\nQuanto gostaria de sacar: "))
            if valor > conta.saldo:
                print(f"Saldo Insuficiente!\nSaldo Atual: {conta.saldo}")
            conta.saldo -= valor
            print("Saque Realizado!")
            print(f"Saldo Atual: {conta.saldo}")

