'''escreva um programa que calcule a media de um aluno com 3 notas, deve mostrar a media obtida'''


'''
    - solicitar o nome do aluno
    - solicitar o numero de faltas
    - adicionar a condição do aluno realizar o exame
       - aprovação -> media >= 6 e numero de faltas <=18
       - reprovação -> numero de faltas <= 18
       - exame -> se a média for < 6 ou numero de faltas >=18
          - obter uma nova nota
          - calcular média
          - verificação se aprovado ou reprovado
'''
nome = str(input('Nome: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
nfaltas = float(input('Faltas: '))
 
media = (n1+n2+n3)/3

if media >= 6 and nfaltas <= 18:
    print(f'Aprovado! \nSua média é {media}')
    
elif media <= 6 or nfaltas >= 18:
    print(f'será necessário fazer um exame')
    nexame = float (input('Nota do exame: '))
    nmedia = (nexame + media)/2

if nmedia >= 6:
    print(f'Aprovado!')
else:
    print(f'Reprovado')
