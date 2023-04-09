minimo = int(input('Valor mínimo: '))
maximo = int(input('Valor máximo: '))
if minimo>maximo:
    print('O valor mínimo é maior que o máximo. Digite novos valores!')
    minimo = int(input('Valor mínimo: '))
    maximo = int(input('Valor máximo: '))
while maximo>=minimo:
    if minimo%5==0:
        print('%.d' %minimo)
    minimo+=1
print('\n\nFim do Programa')
