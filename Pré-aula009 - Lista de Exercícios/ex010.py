from random import randint
N = int(input("Digite o valor de N: "))
L = []
i = 0
while i < N:
    x = randint(0, 1000)
    L.append(x)
    i+=1
print(L)

X = int(input("Verifique se o valor está na lista: "))
i = 0 # reiniciar cont
tamanho = 0 # já que ñ pode usar Len, essa variável vai receber a qntd de elementos no zIndex.
zIndex = []
while i < N:
    if X == L[i]:
        zIndex.append(i)
        tamanho += 1
    i+=1

if tamanho > 1:
    print("O valor aparece mais de uma vez na lista, suas respectivas posições são: {}.".format(zIndex))
elif tamanho == 1:
    print("O valor está na lista, sua posição é: {}".format(zIndex))
else:
    print("Não está na lista.")

print("\n\nIsso é tudo pessoal!")