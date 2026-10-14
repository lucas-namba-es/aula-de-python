import json 

#parte 1: Gravar e criar um arquivo no formato json

# Estrutura de dados em Python (Dicionario contendo uma lista de dicionario dici<lista<dici2)
# Simulando uma base de dados
dados_biblioteca = {
    "categoria" : "Tecnologia", 
    "livros" : [
        {
            "titulo" : "Entendendo Algoritimos com Python",
            "autor" : "Autor 1",
            "ano_publicacao" : 2026,
            "disponivel" : True
        },
        {
            "titulo" : "Python Fluente",
            "autor" : "Autor 2",
            "ano_publicacao" : 2020,
            "disponivel" : False
        },
        {
            "titulo" : "Java Fluente",
            "autor" : "Autor 67",
            "ano_publicacao" : 1999,
            "disponivel" : False
        }
    ]
}

# Criando e salvando o arquivo 'livros.json' (no disco)
with open('livros.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados_biblioteca, arquivo, indent=4, ensure_ascii= False)

print("Arquivo 'livros.json' foi criado com sucesso!\n")

#Parte 2 - Ler o arquivo JSON do disco / memoria (json.load()) 

# Abrindo o arquivo 'livros.json' e carregando os dados na meória
with open("livros.json", 'r', encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

# Exibindo os dados carregados no console
print("lendo os dados do arquivo json: ")
print(f"Categoria do acervo: {dados_carregados['categoria']}\n")

print('----Lista de Livros----')
for livro in dados_carregados['livros']:
    status = "Disponivel" if livro['disponivel'] else "Emprestado"
    print(f' --{livro['titulo']} | Autor: {livro['autor']} | Ano de Publicação: {livro['ano_publicacao']} - [{status}]\n')

    