'''
 4. Crie as classes Time e Jogador. Um Jogador tem nome e posição 
 como atributos, enquanto Time agrega jogadores em uma lista.
'''

class Jogador():
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __str__(self):
        return f"{self.nome}: {self.posicao}"

class Time():
    def __init__(self, nome):
        self.nome = nome
        self.jogadores = []

    def adicionarJogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"{jogador.nome} agora é da {self.nome}")

    def listarJogadores(self):
        print(f"\nJogadores da {self.nome}:")
        for i in self.jogadores:
            print(f"- {i}")

jogador1 = Jogador("Vinícios", "Atacante")
jogador2 = Jogador("Casemiro", "Volante")
jogador3 = Jogador("Alisson", "Goleiro")

time = Time("Seleção Brasileira")

time.adicionarJogador(jogador1)
time.adicionarJogador(jogador2)
time.adicionarJogador(jogador3)

time.listarJogadores()
