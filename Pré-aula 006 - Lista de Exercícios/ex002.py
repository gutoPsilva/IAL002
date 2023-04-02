minimo = int(input('Valor mínimo: '))
maximo = int(input('Valor máximo: '))
if minimo>maximo:
    print('O valor mínimo é maior que o máximo. Digite novos valores!')
    minimo = int(input('Valor mínimo: '))
    maximo = int(input('Valor máximo: '))
while maximo>minimo:
    if maximo%5==0:
        print('%.d' %maximo)
    maximo-=1
print('\n\nFim do Programa')
#este algoritmo desconsidera o valor mínimo na hora de exibir os divisíveis
