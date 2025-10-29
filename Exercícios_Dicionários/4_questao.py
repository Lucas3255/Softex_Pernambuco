''' 4. Removendo elementos
        Dado o dicionário:
            carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
        Remova a chave "ano" do dicionário.'''

carro = {
    "marca": "Ford",
    "modelo": "Fiesta",
    "ano": 2010
    }

#função responsável por tirar itens de um dicionário.
del(carro["ano"])

print(carro)