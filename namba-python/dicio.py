'''
Dicionarios

-Criando um dicionario com informações sobre pessoa

-Sintaxe:
nome = {"chave" : valor, "chave2" : valor2}
'''

pessoa = {
    "nome" : 'Pedro', 
    "idade" : 30,
    "cidade" : 'São Paulo'
}

# Imprimindo o dicionario pessoa
print(pessoa)

# Acessando um valor especifico utilizando a chave "nome"
print(f'Nome: {pessoa["nome"]}')

# Quero adicionar uma nova informação ao dicionario pessoa
pessoa["profissao"] = 'Programador'

# Alterando um valor de uma chave no dicionario
pessoa["idade"] = 31

# Apagando uma chave do dicionario
del pessoa["cidade"]

print(pessoa)