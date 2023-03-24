cont = 0
nPar = 0
while cont<5:
    n = int(input())
    if n%2 == 0:
        nPar += 1
    cont+=1
print(nPar, 'valores pares')
