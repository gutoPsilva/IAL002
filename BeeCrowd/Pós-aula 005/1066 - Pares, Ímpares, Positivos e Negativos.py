cont = 0
nPar = 0
nImp = 0
nPos = 0
nNeg = 0
while cont<5:
    n = int(input())
    if n%2 == 0:
        nPar+=1
    else:
        nImp+=1
    if n>0:
        nPos+=1
    elif n<0:
        nNeg+=1
    cont+=1
print(nPar, 'valor(es) par(es)')
print(nImp, 'valor(es) impar(es)')
print(nPos, 'valor(es) positivo(s)')
print(nNeg, 'valor(es) negativo(s)')
