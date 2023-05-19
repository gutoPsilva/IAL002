L = []
i = 0
while len(L) < 10:
    n = int(input("Digite o elemento de posição {}:".format(i+1)))
    L.append(n)
    i += 1

# desse modo apenas altera a exibição, e não a ordem real da lista
# utilizando L.reverse() e depois o for, ai sim, a ordem é realmente alterada na lista
for elemento in range(len(L)-1, -1, -1):
    print(L[elemento])
    
print("\n\nIsso é tudo pessoal!")