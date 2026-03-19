
print('---calculando a media---')




a = float(input('nota 1: '))
b = float(input('nota 2: '))
c = float(input('nota 3:'))

media = (a+b+c)/3

print(f'média: , {media}')

if media >= 6:
    print('Aprovado!')
else:
    print('Reprovado')