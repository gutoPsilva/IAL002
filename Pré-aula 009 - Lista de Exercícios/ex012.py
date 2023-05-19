from random import randint
N = int(input("Digite o valor de N: "))
L = []
i = 0
while i < N:
    x = randint(1, 2)
    L.append(x)
    i+=1
print(L)


# ALGORITMO de eliminação de cópias
Eliminados = []
i = 0
while i < N:
    j = N - 1 # j vai comparar o valor do index FINAL até o index "inicial"
    while j > i:
        if L[j] == L[i]:
            Eliminados.append((L[j], j))
            del(L[j])
            N-=1
        j -= 1
    i+=1
print("Apos eliminação:\n {}".format(L))

for a in Eliminados:
    print(a)

print("\n\nIsso é tudo pessoal!")
