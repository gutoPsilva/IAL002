n = int(input('Digite um valor máximo: '))
while n<100:
    print('O valor digitado deve ser pelo menos 100!')
    n=int(input('Digite um valor máximo: '))
valor = 1
while valor<n:
    if valor%2 == 0:
        print('{:3d} é um valor par'.format(valor))
    valor+=1
if n%2 == 0:
    print('{} o próprio máximo é um valor par!'.format(n))
print('\n\nFim do Programa')
