import requests

cep = '08664000'
url = f'https://viacep.com.br/ws/{cep}/json/'

try:
    requisicao = requests.get(url) #retorna um objeto http

    if requisicao.status_code == 200:
        dic_requisicao = requisicao.json()

        print(f'CEP: {dic_requisicao['cep']}')
        print(f'Logradouro: {dic_requisicao['logradouro']}')
        print(f'Bairro: {dic_requisicao['bairro']}')
        print(f'Localidade: {dic_requisicao['localidade']}')
        print(f'UF: {dic_requisicao['uf']}')
        print(f'Região: {dic_requisicao['regiao']}')

    elif requisicao.status_code == 404:
        print('Não foi possivel encontrar o endereço (CEP)')

    elif requisicao.status_code == 500:
        print('Servidor fora do ar')

    else:
        print(requisicao.status_code)
        print(f'ERRO: {requisicao.status_code}')

except ConnectionError as e:
    print(f'Erro de conexão: {e}')
except Exception as e:
    print(f'Erro: {e}')