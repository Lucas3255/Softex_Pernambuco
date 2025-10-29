'''
 1. Na classe, ContaBancaria, converta saldo para uma atributo privado. 
 Crie um método setter e um getter para acessar e modificar essa atributo, 
 seguindo uma regra lógica (Ex: saldo não pode ser negativo).
'''

import os, time, platform

class ContaBancaria():
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = max(0.0, saldo)
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
            return True
        
        else:
            print("\nErro! O saldo não pode ser negativo.")
            return False

    def depositar(self, valor):
        if valor <= 0:
            print("\nO valor deve ser maior que 0.")
            return False
        
        else:
            novo_saldo = self.__saldo + valor
            if self.set_saldo(novo_saldo):
                print("\nDeposito Realizado!")
                print(f"Saldo Atual: {self.get_saldo():.2f}")
                return True
            return False
        
    def sacar(self, valor):
        if valor <= 0:
            print("\nO valor deve ser maior q 0.")
            return False
        
        elif valor > self.__saldo:
            print(f"\nSaldo Insuficiente!\nSaldo Atual: {self.get_saldo():.2f}")
            return False

        else:
            novo_saldo = self.__saldo - valor
            if self.set_saldo(novo_saldo):
                print("\nSaque Realizado!")
                print(f"Saldo Atual: {self.get_saldo():.2f}")
                return True
            return False
        
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
            print(f"Titular: {conta.titular}\nSaldo: {conta.get_saldo():.2f}")
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
