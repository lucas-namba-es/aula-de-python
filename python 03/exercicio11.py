'''
escreva um programa para calcular o valor de uma conta de energia eletrica de um consumidor, com base no consumo em kWh.

consumo < 150kWh    -0.20
150 >= consumo < 500kWh    -0.25
consumo>= 500       -0.30
taxa minima  - 11.90

o programa deve imprimir o consumo em kWh e o valor total a pagar.

'''

consumo = float(input('digite aqui o seu consumo de energia total em kWh: '))

if 0 < consumo < 150:
    valor_total = (consumo*0.75)
    tarifa = 0.75 
elif 150 <= consumo < 500:
    valor_total = (consumo*0.95)
    tarifa = 0.95
elif consumo >= 500:
    valor_total = (consumo*1.20)
    tarifa = 1.20

#valor_total = consumo*tarifa


if valor_total >= 45:
    pass
else:
    valor_total = 45

print('----------------------------------------------------------------------------------')
print(f' O seu consumo registrado é {consumo}\n O valor da tarifa é {tarifa}\n O valor calculado é {valor_total}')
print('----------------------------------------------------------------------------------')



