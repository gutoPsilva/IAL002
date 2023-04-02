n = int(input())
ini = 0
p1 = 1
p2 = 1
p3 = 1
while n*2>ini:
    print(p1, p2, p3)
    contP1 = 0
    while contP1<2:
        contP1+=1
    if contP1 == 2: # reiniciar o contador a cada 2 linhas
        contP1 = 0
        p1 += 1 # a cada 2 linhas, soma o p1
        print(p1)
    ini+=1
