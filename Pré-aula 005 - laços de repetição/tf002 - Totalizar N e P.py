totalN = 0
totalP = 0
ini = 1
while ini != 0:
    X = int(input("Digite um valor inteiro: "))
    if X<0:
        totalN += X
    elif X>0:
        totalP += X
    else:
        print("Total dos positivos = %d" %totalP)
        print("Total dos negativos = %d" %totalN)
        ini = 0 # fecha o while
