N = int(input('Digite um valor máximo: '))
while N<100:
    print('O valor digitado deve ser pelo menos 100!')
    N=int(input('Digite um valor máximo: '))
valor = 2
total = 0
while valor<=N:
    if valor%2 == 0: # é par
        total += valor
    valor+=2 # só é par de 2 em 2
print("A somatória de tudo é: {}".format(total))
print('\n\nFim do Programa')
