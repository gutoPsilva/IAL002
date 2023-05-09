L = []
N = int(input("Digite o tamanho da lista: "))
print("Elementos na lista")
i = 0
while i < N:
    X = int(input(" elemento {}: ".format(i+1)))
    if X not in L:
        L.append(X)
        i+=1
    else:
        print("{} ignorado pois já está na lista".format(i))

print("Lista final:\n{}".format(L))
print("\n\n Isso é tudo pessoal!")
