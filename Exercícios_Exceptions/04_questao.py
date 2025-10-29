''' 4. Implemente um programa que abra um arquivo chamado 
dados.txt (não precisa existir). Use try e finally para 
garantir que uma mensagem de "Encerrando programa" seja 
sempre exibida.'''

try:
    arq = open("dados.txt", "r")

except FileNotFoundError:
    print("\nO arquivo não existe.")

except Exception as e:
    print(f"\nOcorreu um erro inesperado {e}.")

finally:
    print("\nEncerrando Programa.\n")