N = int(input('Digite N: '))
i = 0
while i < N:
    X = float(input('Digite o elemento {}: '.format(i+1)))
    if X > 0:
        if i == 0 or X < menor:
            menor = X
        if i == 0 or X > maior:
            maior = X
        i+=1
    else:
        print("número inválida")
if N>0:
    print("Menor valor = {}".format(menor))
    print("Maior valor = {}".format(maior))
else:
    print("A quantidade N não é válida")
print('\n\nFim do Programa')
