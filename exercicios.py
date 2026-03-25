#exercicio1

# n = int(input('Número: '))

# match n: #switch
#     case 1 | 7  :
#         print('Hoje é final de semana.')
#     case 2 | 3 | 4 | 5 | 6 :
#         print('Hoje é dia comercial.')
#     case _: #default
#         print('Dia invalido.')

#exercicio2

# idade = int(input("coloque sua idade: "))

# if 0 < idade <= 12:
#     print('Criança')
# elif 12 < idade <= 17:
#     print('Adolescente')
# elif 17 < idade <= 59:
#     print("Adulto")
# elif idade >=60:
#     print('Idoso')
# else:
#     print('Idade inválida')

#exercicio3

# nome_aluno = str(input('Digite o nome do aluno: '))
# n1 = float(input('Digite sua nota 1: '))
# n2 = float(input('Digite sua nota 2: '))
# media_final = (n1+n2)/2

# if media_final >= 7:
#     print('aprovado')
# elif media_final <= 5:
#     print('reprovado')
# else:
#     print('recuperação')

#exercicio4

# dia = str(input('Dia atual: ')).lower().strip()
# placa = int(input('Digite o final de sua placa: '))


# match dia:
#     case 'segunda' | 'terça' | 'quarta' | 'quinta' | 'sexta' :
#         if placa == 1 or placa == 2:
#             print('Seu carro está proibido de circular hoje.')
#         else:
#             print('Seu carro está livre para circular hoje.')
#     case 'terça' :
#         if placa == 3 or placa == 4:
#             print('Seu carro está proibido de circular hoje.')
#         else:
#             print('Seu carro está livre para circular hoje.')
#     case 'quarta' :
#         if placa == 5 or placa == 6:
#             print('Seu carro está proibido de circular hoje.')
#         else:
#             print('Seu carro está livre para circular hoje.')
#     case 'quinta' :
#         if placa == 7 or placa == 8:
#             print('Seu carro está proibido de circular hoje.')
#         else:
#             print('Seu carro está livre para circular hoje.')
#     case 'sexta' :
#         if placa == 9 or placa == 0:
#             print('Seu carro está proibido de circular hoje.')
#         else:
#             print('Seu carro está livre para circular hoje.')
#     case _:
#         print('informação inválida')

#exercicio5

