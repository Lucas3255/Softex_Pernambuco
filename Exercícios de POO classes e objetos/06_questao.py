''' 6. Modifique a classe ContaBancaria para que o método sacar 
retorne True se a operação for bem-sucedida e False caso contrário. 
Teste o retorno e imprima mensagens adequadas.'''

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print("\nDeposito Realizado!")
        print(f"Saldo Atual: {conta.saldo:.2f}")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"\nSaldo Insuficiente!\nSaldo Atual: {conta.saldo:.2f}")
        else:
            self.saldo -= valor
            print("\nSaque Realizado!")
            print(f"Saldo Atual: {conta.saldo:.2f}")