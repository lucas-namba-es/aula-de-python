import requests

url = 'http://pokeapi.co/api/v2/pokemon'
cont = 1

response = requests.get(url)

dados = response.json()

lista = dados['results']

for pokemon in lista:
        print(f'{cont} - {pokemon['name']}')
        cont+=1