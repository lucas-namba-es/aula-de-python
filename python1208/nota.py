
def media_cp():

    print('----Notas das CP----')
    cp1 = float(input('Nota do cp1: '))
    cp2 = float(input('Nota do cp2: '))
    cp3 = float(input('Nota do cp3: '))

    if cp1<cp2 and cp1<cp3:
        cp = (cp2 + cp3) / 2
    elif cp2<cp1 and cp2<cp3:
        cp = (cp1 + cp3) / 2
    else:
        cp = (cp1 + cp2) / 2

    print(f'Sua média da CP foi {cp}')
    return cp

def media_sp():

    print('----Notas dos SP----')
    sp1 = float(input('Nota do sp1: '))
    sp2 = float(input('Nota do sp2: '))

    sp = (sp1 + sp2) / 2 
    print(f'Sua média da SP foi {sp}')

    return sp 

def obter_gs():

    print('----Nota da GS----')
    gs = float(input('Nota da GS: '))
    print(f'Sua nota da GS foi {gs}')

    return gs

def calculo_medias1():

    cp = media_cp()
    sp = media_sp()
    gs = obter_gs()

    resultado = ((cp * 0.2) + (sp * 0.2) + (gs * 0.6) * 0.6)

    print(f'Sua nota do primeiro semestre foi {resultado}')

    return resultado

def calculo_medias2():

    cp = media_cp()
    sp = media_sp()
    gs = obter_gs()

    resultado = ((cp * 0.2) + (sp * 0.2) + (gs * 0.6) * 0.6)
    print(f'Sua nota do primeiro semestre foi {resultado}')

    return resultado

def media_final():

    nota_final = (calculo_medias1 * 0.4) + (calculo_medias2 * 0.6)

    print(f'{nota_final}')

    return nota_final

media_final()


    






