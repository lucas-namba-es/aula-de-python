# Calculadora simples

# funções:
# - menu()
# - obter_numero()
# - add()
# - sub()
# - div()
# - mult()
# - imprimir()
# - controlador()

# --- menu ---

def menu():
    opcao = 0
    while opcao < 1 or opcao > 4:
        print('--- menu ---')
        print('1 - Adição')
        print('2 - Subtração')
        print('3 - Multiplicção')
        print('4 - Divisão')
        opcao = int(input('Opção: '))
        if opcao < 1 or opcao > 4:
            print('Opção invalida, tente denovo.')
    return opcao

# --- obter número ---

def obter_numero():
    print('---Obter número---')
    numero = int(input('Número: '))
    return numero

# --- Adição ---

def add(a, b):
    print('--- Adição ---')
    return a + b

# --- Subtração ---

def sub(a, b):
    print('--- Subtração ---')
    return a - b

# --- Divisão ---

def div(a, b):
    print('--- Divisão ---')
    return a/b

# --- multiplicação ---

def mult(a, b):
    print('--- Multiplicação ---')
    return a*b

# --- imprimir ---

def imprimir(resultado):
    print('--- imprimir ---')
    print('----------------')
    print(f'Resultado: {resultado}')
    print('----------------')

# --- controlador ---

def controlador(opcao, a, b):
    print('--- Controlador ---')
    if opcao == 1:
        result = add(a, b)
    elif opcao == 2:
        result = sub(a, b)
    elif opcao == 3:
        result = mult(a, b)
    elif opcao == 4:
        result = div(a, b)
    return result

# --- MAIN ---

opcao = menu()
n1 = obter_numero()
n2 = obter_numero()
resultado = controlador(opcao, n1, n2)
imprimir(resultado)