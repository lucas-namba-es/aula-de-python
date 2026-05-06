def menor_numero(n1, n2, n3):
    print('---Menor-numero---')
    if n1<n2 and n1<n3:
        return n1
    elif n2<n1 and n2<n3:
        return n2
    else:
        return n3 
def obter_numero():
    print('---oberter numero---')
    n = int(input("Número 1: "))

    return n

def imprimir(menor):
    print(f'Menor número: {menor}')


n1 = obter_numero()
n2 = obter_numero()
n3 = obter_numero()
retorno = menor_numero(n1, n2, n3)
imprimir(retorno)