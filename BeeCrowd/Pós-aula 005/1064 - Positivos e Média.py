cont = 0
contN = 0
soma = 0
while cont < 6:
    x = float(input())
    if x>0:
        contN += 1
        soma = soma + x
        total = soma / contN
    cont+=1
print(contN, "valores positivos")
print('%.1f' %total)
