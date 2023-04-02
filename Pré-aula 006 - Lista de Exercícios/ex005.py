n = int(input('Digite um valor: '))
while n!=0:
    if n%2 == 0 and n%3 == 0:
        print('{} é divisível por 2 e por 3'.format(n))
    elif n%2 == 0:
        print('{} é divisível por 2'.format(n))
    elif n%3 == 0:
        print('{} é divisível por 3'.format(n))
    else:
        print('{} não e divisível nem por 2 nem por 3'.format(n))
    n = int(input('Digite um valor: '))
print('\n\nFim do Programa')
