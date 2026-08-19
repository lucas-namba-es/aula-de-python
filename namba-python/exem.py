'''
Exercicio

Sistema de cadastro de alunos com dicionarios

desenvolva um programa em python para criar um sistema simples de cadastro e consulta de alunos, utilizando m dicionario para armazenar as informações.

O programa devera trabalhar com um dicionario no seguinte formato:

aluno = {
    "Nome" : 'Ana',
    "idade" : 18,
    "curso" : 'engenharia',
    "media" : 8.5
}

Requisitos:
O programa deverá:
1 - Criar um dicionario contendo os dados de um ano: nome, idade, curso e media
2 - Exibir todas as chaves do dicionario utilizando o metodo keys()
3 - Exibir todos os valores utilizando o metodo values()
4 - Exibir os dados completos utilizando o metodo items()
5 - Solicitar a usuario uma chave e utilizar o get() para consulta
    - Caso a chave exista, apresentar o valor correspondente
    - Caso o contrario, apresentar uma mensagem de erro.
6 - Solicitar a usuario uma nova chave (turma) e valor para ser adicionado no dicionario
7 - Solicitar ao usuario uma chave que deseja excluir - (utilizar a função de delele -> del)
8 - Ao final apresentar o dicionario atualizado

'''

aluno = {}

def cadastro():
    nome =  (input('Digite o seu Nome: '))
    idade = int(input('Digite a sua Idade: '))
    curso = (input('Digite o seu Curso: '))
    media = float(input('Digite sua Media: '))

    aluno['nome'] = nome
    aluno['idade'] = idade
    aluno['curso'] = curso
    aluno['media'] = media

    for chave in aluno.keys():
        print(chave)
        
    for valor in aluno.values():
        print(valor)

    for chave, valor in aluno.items():
        print(f"{chave} : {valor}")

def busca()
    print(input("Digite a chave que você deseja achar: "))
    if 


def adicionar():
   add_chave = (input("Digite sua nova chave: ")) 
   add_valor = (input("Digite seu valor: "))

   aluno['add_chave'] = add_valor






cadastro()
adicionar()