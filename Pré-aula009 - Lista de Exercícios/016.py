n = int(input("Digite N: "))
i = 0
L = []
while i < n:
    x = int(input("Digite valores para inserir: "))
    if x in L:
        print("{} já está na lista.".format(x))
    else:
        L.append(x)
        i += 1 # considera apenas os que forem adicionados
print(L)
