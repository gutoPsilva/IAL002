from random import randint
N = int(input("Digite o valor de N: "))
L = []
i = 0
while i < N:
    x = randint(0, 1000)
    L.append(x)
    i+=1
print(L)

X = int(input("Verifique se o valor está na lista e deleta-lo: "))

# ALGORITMO BUSCA SEQUENCIAL E ELIMINAÇÃO
i = 0 # reiniciar cont
while i < N:
    if X == L[i]: # caso de deletar
        del L[i]
        N -= 1 # deduz 1 da lista, já que 1 index foi tirado da lista
    else: # senão deletar
        i += 1 # adiciona 1 ao index para fechamento do while
print(L)

print("\n\nIsso é tudo pessoal!")
