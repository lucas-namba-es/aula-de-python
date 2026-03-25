inicio = int(input('número: '))
fim = int(input('fim: '))

if inicio <= fim:
  while inicio <= fim:    
      print(inicio)
      inicio += 1
else:
   while fim < inicio:
      print(inicio)
      inicio -= 1
