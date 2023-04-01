linha = input().split()
X = int(linha[0])
Y = int(linha[1])
while X != 0 and Y != 0:
    if X>0:
        if Y>0:
            print('primeiro')
        else:
            print('quarto')
    else:
        if Y>0:
            print('segundo')
        else:
            print('terceiro')
    linha = input().split()
    X = int(linha[0])
    Y = int(linha[1])
