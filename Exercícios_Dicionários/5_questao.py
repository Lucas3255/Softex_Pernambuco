''' 5. Verificando existência de uma chave
        Verifique se a chave "telefone" existe no dicionário:
            contato = {"nome": "Ana", "email": "ana@email.com"}'''

contato = {
    "nome": "Ana",
    "email": "ana@email.com"
    }

if "telefone" in contato:
    print(f"\nTelefone está incluso no dicionário:\n{contato}")
else:
    print(f"\nInfelizmente n existe o dado Telefone no dicionário:\n{contato}")