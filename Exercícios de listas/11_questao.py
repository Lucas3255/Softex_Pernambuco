''' 11- Usando list comprehension, crie um tabuleiro de xadrez vazio e depois 
adicione todas as peças do jogo na posição inicial. Para melhorar a visualização 
do tabuleiro, identifique as posições do tabuleiro da seguinte forma:
    [ ] - para posições vazias
    tor - para a torre
    cav - para o cavalo
    bis - para o bispo
    rai - para a rainha
    rei - para o rei
    pea - para o peão
Por fim imprima o tabuleiro na tela, deixando cada linha da matriz abaixo da outra. 
(Dica você pode usar a biblioteca numpy para auxiliar na impressão da matriz)'''

tabuleiro = [['[ ]' for i in range(8)] for j in range(8)]

linhaPea = [pea] * 8

tabuleiro[0] = ["tor", "cav", "bis", "rai", "rei", "bis", "cav", "tor"]
tabuleiro[1] = linhaPea
tabuleiro[6] = linhaPea
tabuleiro[7] = ["tor", "cav", "bis", "rei", "rai", "bis", "cav", "tor"]

print("")
for linha in tabuleiro:
    print(' '.join(linha))

print("")
