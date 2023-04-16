from random import randint
N = int(input("Digite o valor de N: "))
i = 0
L = []
while i < N:
    z = randint(0, 1000)
    L.append(z)
    i+=1
print(L)
X = int(input("Verificar se o elemento está na lista: "))
if X in L:
    print("{} está na lista.".format(X))
else:
    print("{} NÃO está na lista.".format(X))
print("\n\nIsso é tudo pessoal!")
