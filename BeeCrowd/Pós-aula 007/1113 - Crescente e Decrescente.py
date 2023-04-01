linha = input().split()
X = int(linha[0])
Y = int(linha[1])
while X!=Y:
    if X<Y:
        print('Crescente')
    else:
        print('Decrescente')
    linha = input().split()
    X = int(linha[0])
    Y = int(linha[1])
