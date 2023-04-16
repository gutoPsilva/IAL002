n = int(input("Digite N: "))
i = 0
L = []
while i < n: # adiciona os elementos
    m = int(input("Digite o elemento {}: ".format(i+1)))
    L.append(m)
    i += 1
print(L)

i = 0
j = -1
while i < len(L): # remover os elementos duplicados
    print(i, L[j])
    if L[i] == L[j]:
        del L[j]
        j-=1
    else:
        i+=1
print(L)
