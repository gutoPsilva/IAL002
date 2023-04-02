n = int(input('Digite um valor: '))
cont = 0
soma = 0
media = 0
while n>0:
    n1 = 0
    n2 = 2
    #if n > n1:
    #    n1 = n # maior
    #else:
    #    n2 = n
    cont += 1
    soma += n
    media = soma/cont
    n = int(input('Digite um valor: '))
print('A quantidade de valores: %d' %cont)
print('Menor valor é: %d' %n2)
print('Maior valor é: %d' %n1)
print('A soma é: %d' %soma)
print('A média é: %.2f' %media)
