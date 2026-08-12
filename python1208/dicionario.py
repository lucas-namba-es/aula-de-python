computador = {'cpu': 'intel', 'ram': '32gigabytes', 'ssd': '1tb'}
print(computador.keys())
print(computador.values())

for chave in computador.keys():
    print(f'chave: {chave} e valor: {computador[chave]}' )



notas = {'Python': 8, 'JavaScript': 6, 'Front': 9.5}
print(notas)

lista = []
for nota in notas.values():
    print(f'Nota  {nota}')
    if nota > 7:
        lista.append(nota)

for chave, valor in notas.items():
    print(f'Key: {chave} | values: {valor}')


aluno = {'nome': 'João'}
print(f'Aluno: {aluno}')
aluno.update({'nome': 'Pedro'})
print(f'Aluno: {aluno}')

