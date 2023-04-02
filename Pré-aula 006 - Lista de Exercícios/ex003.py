n = int(input('Quantas vezes queres comparar 2 números: '))
while n > 0:
    f1 = float(input('Digite o primeiro número: '))
    f2 = float(input('Digite o segundo número:  '))
    if f1 == f2:
        print("{} é igual a {}".format(f1, f2))
    elif f1 > f2:
        print("{} é maior que {}".format(f1, f2))
    else:
        print("{} é maior que {}".format(f2, f1))
    n-=1
print('\n\nFim do Programa')
