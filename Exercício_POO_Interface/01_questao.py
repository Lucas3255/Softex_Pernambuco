'''
 1. Crie uma interface chamada Pagamento com um método 
 abstrato processar(valor). Depois, crie duas classes 
 (CartaoCredito e Boleto) que implementem a interface. 
 Mostre como chamar processar() para cada uma.
'''

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self, valor):
        pass

class CartaoCredito(Pagamento):
    def __init__(self, titular: str, numero: int):
        self.titular = titular
        self.numero = numero
    
    def processar(self, valor):
        return f"Fatura do Cartão de {valor:.2f} reais."
    
class Boleto(Pagamento):
    def __init__(self, beneficiario):
        self.beneficiario = beneficiario
    
    def processar(self, valor):
        return f"Boleto de {valor:.2f} reais gerado - Vencimento em 5 dias."

cartao = CartaoCredito("Pedro Gonçalves", 5483990223781289)
boleto = Boleto("Lucas Henrique")

print(cartao.processar(796.90))
print(boleto.processar(299.90))
