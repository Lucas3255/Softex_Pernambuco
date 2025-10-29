''' 6. Modifique a classe ContaBancaria para que o método sacar 
retorne True se a operação for bem-sucedida e False caso contrário. 
Teste o retorno e imprima mensagens adequadas.'''

import os, time, platform

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor <= 0:
            print("\nO valor deve ser maior que 0.")
            return False
        
        else:
            self.saldo += valor
            print("\nDeposito Realizado!")
            print(f"Saldo Atual: {conta.saldo:.2f}")
            return True
        
    def sacar(self, valor):
        if valor <= 0:
            print("\nO valor deve ser maior q 0.")
            return False
        
        elif valor > self.saldo:
            print(f"\nSaldo Insuficiente!\nSaldo Atual: {conta.saldo:.2f}")
            return False

        else:
            self.saldo -= valor
            print("\nSaque Realizado!")
            print(f"Saldo Atual: {conta.saldo:.2f}")
            return True
        
conta = ContaBancaria("Carlo Eduardo", 2560.15)

# Função de Limpa Tela
def limpaTela():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")

while True:
    try:
        limpaTela()
        valor = 0
        escolha = input("""\n=== Conta Bancaria ===\n\n1. Depositar Money.\n2. Sacar Money.\n3. Ver Saldo.\n4. Sair.\n\n >> """)
        
        if escolha == "1":
            limpaTela()
            valor = float(input("\nQuanto você gostaria de Depositar: "))
            conta.depositar(valor)
            input("\nClique Enter para continuar.")

        elif escolha == "2":
            limpaTela()
            valor = float(input("\nQuanto gostaria de sacar: "))
            conta.sacar(valor)
            input("\nClique Enter para continuar.")
        
        elif escolha == "3":
            print("\n=== Seus Dados ===\n")
            print(f"Titular: {conta.titular}\nSaldo: {conta.saldo:.2f}")
            input("\nClique Enter para continuar.")

        elif escolha == "4":
            limpaTela()
            print("Encerrando Programa...")
            for i in range(6):
                print(" o", end="", flush=True)
                time.sleep(0.25)
            exit()

        else:
            limpaTela()
            print("Erro! Digite uma opção válida.")
            input("\nClique Enter para continuar.")
    
    except ValueError:
        limpaTela()
        print(f"Opção {escolha} é inválida!")
        input("\nClique Enter para continuar.")
