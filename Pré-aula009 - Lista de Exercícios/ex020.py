from random import randint
n = int(input("Digite N: "))
while n<11:
    print("N deve ser maior que 10!")
    n = int(input("Digite N: "))
i = 0
L = []
while i < n:
    x = randint(1,1000)
    L.append(x)
    i += 1
print("Lista desordenada: \n{}".format(L))

# bubble-sort
# pega um elemento index e compara com o próximo para ver qual é maior
# se for menor, para, senão, continua.
exchanges = True
passnum = len(L)-1 # -1 pois o range pega do 0 até -1 do Len
while passnum > 0 and exchanges:
    exchanges = False # não houve troca ainda
    for i in range(passnum):
        if L[i] > L[i+1]: # se o e1 for maior que e2, a troca é feita!
            exchanges = True
            temp = L[i]
            L[i] = L[i+1]
            L[i+1] = temp
    passnum -= 1

print("Lista ordenada: \n{}".format(L))

print("\n\nIsso é tudo pessoal!")