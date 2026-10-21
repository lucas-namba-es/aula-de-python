import requests

url = f'http://dummyjson.com/recipes?limit=50'

try:
    resposta = requests.get(url, verify=False)

    if resposta.status_code == 200:

        ing_busca = input('Ingrediente disponivel: ')

        dicionario = resposta.json()

        lista_receitas = dicionario['recipes']

        for receita in lista_receitas:
            lista_ing = receita['ingredients']

            for ingrediente in lista_ing:

                if ing_busca.lower() in ingrediente.lower():
                
                    print('-'*140)
                    print(receita['name'])
                    print(receita['ingredients'])

    elif resposta.status_code == 404:
        print('Endereço não encontrado')

    elif resposta.status_code == 500:
        print('Ocorreu um ERRO no sevidor')      

    else:
        print(f'erro: {resposta.status_code}')  

except ConnectionError as e:
    print('Erro de conexão')

except Exception as e:
    print(f'ERRO: {e}')