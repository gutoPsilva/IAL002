from random import randint

def ExibeValores(valores):
    i = 0
    while i < len(valores):
        print("{:4}".format(valores[i]), end=' ')
        i+=1
        if i > 0 and i % 10 == 0:
            print()
N = int(input("Digite o valor de N: "))
i = 0
L = []
while i < N:
    z = randint(0, 1000)
    L.append(z)
    i+=1
ExibeValores(L)
X = int(input("\n\nVerificar se o elemento está na lista: "))
if X in L:
    print("{} está na lista.".format(X))
else:
    print("{} NÃO está na lista.".format(X))
    
print("\n\nIsso é tudo pessoal!")
