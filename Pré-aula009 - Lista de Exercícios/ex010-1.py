from random import randint

def printar(lista):
    i = 0
    while i < N:
        print("{:4}".format(lista[i]), end=' ')
        i+=1
        if i > 0 and i % 10 == 0:
            print()

def teste2(zIndex):
    
    
N = int(input("Digite o valor de N: "))
L = []
i = 0
while i < N:
    x = randint(0, 1)
    L.append(x)
    i+=1
printar(L)

X = int(input("\n\nVerifique se o valor está na lista: "))
i = 0 # reiniciar cont
tamanho = 0 # já que ñ pode usar Len, essa variável vai receber a qntd de elementos no zIndex.
zIndex = []
while i < N:
    if X == L[i]:
        zIndex.append(i)
        tamanho += 1
    i+=1

if tamanho > 1:
    
    print("O valor aparece {} vezes na lista, suas respectivas posições são: {}.".format(len(zIndex), teste2(zIndex))
elif tamanho == 1:
    print("O valor está na lista, sua única posição é: {}".format(zIndex))
else:
    print("Não está na lista.")

print("\n\nIsso é tudo pessoal!")
