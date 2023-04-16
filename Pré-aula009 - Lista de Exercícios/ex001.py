L = []
i = 0
while len(L) < 10:
    n = int(input("Digite o elemento de posição {}:".format(i+1)))
    L.append(n)
    i += 1

for elemento in L:
    print(elemento)
