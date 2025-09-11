''' 9. Crie uma função sacar(saldo, valor) que:
    - Lance (raise) uma exceção personalizada SaldoInsuficienteError 
    se o valor for maior que o saldo.
    - Caso contrário, retorne o novo saldo. Teste a função dentro 
    de um try-except e exiba uma mensagem apropriada ao usuário.'''

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        mensagem = f"Saldo Insuficiente!\n Saldo Atual: {saldo_atual:.2f}\n Valor de Saque: {valor_saque:.2f}\n"

        super().__init__(mensagem)
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque

def sacar(saldo, valor):
    if valor <= 0:
        raise ValueError("O valor de saque deve ser positivo!")
    
    elif valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
    
    else:
        novo_saldo = saldo - valor
        return novo_saldo

#===============================================================

while True:
    try:
        saldoConta = 3507.50
        valorSacar = float(input("\nQual valor gostaria de sacar: "))

        novo_saldo = sacar(saldoConta, valorSacar)
        print("\nSaque Realizado!")
        print(f"Saldo Atual: {novo_saldo:.2f}")
        break

    except ValueError:
        print("Digite apenas números.")

    except SaldoInsuficienteError as e:
        print(e)