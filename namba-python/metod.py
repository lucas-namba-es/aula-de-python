'''
Métodos principais
-keys() - retorna uma "visão" de todas as chaves do dicionario
-Value() - retorna uma "visão" de todos os valores do dicionario
-items() - retorna uma "visão" dos pates de chave-valor como uma tupla
- get() - acessa um valor de uma forma segur (retornado um valor)
'''

carro = {
    "marca" : 'Jeep',
    "modelo" : 'Compass',
    "ano" : 2026
}

# Percorrendo (iterando) um dicionario (for)
for chave in carro.keys():
    print(chave)


# Percirrendo o dicionario obtendo os valores - values()
for valor in carro.values():
    print(valor)

# Percorrendo o dicionario obtendo o par de chave e valor - items()
for chave, valor in carro.items():
    print(f'{chave}:{valor}')

# Acesso ao dicionario com chave inexistente
    print(f'cor: {carro["cor"]}')

 # Acesso a um elemneto do dicionario com metodo get()

    cor = carro.get("cor", "não definido")
    print(f'cor: {cor}')
    print(f'marca: {carro.get("marca")}')